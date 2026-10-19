"""Print deduplicated full-corpus and active GraphRAG progress."""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import time
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LIST_PATH = ROOT / "reports" / "graph_next_2000_ids.txt"
SELECTION_PATH = ROOT / "reports" / "graph_selection.json"
GRAPH_DB = ROOT / "data" / "graph" / "graph.db"
LITERATURE_DB = ROOT / "data" / "index" / "literature.db"
SUCCESS_TARGET = 5169


def _list_ids(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def _selection_ids() -> list[str]:
    if not SELECTION_PATH.exists():
        return []
    try:
        report = json.loads(SELECTION_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    return [
        str(document.get("document_id"))
        for document in report.get("documents", [])
        if isinstance(document, dict) and document.get("document_id")
    ]


def _counts(ids: list[str], statuses: dict[str, str]) -> tuple[int, int, int]:
    complete = sum(statuses.get(document_id) == "complete" for document_id in ids)
    failed = sum(statuses.get(document_id) == "failed" for document_id in ids)
    not_started = sum(document_id not in statuses for document_id in ids)
    return complete, failed, not_started


def progress_lines() -> list[str]:
    with sqlite3.connect(LITERATURE_DB) as connection:
        full_ids = [str(row[0]) for row in connection.execute("SELECT id FROM documents")]
        duplicates = int(connection.execute("SELECT COUNT(*) FROM duplicates").fetchone()[0])
    with sqlite3.connect(GRAPH_DB) as connection:
        statuses = {
            str(document_id): str(status)
            for document_id, status in connection.execute(
                "SELECT document_id, status FROM graph_papers"
            )
        }
        patent_complete = connection.execute(
            """
            SELECT COUNT(*) FROM graph_papers
            WHERE document_type='patent' AND status='complete'
            """
        ).fetchone()[0]

    full_complete, full_failed, full_not_started = _counts(full_ids, statuses)
    active_ids = _selection_ids()
    active_complete, active_failed, active_not_started = _counts(active_ids, statuses)
    batch_ids = _list_ids(LIST_PATH)
    batch_complete, batch_failed, batch_not_started = _counts(batch_ids, statuses)

    lines = [
        f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "Full corpus (deduplicated)",
        f"Unique documents: {len(full_ids)}",
        f"Requested success target: {SUCCESS_TARGET}",
        f"Completed: {full_complete}",
        f"Failed (retryable): {full_failed}",
        f"Not started: {full_not_started}",
        f"Remaining until requested target: {max(0, SUCCESS_TARGET - full_complete)}",
        f"Documents outside requested target: {max(0, len(full_ids) - SUCCESS_TARGET)}",
        f"Duplicate source records excluded: {duplicates}",
        f"Patents completed: {patent_complete}/9",
    ]
    if active_ids:
        lines.extend(
            [
                "",
                "Active full-corpus queue",
                f"Selected: {len(active_ids)}",
                f"Completed: {active_complete}",
                f"Failed (retryable): {active_failed}",
                f"Not started: {active_not_started}",
            ]
        )
    if batch_ids:
        lines.extend(
            [
                "",
                "Original 2000-document batch",
                f"Completed: {batch_complete}/{len(batch_ids)}",
                f"Failed (retryable): {batch_failed}",
                f"Not started: {batch_not_started}",
            ]
        )
    return lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch", action="store_true", help="Refresh progress continuously.")
    parser.add_argument("--interval", type=float, default=5.0)
    args = parser.parse_args()
    while True:
        if args.watch:
            os.system("cls" if os.name == "nt" else "clear")
        print("\n".join(progress_lines()), flush=True)
        if not args.watch:
            return
        print("\nRefreshing automatically. Press Ctrl+C to stop watching.", flush=True)
        try:
            time.sleep(max(1.0, args.interval))
        except KeyboardInterrupt:
            return


if __name__ == "__main__":
    main()
