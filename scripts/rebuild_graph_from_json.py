"""Rebuild the SQLite knowledge graph from saved paper JSON without API calls."""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import graph_store  # noqa: E402
from rag_store import _connect as connect_literature  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--graph-db",
        type=Path,
        default=graph_store.GRAPH_DB_PATH,
        help="Graph database whose completed rows and saved JSON files should be rebuilt",
    )
    args = parser.parse_args()
    graph_db = args.graph_db if args.graph_db.is_absolute() else ROOT / args.graph_db
    if not graph_db.exists():
        raise FileNotFoundError(graph_db)
    if graph_db.resolve() != graph_store.GRAPH_DB_PATH.resolve():
        raise ValueError("This command currently rebuilds only the active data/graph/graph.db")

    with sqlite3.connect(graph_db) as connection:
        connection.row_factory = sqlite3.Row
        graph_rows = [
            dict(row)
            for row in connection.execute(
                "SELECT * FROM graph_papers WHERE status='complete' ORDER BY document_id"
            )
        ]
    with connect_literature() as connection:
        documents = {
            row["id"]: dict(row)
            for row in connection.execute("SELECT * FROM documents").fetchall()
        }

    rebuilt = 0
    for row in graph_rows:
        document = documents.get(row["document_id"])
        if not document:
            raise KeyError(f"Document is absent from literature.db: {row['document_id']}")
        graph_path = Path(str(row.get("graph_path") or ""))
        if not graph_path.is_absolute():
            graph_path = ROOT / graph_path
        if not graph_path.exists():
            graph_path = graph_store.GRAPH_PAPERS_DIR / f"{row['document_id']}.json"
        payload = json.loads(graph_path.read_text(encoding="utf-8"))
        usage = {
            "prompt_tokens": int(row.get("prompt_tokens") or 0),
            "completion_tokens": int(row.get("completion_tokens") or 0),
        }
        themes = json.loads(row.get("themes") or "[]")
        counts = graph_store.replace_paper_graph(
            document,
            payload,
            str(graph_path.relative_to(ROOT)),
            int(row.get("source_chunks") or 0),
            usage,
            themes,
        )
        rebuilt += 1
        print(
            json.dumps(
                {"event": "rebuilt", "index": rebuilt, "name": document["name"], **counts},
                ensure_ascii=False,
            ),
            flush=True,
        )

    print(json.dumps({"event": "complete", "papers": rebuilt, **graph_store.graph_stats()}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
