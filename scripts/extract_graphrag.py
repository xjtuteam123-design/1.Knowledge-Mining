"""Extract an evidence-grounded GraphRAG pilot corpus with DeepSeek."""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
import threading
import time
from contextlib import closing
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from graph_prompts import GRAPH_CONSOLIDATION_PROMPT, GRAPH_EXTRACTION_PROMPT  # noqa: E402
from graph_store import (  # noqa: E402
    GRAPH_FAILED_DIR,
    GRAPH_PAPERS_DIR,
    GRAPH_RAW_DIR,
    graph_stats,
    record_graph_failure,
    replace_paper_graph,
)
from rag_store import _connect  # noqa: E402


PRINT_LOCK = threading.Lock()
WRITE_LOCK = threading.Lock()
STOP_EVENT = threading.Event()
USAGE_LOG = ROOT / "reports" / "graph_api_usage.jsonl"
SELECTION_REPORT = ROOT / "reports" / "graph_selection.json"
RUN_ID = ""
RUN_USAGE = {
    "requests": 0,
    "successful_requests": 0,
    "invalid_json_requests": 0,
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0,
}


def _is_connectivity_error(exc: Exception) -> bool:
    """Return True for transport failures that should pause, not fail, a batch."""
    name = type(exc).__name__.casefold()
    message = str(exc).casefold()
    status = getattr(exc, "status_code", None)
    return (
        status in {408, 409, 429, 500, 502, 503, 504}
        or name in {"apiconnectionerror", "apitimeouterror", "connecterror", "readtimeout"}
        or "connection error" in message
        or "timed out" in message
        or "timeout" in message
        or "service is too busy" in message
        or "service_unavailable" in message
        or "batch stopped after a fatal api" in message
    )

TOP_LEVEL_LISTS = (
    "alloy_systems",
    "samples",
    "process_steps",
    "phases_and_microstructures",
    "property_observations",
    "mechanisms",
    "machine_learning_models",
    "relations",
    "unresolved_terms",
    "conflicts",
)

THEME_KEYWORDS = {
    "Nb-W/Nb-based": ("nb-w", "nb–w", "niobium alloy", "nb alloy", "nb-1zr", "nb1zr"),
    "Mo-based": ("molybdenum alloy", "mo alloy", "tzm", "molybdenum-based"),
    "W-based": ("tungsten alloy", "w alloy", "tungsten-based", "w-based"),
    "RHEA/MPEA": ("refractory high entropy", "refractory high-entropy", "rhea", "multi-principal"),
    "ODS/dispersion": ("oxide dispersion", "ods alloy", "y2o3", "la2o3", "zro2", "hfo2"),
    "Additive manufacturing": ("additive manufacturing", "laser powder bed", "lpbf", "selective laser", "directed energy", "electron beam melting"),
    "Oxidation": ("oxidation resistance", "oxidation behavior", "oxide scale", "mass gain", "weight gain"),
    "Carbide/boride/silicide": ("carbide", "boride", "silicide", "zrc", "hfc", "tic", "nbc", "tac"),
}


def emit(payload: dict) -> None:
    with PRINT_LOCK:
        print(json.dumps(payload, ensure_ascii=False), flush=True)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(path)


def _usage(response) -> dict[str, int]:
    usage = getattr(response, "usage", None)
    return {
        "prompt_tokens": int(getattr(usage, "prompt_tokens", 0) or 0),
        "completion_tokens": int(getattr(usage, "completion_tokens", 0) or 0),
        "total_tokens": int(getattr(usage, "total_tokens", 0) or 0),
    }


def _record_usage(payload: dict) -> None:
    USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
    with WRITE_LOCK, USAGE_LOG.open("a", encoding="utf-8") as handle:
        record = {"run_id": RUN_ID, **payload}
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        RUN_USAGE["requests"] += 1
        if payload.get("status") == "success":
            RUN_USAGE["successful_requests"] += 1
        elif payload.get("status") == "invalid_json":
            RUN_USAGE["invalid_json_requests"] += 1
        for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
            RUN_USAGE[key] += int(payload.get(key) or 0)


def _page_range(text: str) -> str | None:
    pages = [int(value) for value in re.findall(r"(?im)^##\s+Page\s+(\d+)\s*$", text)]
    if not pages:
        return None
    return str(pages[0]) if pages[0] == pages[-1] else f"{pages[0]}-{pages[-1]}"


