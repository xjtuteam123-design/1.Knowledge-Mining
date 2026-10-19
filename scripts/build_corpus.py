"""Build a resumable local Markdown corpus and SQLite FTS index."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rag_store import corpus_stats, export_reports, ingest_path  # noqa: E402


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Directory containing PDF/TXT/Markdown literature")
    parser.add_argument("--chunk-size", type=int, default=900)
    parser.add_argument("--overlap", type=int, default=150)
    parser.add_argument("--limit", type=int, default=0, help="Process only N files; 0 means all")
    args = parser.parse_args()

    files = sorted(
        path for path in args.source.rglob("*")
        if path.is_file() and path.suffix.lower() in {".pdf", ".txt", ".md"}
    )
    if args.limit:
        files = files[: args.limit]
    print(json.dumps({"event": "start", "files": len(files), "source": str(args.source)}, ensure_ascii=False), flush=True)
    for number, path in enumerate(files, 1):
        result = ingest_path(path, args.chunk_size, args.overlap)
        result.update({"event": "file", "number": number, "total": len(files)})
        print(json.dumps(result, ensure_ascii=False), flush=True)
    print(json.dumps({"event": "complete", **export_reports()}, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
