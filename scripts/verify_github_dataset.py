"""Verify the curated Markdown and GraphRAG data prepared for GitHub."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LITERATURE_DIR = ROOT / "data" / "markdown_bundle" / "literature_5159"
PATENT_DIR = ROOT / "data" / "markdown_bundle" / "patents_10"
CHUNK_DIR = ROOT / "data" / "graph" / "chunk_extractions"
PAPER_GRAPH_DIR = ROOT / "data" / "graph" / "paper_graphs"

EXPECTED_LITERATURE = 5159
EXPECTED_PATENTS = 10
EXPECTED_CHUNKS = 9482
EXPECTED_PAPER_GRAPHS = 5169
CN_PATENT_ID = "c0cdd8774ea209c9"


def files(directory: Path, suffix: str) -> list[Path]:
    if not directory.is_dir():
        raise FileNotFoundError(f"Missing dataset directory: {directory}")
    return sorted(path for path in directory.iterdir() if path.is_file() and path.suffix == suffix)


def document_id(path: Path) -> str:
    value = path.name.split("-", 1)[0] if path.suffix == ".md" else path.stem
    if len(value) != 16:
        raise ValueError(f"Invalid document ID in filename: {path.name}")
    return value


def main() -> int:
    literature = files(LITERATURE_DIR, ".md")
    patents = files(PATENT_DIR, ".md")
    chunks = files(CHUNK_DIR, ".json")
    paper_graphs = files(PAPER_GRAPH_DIR, ".json")

    checks = {
        "literature_markdown": (len(literature), EXPECTED_LITERATURE),
        "patent_markdown": (len(patents), EXPECTED_PATENTS),
        "total_markdown": (len(literature) + len(patents), EXPECTED_PAPER_GRAPHS),
        "chunk_extractions": (len(chunks), EXPECTED_CHUNKS),
        "paper_graphs": (len(paper_graphs), EXPECTED_PAPER_GRAPHS),
    }

    failed = False
    for label, (actual, expected) in checks.items():
        ok = actual == expected
        failed |= not ok
        print(f"[{'OK' if ok else 'FAIL'}] {label}: {actual} (expected {expected})")

    markdown_ids = {document_id(path) for path in literature + patents}
    graph_ids = {document_id(path) for path in paper_graphs}
    id_match = markdown_ids == graph_ids and len(markdown_ids) == EXPECTED_PAPER_GRAPHS
    failed |= not id_match
    print(f"[{'OK' if id_match else 'FAIL'}] markdown/paper graph document IDs match")
    if not id_match:
        print(f"  missing graphs: {len(markdown_ids - graph_ids)}")
        print(f"  extra graphs: {len(graph_ids - markdown_ids)}")

    chunk_ids = {path.name.split(".", 1)[0] for path in chunks}
    chunks_belong_to_corpus = chunk_ids <= markdown_ids
    failed |= not chunks_belong_to_corpus
    print(
        f"[{'OK' if chunks_belong_to_corpus else 'FAIL'}] "
        "all chunk extractions belong to published documents"
    )
    if not chunks_belong_to_corpus:
        print(f"  extra chunk document IDs: {len(chunk_ids - markdown_ids)}")

    patent_ids = {document_id(path) for path in patents}
    cn_patent_ok = CN_PATENT_ID in patent_ids
    failed |= not cn_patent_ok
    print(f"[{'OK' if cn_patent_ok else 'FAIL'}] CN102719713A is classified as a patent")

    if failed:
        print("Dataset verification failed.", file=sys.stderr)
        return 1
    print("Dataset verification passed: 5159 literature + 10 patents = 5169 documents.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
