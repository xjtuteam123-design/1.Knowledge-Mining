"""SQLite-backed literature store with PDF-to-Markdown conversion and deduplication."""

from __future__ import annotations

import hashlib
import csv
import itertools
import json
import math
import re
import shutil
import sqlite3
import threading
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from pypdf import PdfReader


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MARKDOWN_DIR = DATA_DIR / "markdown"
STRUCTURED_DIR = DATA_DIR / "structured"
UPLOAD_DIR = DATA_DIR / "uploads"
INDEX_DIR = DATA_DIR / "index"
REPORTS_DIR = BASE_DIR / "reports"
DB_PATH = INDEX_DIR / "literature.db"
SUPPORTED_SUFFIXES = {".pdf", ".txt", ".md"}
_LOCK = threading.RLock()


def _connect() -> sqlite3.Connection:
    for directory in (MARKDOWN_DIR, STRUCTURED_DIR, UPLOAD_DIR, INDEX_DIR, REPORTS_DIR):
        directory.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH, timeout=60)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA journal_mode=WAL")
    connection.executescript(
        """
        CREATE TABLE IF NOT EXISTS documents (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            source_path TEXT NOT NULL,
            file_sha256 TEXT NOT NULL UNIQUE,
            text_sha256 TEXT NOT NULL UNIQUE,
            markdown_path TEXT NOT NULL,
            pages INTEGER NOT NULL,
            chunk_count INTEGER NOT NULL,
            structured INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id TEXT NOT NULL,
            source TEXT NOT NULL,
            page INTEGER,
            kind TEXT NOT NULL,
            text TEXT NOT NULL,
            FOREIGN KEY(document_id) REFERENCES documents(id) ON DELETE CASCADE
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
            chunk_id UNINDEXED,
            text,
            tokens,
            tokenize='unicode61'
        );
        CREATE INDEX IF NOT EXISTS idx_chunks_document_id ON chunks(document_id);
        CREATE TABLE IF NOT EXISTS duplicates (
            source_path TEXT PRIMARY KEY,
            canonical_document_id TEXT NOT NULL,
            reason TEXT NOT NULL,
            detected_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS failures (
            source_path TEXT PRIMARY KEY,
            error TEXT NOT NULL,
            detected_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS retrieval_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_text TEXT NOT NULL,
            query_tokens TEXT NOT NULL,
            mode TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        CREATE VIRTUAL TABLE IF NOT EXISTS retrieval_questions_fts USING fts5(
            question_id UNINDEXED,
            query_text,
            query_tokens,
            tokenize='unicode61'
        );
        CREATE TABLE IF NOT EXISTS retrieval_question_chunks (
            question_id INTEGER NOT NULL,
            chunk_id INTEGER NOT NULL,
            document_id TEXT NOT NULL,
            relevance REAL NOT NULL DEFAULT 0,
            cited INTEGER NOT NULL DEFAULT 0,
            PRIMARY KEY(question_id, chunk_id)
        );
        CREATE INDEX IF NOT EXISTS idx_retrieval_question_chunks_question
            ON retrieval_question_chunks(question_id);
        CREATE INDEX IF NOT EXISTS idx_retrieval_question_chunks_chunk
            ON retrieval_question_chunks(chunk_id);
        CREATE TABLE IF NOT EXISTS retrieval_chunk_stats (
            chunk_id INTEGER PRIMARY KEY,
            document_id TEXT NOT NULL,
            question_count INTEGER NOT NULL DEFAULT 0,
            citation_count INTEGER NOT NULL DEFAULT 0,
            last_used_at TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_retrieval_chunk_stats_document
            ON retrieval_chunk_stats(document_id);
        """
    )
    return connection