def split_markdown(markdown: str, max_chars: int) -> list[str]:
    """Split at page/paragraph boundaries without dropping source text."""
    if len(markdown) <= max_chars:
        return [markdown]
    blocks = re.split(r"(?=^##\s+Page\s+\d+\s*$)", markdown, flags=re.MULTILINE)
    if len(blocks) <= 2:
        blocks = markdown.split("\n\n")
    parts: list[str] = []
    current: list[str] = []
    length = 0
    for block in blocks:
        if not block.strip():
            continue
        if current and length + len(block) > max_chars:
            parts.append("".join(current).strip())
            current = []
            length = 0
        if len(block) > max_chars:
            paragraphs = block.split("\n\n")
            for paragraph in paragraphs:
                addition = paragraph + "\n\n"
                if current and length + len(addition) > max_chars:
                    parts.append("".join(current).strip())
                    current = []
                    length = 0
                if len(addition) > max_chars:
                    for start in range(0, len(addition), max_chars):
                        segment = addition[start : start + max_chars].strip()
                        if segment:
                            parts.append(segment)
                else:
                    current.append(addition)
                    length += len(addition)
        else:
            current.append(block)
            length += len(block)
    if current:
        parts.append("".join(current).strip())
    return [part for part in parts if part]


def _extract_json(text: str) -> dict:
    content = (text or "").strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json)?\s*", "", content, flags=re.IGNORECASE)
        content = re.sub(r"\s*```$", "", content)
    try:
        value = json.loads(content)
    except json.JSONDecodeError:
        start = content.find("{")
        end = content.rfind("}")
        if start < 0 or end <= start:
            raise ValueError("Model response contains no JSON object")
        value = json.loads(content[start : end + 1])
    if not isinstance(value, dict):
        raise ValueError("Graph extraction response is not a JSON object")
    return value


def normalize_payload(payload: dict, document_id: str, chunk_id: str) -> dict:
    payload["document_id"] = document_id
    payload["chunk_id"] = chunk_id
    if not isinstance(payload.get("paper_metadata"), dict):
        payload["paper_metadata"] = {}
    for key in TOP_LEVEL_LISTS:
        if not isinstance(payload.get(key), list):
            payload[key] = []
    # Carry chunk identity down to evidence so it survives paper consolidation.
    for collection_name in (
        "alloy_systems",
        "samples",
        "process_steps",
        "phases_and_microstructures",
        "property_observations",
        "mechanisms",
        "machine_learning_models",
        "relations",
    ):
        for item in payload[collection_name]:
            if not isinstance(item, dict):
                continue
            evidences = item.get("evidence")
            if isinstance(evidences, list):
                for evidence in evidences:
                    if isinstance(evidence, dict):
                        evidence.setdefault("chunk_id", chunk_id)
            if collection_name == "samples":
                for composition in item.get("composition", []) if isinstance(item.get("composition"), list) else []:
                    if not isinstance(composition, dict):
                        continue
                    for evidence in composition.get("evidence", []) if isinstance(composition.get("evidence"), list) else []:
                        if isinstance(evidence, dict):
                            evidence.setdefault("chunk_id", chunk_id)
    return payload


def document_type(document: dict) -> str:
    """Classify known source folders without asking the model to guess."""
    source_path = str(document.get("source_path") or "").replace("\\", "/").casefold()
    return "patent" if "/patent database/" in f"/{source_path.strip('/')}" else "literature"


