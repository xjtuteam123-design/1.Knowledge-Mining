"""Resumably enrich Markdown papers with DeepSeek structured knowledge cards."""

from __future__ import annotations

import argparse
import json
import random
import sys
import threading
import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from prompts import LITERATURE_ANALYSIS_PROMPT  # noqa: E402
from rag_store import REPORTS_DIR, STRUCTURED_DIR, _chunk_structured, _connect, _insert_chunk  # noqa: E402


PRINT_LOCK = threading.Lock()
WRITE_LOCK = threading.Lock()
STOP_EVENT = threading.Event()
USAGE_LOG = REPORTS_DIR / "api_usage.jsonl"


def emit(payload: dict) -> None:
    with PRINT_LOCK:
        print(json.dumps(payload, ensure_ascii=False), flush=True)


def split_markdown(markdown: str, max_chars: int) -> list[str]:
    """Split oversized documents at page headings while keeping every character."""
    if len(markdown) <= max_chars:
        return [markdown]
    blocks = markdown.split("\n\n")
    parts: list[str] = []
    current: list[str] = []
    length = 0
    for block in blocks:
        addition = len(block) + 2
        if current and length + addition > max_chars:
            parts.append("\n\n".join(current))
            current = []
            length = 0
        if addition > max_chars:
            for start in range(0, len(block), max_chars):
                if current:
                    parts.append("\n\n".join(current))
                    current = []
                    length = 0
                parts.append(block[start : start + max_chars])
        else:
            current.append(block)
            length += addition
    if current:
        parts.append("\n\n".join(current))
    return [part for part in parts if part.strip()]


def call_deepseek(client: OpenAI, config: dict, name: str, text: str, part: int, total: int):
    segment_note = ""
    if total > 1:
        segment_note = (
            f"This is source-text segment {part} of {total} from one oversized document. "
            "Extract only evidence present in this segment. Preserve page/section evidence, "
            "and do not infer missing information from other segments.\n\n"
        )
    last_error: Exception | None = None
    for attempt in range(1, 6):
        try:
            return client.chat.completions.create(
                model=config["model"],
                messages=[
                    {"role": "system", "content": LITERATURE_ANALYSIS_PROMPT},
                    {
                        "role": "user",
                        "content": (
                            f"Paper file name: {name}\n\n{segment_note}"
                            f"Paper text:\n\n{text}"
                        ),
                    },
                ],
                max_tokens=config.get("ingestion_max_tokens", 8192),
                extra_body={"thinking": {"type": "disabled"}},
                timeout=config.get("api_timeout_seconds", 900),
            )
        except Exception as exc:  # SDK errors vary by version/status.
            last_error = exc
            status = getattr(exc, "status_code", None)
            if status in {401, 402, 403}:
                STOP_EVENT.set()
            if status in {400, 401, 402, 403, 404}:
                raise
            if attempt == 5:
                raise
            delay = min(30, (2 ** (attempt - 1)) + random.random())
            emit({"event": "retry", "name": name, "part": part, "attempt": attempt, "delay_seconds": round(delay, 1), "error": str(exc)})
            time.sleep(delay)
    raise last_error or RuntimeError("DeepSeek request failed")


def usage_dict(response) -> dict:
    usage = getattr(response, "usage", None)
    return {
        "prompt_tokens": int(getattr(usage, "prompt_tokens", 0) or 0),
        "completion_tokens": int(getattr(usage, "completion_tokens", 0) or 0),
        "total_tokens": int(getattr(usage, "total_tokens", 0) or 0),
    }


def record_usage(payload: dict) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    with WRITE_LOCK:
        with USAGE_LOG.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")