def initialize() -> None:
    with _connect():
        pass


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _normalize_text(text: str) -> str:
    # Some PDF font maps emit lone UTF-16 surrogate code points. Replace only
    # those invalid Unicode values so an otherwise extractable paper is kept.
    text = text.encode("utf-8", errors="replace").decode("utf-8")
    text = text.replace("\x00", " ").replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _normalized_for_hash(text: str) -> str:
    text = text.encode("utf-8", errors="replace").decode("utf-8")
    return re.sub(r"\s+", "", text).lower()


def _safe_stem(name: str, limit: int = 90) -> str:
    stem = Path(name).stem
    stem = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", stem).strip(" ._")
    return (stem or "document")[:limit]


def _extract(path: Path) -> list[tuple[int | None, str]]:
    if path.suffix.lower() == ".pdf":
        reader = PdfReader(str(path))
        return [(number, page.extract_text() or "") for number, page in enumerate(reader.pages, 1)]
    for encoding in ("utf-8", "utf-8-sig", "gb18030"):
        try:
            return [(None, path.read_text(encoding=encoding))]
        except UnicodeDecodeError:
            continue
    raise ValueError("Unsupported text encoding")


def _to_markdown(name: str, source: Path, file_hash: str, pages: list[tuple[int | None, str]]) -> str:
    header = (
        f"# {Path(name).stem}\n\n"
        f"<!-- source: {source} -->\n"
        f"<!-- file_sha256: {file_hash} -->\n\n"
    )
    body = []
    for page, text in pages:
        normalized = _normalize_text(text)
        if not normalized:
            continue
        if page is not None:
            body.append(f"## Page {page}\n\n{normalized}")
        else:
            body.append(normalized)
    return header + "\n\n".join(body) + "\n"


