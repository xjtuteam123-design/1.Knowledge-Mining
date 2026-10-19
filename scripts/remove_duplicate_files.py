"""Remove source files already recorded as exact duplicates in literature.db."""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "index" / "literature.db"
REPORT_PATH = ROOT / "reports" / "duplicate_file_removal.json"


def normalized(path: Path) -> str:
    return os.path.normcase(os.path.abspath(path))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Delete validated duplicate files")
    args = parser.parse_args()

    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(
            """
            SELECT d.source_path, d.canonical_document_id, d.reason,
                   c.source_path AS canonical_path
            FROM duplicates d
            LEFT JOIN documents c ON c.id = d.canonical_document_id
            ORDER BY d.source_path
            """
        ).fetchall()

    records: list[dict] = []
    unsafe: list[dict] = []
    for row in rows:
        duplicate = Path(row["source_path"])
        canonical_value = row["canonical_path"]
        canonical = Path(canonical_value) if canonical_value else None
        problems: list[str] = []
        if canonical is None:
            problems.append("canonical record missing")
        elif not canonical.is_file():
            problems.append("canonical file missing")
        if canonical is not None and normalized(duplicate) == normalized(canonical):
            problems.append("duplicate path equals canonical path")
        if duplicate.suffix.casefold() != ".pdf":
            problems.append("duplicate is not a PDF")
        record = {
            "source_path": str(duplicate),
            "canonical_document_id": row["canonical_document_id"],
            "canonical_path": str(canonical) if canonical else None,
            "reason": row["reason"],
            "existed_before": duplicate.is_file(),
            "problems": problems,
        }
        records.append(record)
        if problems:
            unsafe.append(record)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "apply" if args.apply else "dry-run",
        "database_rows": len(rows),
        "existing_duplicate_files": sum(record["existed_before"] for record in records),
        "unsafe_records": len(unsafe),
        "deleted": 0,
        "already_absent": 0,
        "records": records,
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    if unsafe:
        print(json.dumps({"status": "aborted", "unsafe": len(unsafe)}, ensure_ascii=False))
        return 2
    if not args.apply:
        print(json.dumps({"status": "validated", **{k: report[k] for k in ("database_rows", "existing_duplicate_files", "unsafe_records")}}, ensure_ascii=False))
        return 0

    deleted = already_absent = 0
    for record in records:
        path = Path(record["source_path"])
        if not path.exists():
            already_absent += 1
            continue
        path.unlink()
        deleted += 1

    report["deleted"] = deleted
    report["already_absent"] = already_absent
    report["confirmed_absent_after"] = sum(
        not Path(record["source_path"]).exists() for record in records
    )
    report["completed_at"] = datetime.now(timezone.utc).isoformat()
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "complete",
                "deleted": deleted,
                "already_absent": already_absent,
                "confirmed_absent_after": report["confirmed_absent_after"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