def analyze_one(client: OpenAI, config: dict, row: dict, max_input_chars: int) -> dict:
    if STOP_EVENT.is_set():
        raise RuntimeError("Batch stopped after a fatal API authorization or balance error")
    markdown = (ROOT / row["markdown_path"]).read_text(encoding="utf-8")
    parts = split_markdown(markdown, max_input_chars)
    outputs: list[str] = []
    totals = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    for index, part_text in enumerate(parts, 1):
        if STOP_EVENT.is_set():
            raise RuntimeError("Batch stopped after a fatal API authorization or balance error")
        response = call_deepseek(client, config, row["name"], part_text, index, len(parts))
        text = response.choices[0].message.content or ""
        if not text.strip():
            raise ValueError("DeepSeek returned empty structured content")
        outputs.append(text.strip())
        used = usage_dict(response)
        for key in totals:
            totals[key] += used[key]
        record_usage(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "document_id": row["id"],
                "name": row["name"],
                "part": index,
                "parts": len(parts),
                "model": config["model"],
                **used,
            }
        )
    if len(outputs) == 1:
        structured_text = outputs[0]
    else:
        structured_text = "\n\n".join(
            f"# Oversized Document Segment {i}/{len(outputs)}\n\n{value}"
            for i, value in enumerate(outputs, 1)
        )
    chunks = _chunk_structured(structured_text)
    output = STRUCTURED_DIR / Path(row["markdown_path"]).name
    temporary = output.with_suffix(output.suffix + ".tmp")
    with WRITE_LOCK:
        output.parent.mkdir(parents=True, exist_ok=True)
        temporary.write_text(structured_text.rstrip() + "\n", encoding="utf-8")
        temporary.replace(output)
        with _connect() as connection:
            # Defensive cleanup makes a retry idempotent if a prior run stopped
            # between inserting chunks and marking the document complete.
            stale = connection.execute(
                "SELECT id FROM chunks WHERE document_id=? AND kind='structured_analysis'",
                (row["id"],),
            ).fetchall()
            if stale:
                ids = [str(item["id"]) for item in stale]
                connection.executemany("DELETE FROM chunks_fts WHERE chunk_id=?", [(value,) for value in ids])
                connection.execute(
                    "DELETE FROM chunks WHERE document_id=? AND kind='structured_analysis'",
                    (row["id"],),
                )
            for chunk in chunks:
                _insert_chunk(connection, row["id"], row["name"], None, "structured_analysis", chunk)
            connection.execute(
                "UPDATE documents SET structured=1, chunk_count=(SELECT COUNT(*) FROM chunks WHERE document_id=?) WHERE id=?",
                (row["id"], row["id"]),
            )
    return {"parts": len(parts), "structured_chunks": len(chunks), **totals}


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
        sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=0, help="Maximum papers to analyze; 0 means all")
    parser.add_argument("--workers", type=int, default=8, help="Concurrent API requests")
    parser.add_argument(
        "--max-input-chars",
        type=int,
        default=1_800_000,
        help="Split oversized Markdown before it approaches the model context limit",
    )
    args = parser.parse_args()
    config = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
    client = OpenAI(api_key=config["api_key"], base_url=config["base_url"])
    with _connect() as connection:
        rows = [dict(row) for row in connection.execute(
            "SELECT * FROM documents WHERE structured=0 ORDER BY created_at"
        ).fetchall()]
    if args.limit:
        rows = rows[: args.limit]
    emit({"event": "start", "papers": len(rows), "workers": args.workers, "model": config["model"]})
    succeeded = failed = 0
    token_totals = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    completed = 0
    iterator = iter(rows)
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {}
        for row in iterator:
            futures[executor.submit(analyze_one, client, config, row, args.max_input_chars)] = row
            if len(futures) >= max(1, args.workers):
                break
        while futures:
            done, _ = wait(futures, return_when=FIRST_COMPLETED)
            for future in done:
                row = futures.pop(future)
                completed += 1
                try:
                    result = future.result()
                    succeeded += 1
                    for key in token_totals:
                        token_totals[key] += result[key]
                    emit({"event": "paper", "completed": completed, "total": len(rows), "status": "analyzed", "name": row["name"], **result})
                except Exception as exc:
                    failed += 1
                    emit({"event": "paper", "completed": completed, "total": len(rows), "status": "failed", "name": row["name"], "error": str(exc)})
                if not STOP_EVENT.is_set():
                    try:
                        next_row = next(iterator)
                    except StopIteration:
                        pass
                    else:
                        futures[executor.submit(analyze_one, client, config, next_row, args.max_input_chars)] = next_row
            if STOP_EVENT.is_set() and futures:
                # Already-running siblings may finish or fail; no new documents
                # are submitted after a fatal authorization/balance error.
                continue
    emit({"event": "complete", "succeeded": succeeded, "failed": failed, **token_totals})
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