def _chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    text = _normalize_text(text)
    if not text:
        return []
    output: list[str] = []
    start = 0
    while start < len(text):
        hard_end = min(start + chunk_size, len(text))
        end = hard_end
        if hard_end < len(text):
            lower = start + max(chunk_size // 2, 1)
            boundaries = [text.rfind(mark, lower, hard_end) for mark in ("\n\n", "。", "！", "？", ". ", "; ")]
            boundary = max(boundaries)
            if boundary > start:
                end = boundary + (2 if text[boundary : boundary + 2] == "\n\n" else 1)
        value = text[start:end].strip()
        if value:
            output.append(value)
        if end >= len(text):
            break
        start = max(end - overlap, start + 1)
    return output


def _chunk_structured(text: str, chunk_size: int = 2400) -> list[str]:
    sections = re.split(r"(?=^#\s)", _normalize_text(text), flags=re.MULTILINE)
    output: list[str] = []
    for section in sections:
        section = section.strip()
        if not section:
            continue
        output.extend([section] if len(section) <= chunk_size else _chunk_text(section, chunk_size, 150))
    return output


def _search_tokens(text: str) -> str:
    lowered = text.lower()
    tokens = re.findall(r"[a-z0-9]+(?:[-_.][a-z0-9]+)*", lowered)
    for run in re.findall(r"[\u3400-\u9fff]+", lowered):
        # Index/query complete Chinese runs and overlapping bigrams. Expanding
        # every run into single characters made greetings such as "你好" match
        # unrelated materials text containing common characters such as "好".
        tokens.append(run)
        tokens.extend(run[i : i + 2] for i in range(len(run) - 1))
    return " ".join(dict.fromkeys(token for token in tokens if token))


def _insert_chunk(connection: sqlite3.Connection, document_id: str, source: str, page: int | None, kind: str, text: str) -> None:
    cursor = connection.execute(
        "INSERT INTO chunks(document_id, source, page, kind, text) VALUES (?, ?, ?, ?, ?)",
        (document_id, source, page, kind, text),
    )
    connection.execute(
        "INSERT INTO chunks_fts(chunk_id, text, tokens) VALUES (?, ?, ?)",
        (cursor.lastrowid, text, _search_tokens(text)),
    )


def ingest_path(
    path: str | Path,
    chunk_size: int = 900,
    overlap: int = 150,
    analyzer: Callable[[str, str], str] | None = None,
    copy_upload: bool = False,
    pages_override: list[tuple[int | None, str]] | None = None,
) -> dict[str, Any]:
    source = Path(path).resolve()
    if source.suffix.lower() not in SUPPORTED_SUFFIXES:
        return {"status": "skipped", "source": str(source), "reason": "unsupported extension"}
    chunk_size = max(300, min(int(chunk_size), 3000))
    overlap = max(0, min(int(overlap), chunk_size // 2))
    now = datetime.now(timezone.utc).isoformat()

    with _LOCK, _connect() as connection:
        existing_path = connection.execute(
            "SELECT id FROM documents WHERE source_path=?", (str(source),)
        ).fetchone()
        if existing_path:
            connection.execute("DELETE FROM failures WHERE source_path=?", (str(source),))
            return {"status": "already_indexed", "source": str(source), "id": existing_path["id"]}
        known_duplicate = connection.execute(
            "SELECT canonical_document_id FROM duplicates WHERE source_path=?", (str(source),)
        ).fetchone()
        if known_duplicate:
            connection.execute("DELETE FROM failures WHERE source_path=?", (str(source),))
            return {
                "status": "already_indexed",
                "source": str(source),
                "id": known_duplicate["canonical_document_id"],
            }

    file_hash = _sha256_file(source)
    with _LOCK, _connect() as connection:
        existing = connection.execute(
            "SELECT id, source_path FROM documents WHERE file_sha256=?", (file_hash,)
        ).fetchone()
        if existing:
            if Path(existing["source_path"]).resolve() == source:
                return {"status": "already_indexed", "source": str(source), "id": existing["id"]}
            connection.execute(
                "INSERT OR REPLACE INTO duplicates VALUES (?, ?, ?, ?)",
                (str(source), existing["id"], "identical_file", now),
            )
            return {"status": "duplicate", "source": str(source), "reason": "identical_file"}

    try:
        pages = pages_override if pages_override is not None else _extract(source)
        full_text = "\n\n".join(text for _, text in pages if text.strip())
        normalized = _normalized_for_hash(full_text)
        if not normalized:
            raise ValueError("No extractable text; OCR is required")
        text_hash = hashlib.sha256(normalized.encode("utf-8")).hexdigest()

        with _LOCK, _connect() as connection:
            existing = connection.execute(
                "SELECT id, source_path FROM documents WHERE text_sha256=?", (text_hash,)
            ).fetchone()
            if existing:
                if Path(existing["source_path"]).resolve() == source:
                    return {"status": "already_indexed", "source": str(source), "id": existing["id"]}
                connection.execute(
                    "INSERT OR REPLACE INTO duplicates VALUES (?, ?, ?, ?)",
                    (str(source), existing["id"], "identical_normalized_text", now),
                )
                return {"status": "duplicate", "source": str(source), "reason": "identical_normalized_text"}

        document_id = text_hash[:16]
        markdown_name = f"{document_id}-{_safe_stem(source.name)}.md"
        markdown_path = MARKDOWN_DIR / markdown_name
        markdown = _to_markdown(source.name, source, file_hash, pages)
        markdown_path.write_text(markdown, encoding="utf-8")

        structured_text = analyzer(source.name, markdown) if analyzer else ""
        if structured_text:
            (STRUCTURED_DIR / markdown_name).write_text(structured_text.strip() + "\n", encoding="utf-8")

        raw_chunks: list[tuple[int | None, str]] = []
        for page, text in pages:
            raw_chunks.extend((page, chunk) for chunk in _chunk_text(text, chunk_size, overlap))
        structured_chunks = _chunk_structured(structured_text) if structured_text else []
        chunk_count = len(raw_chunks) + len(structured_chunks)

        with _LOCK, _connect() as connection:
            connection.execute(
                "INSERT INTO documents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    document_id,
                    source.name,
                    str(source),
                    file_hash,
                    text_hash,
                    str(markdown_path.relative_to(BASE_DIR)),
                    len(pages),
                    chunk_count,
                    int(bool(structured_text)),
                    now,
                ),
            )
            for page, chunk in raw_chunks:
                _insert_chunk(connection, document_id, source.name, page, "original_text", chunk)
            for chunk in structured_chunks:
                _insert_chunk(connection, document_id, source.name, None, "structured_analysis", chunk)
            connection.execute("DELETE FROM failures WHERE source_path=?", (str(source),))

        if copy_upload:
            destination = UPLOAD_DIR / f"{document_id}{source.suffix.lower()}"
            if not destination.exists():
                shutil.copy2(source, destination)
        return {"status": "indexed", "source": str(source), "id": document_id, "chunks": chunk_count}
    except Exception as exc:
        with _LOCK, _connect() as connection:
            connection.execute(
                "INSERT OR REPLACE INTO failures VALUES (?, ?, ?)",
                (str(source), str(exc), now),
            )
        return {"status": "failed", "source": str(source), "error": str(exc)}


def _uploaded_path(file: Any) -> Path:
    if isinstance(file, (str, Path)):
        return Path(file)
    return Path(getattr(file, "path", None) or getattr(file, "name", ""))


def add_documents(files: list[Any] | Any | None, chunk_size: int = 900, overlap: int = 150, analyzer=None) -> str:
    if not files:
        return "Please select one or more PDF, TXT, or Markdown files."
    if not isinstance(files, list):
        files = [files]
    results = [ingest_path(_uploaded_path(file), chunk_size, overlap, analyzer, True) for file in files]
    messages = []
    for result in results:
        name = Path(result["source"]).name
        if result["status"] == "indexed":
            messages.append(f"Indexed: {name} ({result['chunks']} chunks)")
        elif result["status"] == "already_indexed":
            messages.append(f"Already indexed: {name}")
        elif result["status"] == "duplicate":
            messages.append(f"Skipped duplicate: {name} ({result['reason']})")
        else:
            messages.append(f"Failed: {name} — {result.get('error', result.get('reason'))}")
    return "\n\n".join(messages)


def list_documents() -> list[list[Any]]:
    with _connect() as connection:
        rows = connection.execute("SELECT name, chunk_count FROM documents ORDER BY created_at DESC").fetchall()
    return [[row["name"], row["chunk_count"]] for row in rows]


def clear_documents() -> tuple[str, list[list[Any]]]:
    with _LOCK, _connect() as connection:
        connection.execute("DELETE FROM chunks_fts")
        connection.execute("DELETE FROM chunks")
        connection.execute("DELETE FROM documents")
        connection.execute("DELETE FROM duplicates")
        connection.execute("DELETE FROM failures")
    for directory in (MARKDOWN_DIR, STRUCTURED_DIR, UPLOAD_DIR):
        for path in directory.iterdir():
            if path.is_file():
                path.unlink()
    return "The local literature library has been cleared.", []


def search(
    query: str,
    top_k: int = 5,
    document_ids: list[str] | tuple[str, ...] | set[str] | None = None,
) -> list[dict[str, Any]]:
    tokens = list(dict.fromkeys(_search_tokens(query).split()))
    if not tokens:
        return []
    active_ids = list(dict.fromkeys(str(value) for value in document_ids or []))
    if document_ids is not None and not active_ids:
        return []
    expression = " OR ".join('"' + token.replace('"', '""') + '"' for token in tokens[:80])
    document_filter = ""
    parameters: list[Any] = [expression]
    if active_ids:
        placeholders = ",".join("?" for _ in active_ids)
        document_filter = f" AND c.document_id IN ({placeholders})"
        parameters.extend(active_ids)
    parameters.append(max(1, int(top_k)))
    with closing(_connect()) as connection:
        rows = connection.execute(
            f"""
            SELECT c.id AS chunk_id, c.document_id, c.source, c.page, c.kind, c.text,
                   -bm25(chunks_fts) AS score
            FROM chunks_fts JOIN chunks c ON c.id = CAST(chunks_fts.chunk_id AS INTEGER)
            WHERE chunks_fts MATCH ?{document_filter}
            ORDER BY bm25(chunks_fts) LIMIT ?
            """,
            parameters,
        ).fetchall()
    return [dict(row) for row in rows]


_QUERY_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "how", "in", "is", "it", "of", "on", "or", "that", "the", "this",
    "to", "was", "were", "what", "when", "which", "with", "does", "do",
    "did", "affect", "affects", "effect", "effects", "impact", "impacts",
    "influence", "influences", "explain", "compare", "role",
}


def _query_relevance_terms(query: str) -> list[str]:
    """Return meaningful, deduplicated terms for global scoped retrieval."""
    terms = _search_tokens(query).split()
    return [
        term
        for term in dict.fromkeys(terms)
        if term and term not in _QUERY_STOPWORDS
    ][:80]


def _lexical_relevance(text: str, terms: list[str], query: str = "") -> float:
    """Score query coverage and term frequency on a stable 0-100 scale."""
    if not terms:
        return 0.0
    lowered = str(text or "").casefold()
    counts = [lowered.count(term.casefold()) for term in terms]
    matched = sum(1 for count in counts if count)
    if not matched:
        return 0.0

    coverage = matched / len(terms)
    frequency = min(1.0, sum(min(count, 4) for count in counts) / max(2 * len(terms), 1))
    score = 80.0 * coverage + 20.0 * frequency

    normalized_query = re.sub(r"\s+", " ", str(query or "").casefold()).strip()
    if len(normalized_query) >= 3 and normalized_query in lowered:
        score += 10.0
    return round(min(score, 100.0), 2)


def search_global(
    query: str,
    document_ids: list[str] | tuple[str, ...] | set[str],
    minimum_relevance: float = 0.0,
) -> list[dict[str, Any]]:
    """Use SQLite FTS to recall every lexical match in the active corpus.

    The old implementation loaded every chunk into Python for every question.
    Here the full active corpus remains eligible, but the inverted index skips
    chunks that contain none of the meaningful query terms. No result-count
    limit is applied: the caller controls evidence with a relevance threshold
    and a context budget instead of an arbitrary top-k.
    """
    active_ids = list(dict.fromkeys(str(value) for value in document_ids or []))
    if not active_ids:
        return []
    terms = _query_relevance_terms(query)
    if not terms:
        return []
    quoted_terms = ['"' + term.replace('"', '""') + '"' for term in terms]
    # A chunk can receive at most 20 frequency points and the answer pipeline
    # adds at most 7 non-history points (numeric + graph support). Requiring the
    # mathematically necessary term coverage inside SQLite prevents broad OR
    # queries from copying tens of thousands of impossible candidates into
    # Python, while never imposing a fixed result count.
    required_lexical = max(0.0, float(minimum_relevance) - 7.0)
    minimum_coverage = max(0.0, (required_lexical - 20.0) / 80.0)
    minimum_matches = max(1, math.ceil(minimum_coverage * len(terms)))
    combination_count = math.comb(len(terms), minimum_matches)
    if minimum_matches > 1 and combination_count <= 160:
        # Express "at least N query terms" directly in the FTS inverted index.
        # This is much faster than OR-recalling every generic term and checking
        # coverage against the full text afterwards.
        expression = " OR ".join(
            "(" + " AND ".join(group) + ")"
            for group in itertools.combinations(quoted_terms, minimum_matches)
        )
        coverage_clause = ""
        coverage_parameters: tuple[Any, ...] = ()
    else:
        expression = " OR ".join(quoted_terms)
        coverage_expression = " + ".join(
            "CASE WHEN instr(lower(c.text), ?) > 0 THEN 1 ELSE 0 END"
            for _ in terms
        )
        coverage_clause = f"AND ({coverage_expression}) >= ?"
        coverage_parameters = (*[term.casefold() for term in terms], minimum_matches)
    rows: list[sqlite3.Row] = []
    with closing(_connect()) as connection:
        # Stay below SQLite's common 999-variable limit while supporting
        # future corpora containing far more than the current 500 papers.
        for start in range(0, len(active_ids), 750):
            batch = active_ids[start : start + 750]
            placeholders = ",".join("?" for _ in batch)
            rows.extend(
                connection.execute(
                    f"""
                    SELECT c.id AS chunk_id, c.document_id, c.source, c.page,
                           c.kind, c.text, -bm25(chunks_fts) AS fts_score
                    FROM chunks_fts
                    JOIN chunks c ON c.id=CAST(chunks_fts.chunk_id AS INTEGER)
                    WHERE chunks_fts MATCH ?
                      AND c.kind='original_text'
                      AND c.document_id IN ({placeholders})
                      {coverage_clause}
                    ORDER BY bm25(chunks_fts)
                    """,
                    (
                        expression,
                        *batch,
                        *coverage_parameters,
                    ),
                ).fetchall()
            )

    results = []
    for row in rows:
        result = dict(row)
        lexical = _lexical_relevance(result.get("text", ""), terms, query)
        result["lexical_relevance"] = lexical
        result["score"] = lexical
        result["relevance"] = lexical
        results.append(result)
    results.sort(
        key=lambda item: (
            float(item.get("relevance", 0.0)),
            float(item.get("fts_score", 0.0)),
        ),
        reverse=True,
    )
    return results


def count_original_chunks(
    document_ids: list[str] | tuple[str, ...] | set[str],
) -> int:
    """Count all active source chunks without loading their text."""
    active_ids = list(dict.fromkeys(str(value) for value in document_ids or []))
    if not active_ids:
        return 0
    total = 0
    with closing(_connect()) as connection:
        for start in range(0, len(active_ids), 900):
            batch = active_ids[start : start + 900]
            placeholders = ",".join("?" for _ in batch)
            total += int(
                connection.execute(
                    f"SELECT COUNT(*) FROM chunks WHERE kind='original_text' "
                    f"AND document_id IN ({placeholders})",
                    batch,
                ).fetchone()[0]
            )
    return total


def _term_similarity(left: set[str], right: set[str]) -> float:
    """Weighted overlap for short technical questions."""
    if not left or not right:
        return 0.0
    intersection = len(left.intersection(right))
    if not intersection:
        return 0.0
    containment = intersection / min(len(left), len(right))
    jaccard = intersection / len(left.union(right))
    return round(0.65 * containment + 0.35 * jaccard, 4)


def historical_chunk_priors(
    query: str,
    document_ids: list[str] | tuple[str, ...] | set[str],
    question_limit: int = 120,
) -> dict[int, dict[str, float | int]]:
    """Return bounded priors learned from genuinely similar past questions.

    History is deliberately a weak prior. It can promote a previously useful
    chunk into the candidate set, but current-query evidence still dominates
    the final rank and every new question continues to search the full index.
    """
    query_terms = set(_query_relevance_terms(query))
    active_ids = {str(value) for value in document_ids or []}
    if not query_terms or not active_ids:
        return {}
    expression = " OR ".join('"' + term.replace('"', '""') + '"' for term in query_terms)
    with closing(_connect()) as connection:
        questions = connection.execute(
            """
            SELECT q.id, q.query_tokens
            FROM retrieval_questions_fts f
            JOIN retrieval_questions q ON q.id=CAST(f.question_id AS INTEGER)
            WHERE retrieval_questions_fts MATCH ?
            ORDER BY bm25(retrieval_questions_fts)
            LIMIT ?
            """,
            (expression, max(1, int(question_limit))),
        ).fetchall()
        similar = {
            int(row["id"]): _term_similarity(query_terms, set(str(row["query_tokens"]).split()))
            for row in questions
        }
        similar = {question_id: score for question_id, score in similar.items() if score >= 0.28}
        if not similar:
            return {}
        placeholders = ",".join("?" for _ in similar)
        rows = connection.execute(
            f"""
            SELECT qc.question_id, qc.chunk_id, qc.document_id, qc.cited,
                   s.question_count, s.citation_count
            FROM retrieval_question_chunks qc
            LEFT JOIN retrieval_chunk_stats s ON s.chunk_id=qc.chunk_id
            WHERE qc.question_id IN ({placeholders})
            """,
            tuple(similar),
        ).fetchall()

    priors: dict[int, dict[str, float | int]] = {}
    for row in rows:
        if str(row["document_id"]) not in active_ids:
            continue
        chunk_id = int(row["chunk_id"])
        # Repeated support from similar questions raises confidence slowly;
        # citations are more valuable than mere selection.
        question_count = int(row["question_count"] or 0)
        citation_count = int(row["citation_count"] or 0)
        item = priors.setdefault(
            chunk_id,
            {
                "query_similarity": 0.0,
                "question_count": question_count,
                "citation_count": citation_count,
                "history_score": 0.0,
            },
        )
        # Use the strongest similar-question score because duplicate historic
        # questions should not linearly overwhelm fresh evidence.
        strongest_similarity = float(similar.get(int(row["question_id"]), 0.0))
        item["query_similarity"] = max(float(item["query_similarity"]), strongest_similarity)
        citation_rate = citation_count / question_count if question_count else 0.0
        popularity = min(1.0, math.log1p(question_count) / math.log(11))
        item["history_score"] = round(
            min(1.0, strongest_similarity * (0.65 + 0.20 * citation_rate + 0.15 * popularity)),
            4,
        )
    return priors


def fetch_original_chunks(chunk_ids: list[int] | tuple[int, ...] | set[int]) -> list[dict[str, Any]]:
    ids = list(dict.fromkeys(int(value) for value in chunk_ids or []))
    if not ids:
        return []
    rows: list[sqlite3.Row] = []
    with closing(_connect()) as connection:
        for start in range(0, len(ids), 900):
            batch = ids[start : start + 900]
            placeholders = ",".join("?" for _ in batch)
            rows.extend(
                connection.execute(
                    f"""
                    SELECT id AS chunk_id, document_id, source, page, kind, text
                    FROM chunks WHERE kind='original_text' AND id IN ({placeholders})
                    """,
                    batch,
                ).fetchall()
            )
    return [dict(row) for row in rows]


def record_retrieval_feedback(
    query: str,
    mode: str,
    results: list[dict[str, Any]],
    cited_document_ids: set[str] | list[str] | tuple[str, ...],
) -> None:
    """Persist selected chunk usage and whether the final answer cited it."""
    selected: dict[int, dict[str, Any]] = {}
    for result in results:
        chunk_id = result.get("chunk_id")
        if result.get("kind") == "graph_evidence" or chunk_id is None:
            continue
        selected[int(chunk_id)] = result
    if not selected:
        return
    cited_ids = {str(value) for value in cited_document_ids or []}
    now = datetime.now(timezone.utc).isoformat()
    query_tokens = " ".join(_query_relevance_terms(query))
    with _LOCK, closing(_connect()) as connection, connection:
        cursor = connection.execute(
            "INSERT INTO retrieval_questions(query_text, query_tokens, mode, created_at) VALUES (?, ?, ?, ?)",
            (str(query), query_tokens, str(mode), now),
        )
        question_id = int(cursor.lastrowid)
        connection.execute(
            "INSERT INTO retrieval_questions_fts(question_id, query_text, query_tokens) VALUES (?, ?, ?)",
            (question_id, str(query), query_tokens),
        )
        for chunk_id, result in selected.items():
            document_id = str(result.get("document_id") or "")
            cited = int(document_id in cited_ids)
            connection.execute(
                """
                INSERT INTO retrieval_question_chunks(
                    question_id, chunk_id, document_id, relevance, cited
                ) VALUES (?, ?, ?, ?, ?)
                """,
                (
                    question_id,
                    chunk_id,
                    document_id,
                    float(result.get("relevance", 0.0)),
                    cited,
                ),
            )
            connection.execute(
                """
                INSERT INTO retrieval_chunk_stats(
                    chunk_id, document_id, question_count, citation_count, last_used_at
                ) VALUES (?, ?, 1, ?, ?)
                ON CONFLICT(chunk_id) DO UPDATE SET
                    document_id=excluded.document_id,
                    question_count=question_count + 1,
                    citation_count=citation_count + excluded.citation_count,
                    last_used_at=excluded.last_used_at
                """,
                (chunk_id, document_id, cited, now),
            )


def chunk_history_stats(
    chunk_ids: list[int] | tuple[int, ...] | set[int],
) -> dict[int, dict[str, float | int]]:
    ids = list(dict.fromkeys(int(value) for value in chunk_ids or []))
    if not ids:
        return {}
    output: dict[int, dict[str, float | int]] = {}
    with closing(_connect()) as connection:
        for start in range(0, len(ids), 900):
            batch = ids[start : start + 900]
            placeholders = ",".join("?" for _ in batch)
            rows = connection.execute(
                f"""
                SELECT chunk_id, question_count, citation_count
                FROM retrieval_chunk_stats WHERE chunk_id IN ({placeholders})
                """,
                batch,
            ).fetchall()
            for row in rows:
                question_count = int(row["question_count"] or 0)
                citation_count = int(row["citation_count"] or 0)
                output[int(row["chunk_id"])] = {
                    "question_count": question_count,
                    "citation_count": citation_count,
                    "citation_rate": round(citation_count / question_count, 4) if question_count else 0.0,
                }
    return output


def retrieval_question_count() -> int:
    """Return the denominator used for historical chunk question-use rates."""
    with closing(_connect()) as connection:
        return int(connection.execute("SELECT COUNT(*) FROM retrieval_questions").fetchone()[0])


def corpus_stats() -> dict[str, int]:
    with _connect() as connection:
        return {
            "documents": connection.execute("SELECT COUNT(*) FROM documents").fetchone()[0],
            "chunks": connection.execute("SELECT COUNT(*) FROM chunks").fetchone()[0],
            "duplicates": connection.execute("SELECT COUNT(*) FROM duplicates").fetchone()[0],
            "failures": connection.execute("SELECT COUNT(*) FROM failures").fetchone()[0],
            "structured": connection.execute("SELECT COUNT(*) FROM documents WHERE structured=1").fetchone()[0],
        }


def export_reports() -> dict[str, Any]:
    """Export portable corpus, duplicate, failure, and API sizing reports."""
    with _connect() as connection:
        documents = [dict(row) for row in connection.execute("SELECT * FROM documents ORDER BY name")]
        duplicates = [dict(row) for row in connection.execute("SELECT * FROM duplicates ORDER BY source_path")]
        failures = [dict(row) for row in connection.execute("SELECT * FROM failures ORDER BY source_path")]
    total_characters = 0
    for document in documents:
        path = BASE_DIR / document["markdown_path"]
        if path.exists():
            total_characters += len(path.read_text(encoding="utf-8"))
    summary: dict[str, Any] = {
        **corpus_stats(),
        "markdown_characters": total_characters,
        "estimated_input_tokens": math.ceil(total_characters / 3.5),
        "estimate_note": "Token estimate uses characters / 3.5; actual billing depends on tokenizer and prompt overhead.",
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    (REPORTS_DIR / "corpus_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (REPORTS_DIR / "documents.json").write_text(
        json.dumps(documents, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    for filename, rows, fields in (
        ("duplicates.csv", duplicates, ["source_path", "canonical_document_id", "reason", "detected_at"]),
        ("failures.csv", failures, ["source_path", "error", "detected_at"]),
    ):
        with (REPORTS_DIR / filename).open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
    return summary