def _request_json(
    client: OpenAI,
    config: dict,
    system_prompt: str,
    user_content: str,
    *,
    document: dict,
    stage: str,
    part: int,
) -> tuple[dict, dict[str, int]]:
    last_error: Exception | None = None
    use_json_mode = True
    for attempt in range(1, 5):
        try:
            kwargs = {
                "model": config["model"],
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content},
                ],
                "max_tokens": int(config.get("graph_ingestion_max_tokens", 16000)),
                "extra_body": {"thinking": {"type": "disabled"}},
                "timeout": int(config.get("api_timeout_seconds", 900)),
            }
            if use_json_mode:
                kwargs["response_format"] = {"type": "json_object"}
            response = client.chat.completions.create(**kwargs)
            content = response.choices[0].message.content or ""
            used = _usage(response)
            usage_record = {
                "timestamp": _now(),
                "document_id": document["id"],
                "name": document["name"],
                "stage": stage,
                "part": part,
                "attempt": attempt,
                "model": config["model"],
                **used,
            }
            try:
                payload = _extract_json(content)
            except Exception as parse_error:
                _record_usage({**usage_record, "status": "invalid_json", "parse_error": str(parse_error)[:500]})
                raise
            _record_usage({**usage_record, "status": "success"})
            return payload, used
        except Exception as exc:
            last_error = exc
            status = getattr(exc, "status_code", None)
            message = str(exc).lower()
            if status == 400 and use_json_mode and ("response_format" in message or "json" in message):
                use_json_mode = False
                continue
            if status in {401, 402, 403}:
                STOP_EVENT.set()
                raise
            if status in {400, 404} and "response_format" not in message:
                raise
            if attempt == 4:
                if _is_connectivity_error(exc):
                    STOP_EVENT.set()
                raise
            delay = min(30, 2 ** (attempt - 1) + random.random())
            emit(
                {
                    "event": "retry",
                    "name": document["name"],
                    "stage": stage,
                    "part": part,
                    "attempt": attempt,
                    "delay_seconds": round(delay, 1),
                    "error": str(exc),
                }
            )
            time.sleep(delay)
    raise last_error or RuntimeError("Graph extraction request failed")


def _prefix_ids(payload: dict, prefix: str) -> dict:
    """Make IDs unique for a deterministic multi-segment fallback merge."""
    mapping: dict[str, str] = {}
    for collection in (
        "alloy_systems",
        "samples",
        "process_steps",
        "phases_and_microstructures",
        "property_observations",
        "mechanisms",
        "machine_learning_models",
    ):
        for item in payload.get(collection, []):
            if isinstance(item, dict) and item.get("id"):
                old = str(item["id"])
                mapping[old] = f"{prefix}_{old}"
                item["id"] = mapping[old]
    reference_fields = (
        "alloy_system_id", "sample_id", "comparison_sample_id",
        "property_observation_id", "source_id", "target_id",
    )
    for collection in (
        "samples",
        "process_steps",
        "phases_and_microstructures",
        "property_observations",
        "mechanisms",
        "machine_learning_models",
        "relations",
    ):
        for item in payload.get(collection, []):
            if not isinstance(item, dict):
                continue
            if collection == "relations" and item.get("id"):
                item["id"] = f"{prefix}_{item['id']}"
            for field in reference_fields:
                if item.get(field) is not None:
                    item[field] = mapping.get(str(item[field]), f"{prefix}_{item[field]}")
    return payload


def deterministic_merge(payloads: list[dict], document_id: str) -> dict:
    output = {
        "document_id": document_id,
        "chunk_id": "paper",
        "paper_metadata": {},
        **{key: [] for key in TOP_LEVEL_LISTS},
    }
    for index, original in enumerate(payloads, 1):
        payload = _prefix_ids(json.loads(json.dumps(original)), f"part{index}")
        for key, value in payload.get("paper_metadata", {}).items():
            if output["paper_metadata"].get(key) in (None, "", []):
                output["paper_metadata"][key] = value
        for key in TOP_LEVEL_LISTS:
            output[key].extend(payload.get(key, []))
    output["conflicts"].append(
        {
            "type": "merge_fallback",
            "message": "Segment graphs were combined deterministically; aliases may remain duplicated.",
        }
    )
    return output


