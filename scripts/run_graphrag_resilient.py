"""Resume unattempted GraphRAG documents and wait safely through API outages."""

from __future__ import annotations

import argparse
import json
import sqlite3
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

from openai import OpenAI


ROOT = Path(__file__).resolve().parents[1]
RETRY_SECONDS = 300
FAILED_RETRY_LIST = ROOT / "reports" / "graph_failed_retry_ids.txt"


def log(message: str) -> None:
    print(f"[RESILIENT {datetime.now().isoformat(timespec='seconds')}] {message}", flush=True)


def generation_available() -> bool:
    """Probe chat generation cheaply before submitting large document prompts."""
    config = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
    try:
        client = OpenAI(
            api_key=config["api_key"],
            base_url=config["base_url"],
            max_retries=0,
            timeout=30,
        )
        client.chat.completions.create(
            model=config["model"],
            messages=[{"role": "user", "content": "Reply OK."}],
            max_tokens=2,
            extra_body={"thinking": {"type": "disabled"}},
        )
        return True
    except Exception as exc:
        log(f"DeepSeek generation health check failed: {str(exc)[:500]}")
        return False


def failed_batch_ids(include_file: Path | None) -> list[str]:
    allowed = None
    if include_file is not None:
        allowed = {
            line.strip()
            for line in include_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        }
    with sqlite3.connect(ROOT / "data" / "graph" / "graph.db") as connection:
        return [
            str(document_id)
            for (document_id,) in connection.execute(
                "SELECT document_id FROM graph_papers WHERE status='failed' ORDER BY updated_at"
            )
            if allowed is None or str(document_id) in allowed
        ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--include-file",
        type=Path,
        default=ROOT / "reports" / "graph_next_2000_ids.txt",
        help="Document ID list to finish; use --all-corpus to process every eligible document",
    )
    parser.add_argument("--all-corpus", action="store_true")
    parser.add_argument(
        "--unstarted-first",
        action="store_true",
        help="Process never-attempted documents before repairing failures",
    )
    args = parser.parse_args()
    include_file = None if args.all_corpus else args.include_file
    if include_file is not None and not include_file.is_absolute():
        include_file = ROOT / include_file
    unstarted_command = [
        sys.executable,
        str(ROOT / "scripts" / "extract_graphrag.py"),
        "--selection",
        "all",
        "--skip-failed",
        "--max-input-chars",
        "30000",
        "--workers",
        "2",
    ]
    if include_file is None:
        unstarted_command.extend(["--limit", "1000000", "--include-long-documents"])
    else:
        unstarted_command.extend(["--include-file", str(include_file)])
    # Repair existing failures before spending requests on never-attempted
    # documents. After the unstarted pass, make one final repair pass for any
    # documents that failed during that phase.
    phase = "unstarted" if args.unstarted_first else "failed_first"
    while True:
        if not generation_available():
            log(f"No documents submitted; retrying health check in {RETRY_SECONDS} seconds.")
            time.sleep(RETRY_SECONDS)
            continue
        if phase == "unstarted":
            log("Starting or resuming the unattempted-document batch.")
            result = subprocess.run(unstarted_command, cwd=ROOT)
            if result.returncode == 0:
                log("No unattempted documents remain; moving to the final failed-document repair pass.")
                phase = "failed_final"
                continue
        else:
            failed_ids = failed_batch_ids(include_file)
            if not failed_ids:
                if phase == "failed_first":
                    log("No existing failed documents remain; starting unattempted documents.")
                    phase = "unstarted"
                    continue
                log("All selected documents, including prior failures, are complete.")
                return 0
            FAILED_RETRY_LIST.write_text("\n".join(failed_ids) + "\n", encoding="utf-8")
            label = "existing" if phase == "failed_first" else "final"
            log(f"Repairing {len(failed_ids)} {label} failed documents with 15000-character segments.")
            repair_command = [
                sys.executable,
                str(ROOT / "scripts" / "extract_graphrag.py"),
                "--include-file",
                str(FAILED_RETRY_LIST),
                "--selection",
                "all",
                "--max-input-chars",
                "15000",
                "--workers",
                "2",
            ]
            result = subprocess.run(repair_command, cwd=ROOT)
            if result.returncode == 0:
                if phase == "failed_first":
                    remaining = len(failed_batch_ids(include_file))
                    log(f"Initial repair pass finished with {remaining} unresolved documents; continuing with unattempted documents.")
                    phase = "unstarted"
                    continue
                if not failed_batch_ids(include_file):
                    log("All selected documents, including prior failures, are complete.")
                    return 0
        if result.returncode == 3:
            log(f"DeepSeek generation is unavailable; retrying in {RETRY_SECONDS} seconds.")
            time.sleep(RETRY_SECONDS)
            continue
        if phase == "failed_final":
            remaining = len(failed_batch_ids(include_file))
            log(f"Repair pass finished with {remaining} unresolved documents; stopping to avoid repeated API cost.")
            return 2
        if phase == "failed_first":
            remaining = len(failed_batch_ids(include_file))
            log(f"Initial repair pass ended with {remaining} unresolved documents; continuing with unattempted documents.")
            phase = "unstarted"
            continue
        log(f"Extraction exited with code {result.returncode}; rerunning to skip completed/failed records.")
        time.sleep(5)


if __name__ == "__main__":
    raise SystemExit(main())