def consolidate_payloads(
    client: OpenAI,
    config: dict,
    document: dict,
    payloads: list[dict],
) -> tuple[dict, dict[str, int]]:
    if len(payloads) == 1:
        return payloads[0], {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    compact = json.dumps(payloads, ensure_ascii=False, separators=(",", ":"))
    user_content = (
        f"Document ID: {document['id']}\nPaper file: {document['name']}\n"
        "Merge these segment graph objects without adding knowledge:\n" + compact
    )
    try:
        payload, used = _request_json(
            client,
            config,
            GRAPH_CONSOLIDATION_PROMPT,
            user_content,
            document=document,
            stage="consolidate",
            part=0,
        )
        return normalize_payload(payload, document["id"], "paper"), used
    except Exception as exc:
        emit({"event": "consolidation_fallback", "name": document["name"], "error": str(exc)})
        return deterministic_merge(payloads, document["id"]), {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
        }


def classify_themes(text: str) -> tuple[list[str], dict[str, int]]:
    lowered = text.lower().replace("–", "-").replace("—", "-")
    scores: dict[str, int] = {}
    for theme, keywords in THEME_KEYWORDS.items():
        score = sum(min(lowered.count(keyword.replace("–", "-")), 20) for keyword in keywords)
        if score:
            scores[theme] = score
    return list(scores), scores


def select_documents(
    limit: int,
    selection: str,
    force: bool,
    include_ids: list[str] | None = None,
    skip_failed: bool = False,
    include_long_documents: bool = False,
) -> list[dict]:
    with closing(_connect()) as connection, connection:
        condition = "WHERE structured=1" if selection == "old-structured" else ""
        rows = [dict(row) for row in connection.execute(f"SELECT * FROM documents {condition} ORDER BY created_at").fetchall()]
    if include_ids is not None:
        rows_by_id = {row["id"]: row for row in rows}
        missing = [document_id for document_id in include_ids if document_id not in rows_by_id]
        if missing:
            raise ValueError(
                "Source graph references documents that are absent from literature.db: "
                + ", ".join(missing)
            )
        rows = [rows_by_id[document_id] for document_id in include_ids]
    excluded: set[str] = set()
    graph_db = ROOT / "data" / "graph" / "graph.db"
    if graph_db.exists() and not force:
        import sqlite3

        with sqlite3.connect(graph_db) as connection:
            try:
                statuses = ("complete", "failed") if skip_failed else ("complete",)
                placeholders = ",".join("?" for _ in statuses)
                excluded = {
                    row[0]
                    for row in connection.execute(
                        f"SELECT document_id FROM graph_papers WHERE status IN ({placeholders})",
                        statuses,
                    )
                }
            except sqlite3.OperationalError:
                excluded = set()
    candidates: list[dict] = []
    for row in rows:
        if row["id"] in excluded:
            continue
        # A pilot should represent ordinary papers rather than a book/thesis
        # that would dominate both API cost and graph size.
        if not include_long_documents and int(row.get("pages") or 0) > 50:
            continue
        markdown_path = ROOT / row["markdown_path"]
        if not markdown_path.exists():
            continue
        text = markdown_path.read_text(encoding="utf-8", errors="replace")
        themes, scores = classify_themes(text)
        row["document_type"] = document_type(row)
        row["themes"] = themes or ["Other refractory alloy"]
        row["theme_scores"] = scores
        row["characters"] = len(text)
        candidates.append(row)

    if include_ids is not None:
        return candidates[:limit]

    selected: list[dict] = []
    selected_ids: set[str] = set()
    buckets: dict[str, list[dict]] = {}
    for theme in THEME_KEYWORDS:
        buckets[theme] = sorted(
            [row for row in candidates if theme in row["themes"]],
            key=lambda row: (-row["theme_scores"].get(theme, 0), row["name"]),
        )
    while len(selected) < limit:
        changed = False
        for theme in THEME_KEYWORDS:
            bucket = buckets[theme]
            while bucket and bucket[0]["id"] in selected_ids:
                bucket.pop(0)
            if bucket and len(selected) < limit:
                row = bucket.pop(0)
                selected.append(row)
                selected_ids.add(row["id"])
                changed = True
        if not changed:
            break
    if len(selected) < limit:
        remaining = sorted(
            [row for row in candidates if row["id"] not in selected_ids],
            key=lambda row: (-len(row["themes"]), -row["pages"], row["name"]),
        )
        selected.extend(remaining[: limit - len(selected)])
    return selected[:limit]


def analyze_document(client: OpenAI, config: dict, document: dict, max_input_chars: int) -> dict:
    if STOP_EVENT.is_set():
        raise RuntimeError("Batch stopped after a fatal API authorization or balance error")
    markdown = (ROOT / document["markdown_path"]).read_text(encoding="utf-8", errors="replace")
    parts = split_markdown(markdown, max_input_chars)
    payloads: list[dict] = []
    totals = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    safe_id = re.sub(r"[^a-zA-Z0-9_-]+", "_", document["id"])
    for index, part_text in enumerate(parts, 1):
        if STOP_EVENT.is_set():
            raise RuntimeError("Batch stopped after a fatal API authorization or balance error")
        chunk_id = f"{document['id']}:part:{index:03d}"
        metadata = {
            "document_id": document["id"],
            "paper_file_name": document["name"],
            "document_type": document_type(document),
            "chunk_id": chunk_id,
            "segment": f"{index}/{len(parts)}",
            "page_range": _page_range(part_text),
        }
        user_content = (
            "INPUT METADATA\n"
            + json.dumps(metadata, ensure_ascii=False, indent=2)
            + "\n\nSOURCE TEXT\n"
            + part_text
        )
        payload, used = _request_json(
            client,
            config,
            GRAPH_EXTRACTION_PROMPT,
            user_content,
            document=document,
            stage="extract",
            part=index,
        )
        payload = normalize_payload(payload, document["id"], chunk_id)
        payload["paper_metadata"]["document_type"] = document_type(document)
        payloads.append(payload)
        for key in totals:
            totals[key] += used[key]
        _write_json(GRAPH_RAW_DIR / f"{safe_id}.part{index:03d}.json", payload)

    paper_payload, consolidation_usage = consolidate_payloads(client, config, document, payloads)
    for key in totals:
        totals[key] += consolidation_usage[key]
    paper_payload = normalize_payload(paper_payload, document["id"], "paper")
    paper_payload["paper_metadata"]["document_type"] = document_type(document)
    document["document_type"] = document_type(document)
    graph_path = GRAPH_PAPERS_DIR / f"{safe_id}.json"
    _write_json(graph_path, paper_payload)
    counts = replace_paper_graph(
        document,
        paper_payload,
        str(graph_path.relative_to(ROOT)),
        len(parts),
        totals,
        document.get("themes", []),
    )
    return {"parts": len(parts), **counts, **totals}


def main() -> int:
    global RUN_ID
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
        sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    RUN_ID = datetime.now(timezone.utc).strftime("graphrag-%Y%m%dT%H%M%SZ")
    for key in RUN_USAGE:
        RUN_USAGE[key] = 0
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=50)
    parser.add_argument(
        "--target-total",
        type=int,
        default=0,
        help="Extract only enough pending papers to reach this total completed graph-paper count",
    )
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--max-input-chars", type=int, default=90_000)
    parser.add_argument("--model", help="Temporarily override the configured model for this run")
    parser.add_argument("--selection", choices=("old-structured", "all"), default="old-structured")
    parser.add_argument("--force", action="store_true", help="Re-extract papers already in the graph database")
    parser.add_argument(
        "--include-long-documents",
        action="store_true",
        help="Include documents over 50 pages (needed for a complete-corpus run)",
    )
    parser.add_argument(
        "--skip-failed",
        action="store_true",
        help="Skip both completed and previously failed papers; process only documents not yet attempted",
    )
    parser.add_argument(
        "--source-graph-db",
        type=Path,
        help="Re-extract the exact set of papers marked complete in another graph.db",
    )
    parser.add_argument(
        "--include-id",
        action="append",
        default=[],
        help="Extract a specific document ID; repeat this option to supply multiple IDs",
    )
    parser.add_argument(
        "--include-file",
        type=Path,
        help="UTF-8 text file containing one document ID per line",
    )
    parser.add_argument("--dry-run", action="store_true", help="Select and report papers without calling the API")
    args = parser.parse_args()

    config = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
    if args.model:
        config["model"] = args.model
    source_document_ids: list[str] | None = None
    if args.include_id or args.include_file:
        source_document_ids = [str(value).strip() for value in args.include_id if str(value).strip()]
        if args.include_file:
            include_file = args.include_file if args.include_file.is_absolute() else ROOT / args.include_file
            source_document_ids.extend(
                line.strip()
                for line in include_file.read_text(encoding="utf-8").splitlines()
                if line.strip() and not line.lstrip().startswith("#")
            )
        source_document_ids = list(dict.fromkeys(source_document_ids))
    if args.source_graph_db:
        if source_document_ids:
            raise ValueError("Use either --source-graph-db or --include-id/--include-file, not both")
        import sqlite3

        source_graph_db = args.source_graph_db
        if not source_graph_db.is_absolute():
            source_graph_db = ROOT / source_graph_db
        if not source_graph_db.exists():
            raise FileNotFoundError(f"Source graph database does not exist: {source_graph_db}")
        with sqlite3.connect(source_graph_db) as connection:
            source_document_ids = [
                row[0]
                for row in connection.execute(
                    "SELECT document_id FROM graph_papers WHERE status='complete' ORDER BY document_id"
                )
            ]
        if not source_document_ids:
            raise ValueError(f"No completed papers found in source graph database: {source_graph_db}")

    requested_limit = len(source_document_ids) if source_document_ids is not None else max(1, args.limit)
    if args.target_total and source_document_ids is None:
        requested_limit = max(0, args.target_total - graph_stats()["papers"])
    documents = (
        select_documents(
            requested_limit,
            args.selection,
            args.force,
            include_ids=source_document_ids,
            skip_failed=args.skip_failed,
            include_long_documents=args.include_long_documents,
        )
        if requested_limit
        else []
    )
    report = {
        "generated_at": _now(),
        "selection": args.selection,
        "model": config["model"],
        "skip_failed": args.skip_failed,
        "limit": requested_limit,
        "target_total": args.target_total or None,
        "source_graph_db": str(args.source_graph_db) if args.source_graph_db else None,
        "documents": [
            {
                "document_id": row["id"],
                "name": row["name"],
                "document_type": row["document_type"],
                "pages": row["pages"],
                "characters": row["characters"],
                "themes": row["themes"],
            }
            for row in documents
        ],
    }
    _write_json(SELECTION_REPORT, report)
    emit({"event": "selection", "run_id": RUN_ID, "papers": len(documents), "report": str(SELECTION_REPORT)})
    if args.dry_run:
        return 0
    if not documents:
        emit({"event": "complete", "succeeded": 0, "failed": 0, "message": "No pending papers"})
        return 0

    client = OpenAI(api_key=config["api_key"], base_url=config["base_url"])
    succeeded = failed = deferred = completed = 0
    totals = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    iterator = iter(documents)
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {}
        for document in iterator:
            futures[executor.submit(analyze_document, client, config, document, args.max_input_chars)] = document
            if len(futures) >= max(1, args.workers):
                break
        while futures:
            done, _ = wait(futures, return_when=FIRST_COMPLETED)
            for future in done:
                document = futures.pop(future)
                completed += 1
                try:
                    result = future.result()
                    succeeded += 1
                    for key in totals:
                        totals[key] += result[key]
                    emit(
                        {
                            "event": "paper",
                            "completed": completed,
                            "total": len(documents),
                            "status": "complete",
                            "name": document["name"],
                            **result,
                        }
                    )
                except Exception as exc:
                    if STOP_EVENT.is_set() and _is_connectivity_error(exc):
                        deferred += 1
                        emit(
                            {
                                "event": "paper",
                                "completed": completed,
                                "total": len(documents),
                                "status": "deferred_network",
                                "name": document["name"],
                                "error": str(exc),
                            }
                        )
                    else:
                        failed += 1
                        record_graph_failure(document, str(exc), document.get("themes", []))
                        failure_path = GRAPH_FAILED_DIR / f"{document['id']}.json"
                        _write_json(
                            failure_path,
                            {"timestamp": _now(), "document": document["name"], "error": str(exc)},
                        )
                        emit(
                            {
                                "event": "paper",
                                "completed": completed,
                                "total": len(documents),
                                "status": "failed",
                                "name": document["name"],
                                "error": str(exc),
                            }
                        )
                if not STOP_EVENT.is_set():
                    try:
                        next_document = next(iterator)
                    except StopIteration:
                        pass
                    else:
                        futures[executor.submit(analyze_document, client, config, next_document, args.max_input_chars)] = next_document

    summary = {
        "event": "complete",
        "run_id": RUN_ID,
        "succeeded": succeeded,
        "failed": failed,
        "deferred_network": deferred,
        **totals,
        "logged_usage_including_retries": dict(RUN_USAGE),
        "graph": graph_stats(),
    }
    emit(summary)
    _write_json(ROOT / "reports" / "graph_run_status.json", {"generated_at": _now(), **summary})
    if deferred:
        return 3
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
