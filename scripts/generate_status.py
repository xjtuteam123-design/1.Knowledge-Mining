"""Generate a durable Markdown/JSON status report from the local corpus."""

from __future__ import annotations

import json
import sqlite3
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "index" / "literature.db"
REPORTS = ROOT / "reports"
USAGE_LOG = REPORTS / "api_usage.jsonl"


def main() -> None:
    with sqlite3.connect(DB) as connection:
        connection.row_factory = sqlite3.Row
        documents = connection.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
        structured = connection.execute("SELECT COUNT(*) FROM documents WHERE structured=1").fetchone()[0]
        duplicates = connection.execute("SELECT COUNT(*) FROM duplicates").fetchone()[0]
        failures = connection.execute("SELECT error FROM failures").fetchall()
        raw_chunks = connection.execute("SELECT COUNT(*) FROM chunks WHERE kind='original_text'").fetchone()[0]
        structured_chunks = connection.execute("SELECT COUNT(*) FROM chunks WHERE kind='structured_analysis'").fetchone()[0]

    usage = {"requests": 0, "prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    if USAGE_LOG.exists():
        for line in USAGE_LOG.read_text(encoding="utf-8").splitlines():
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            usage["requests"] += 1
            for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
                usage[key] += int(item.get(key, 0) or 0)

    # This is an upper-bound estimate that treats all input as cache-miss input.
    off_peak_cny = usage["prompt_tokens"] / 1_000_000 * 4.5 + usage["completion_tokens"] / 1_000_000 * 13.5
    failure_groups = Counter(row["error"] for row in failures)
    generated = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    status = {
        "generated_at": generated,
        "source_files_accounted_for": documents + duplicates + len(failures),
        "unique_documents": documents,
        "duplicates": duplicates,
        "failures": len(failures),
        "original_text_chunks": raw_chunks,
        "structured_documents": structured,
        "structured_remaining": documents - structured,
        "structured_chunks": structured_chunks,
        "api_usage": usage,
        "v4_pro_off_peak_cost_upper_bound_cny": round(off_peak_cny, 2),
        "failure_groups": dict(failure_groups),
    }
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "run_status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    failure_lines = "\n".join(f"- {count} × `{error}`" for error, count in failure_groups.items()) or "- 无"
    markdown = f"""# 语料处理状态

生成时间：{generated}

## 本地语料

- 已核对源文件：{status['source_files_accounted_for']:,}
- 唯一文献：{documents:,}
- 重复文献：{duplicates:,}
- 待修复文件：{len(failures):,}
- 原文检索切片：{raw_chunks:,}

## DeepSeek 结构化提取

- 已完成文献：{structured:,}
- 剩余文献：{documents - structured:,}
- 结构化知识切片：{structured_chunks:,}
- 已完成 API 请求：{usage['requests']:,}
- 输入 tokens：{usage['prompt_tokens']:,}
- 输出 tokens：{usage['completion_tokens']:,}
- 总 tokens：{usage['total_tokens']:,}
- V4 Pro 闲时费用上限估算：¥{off_peak_cny:,.2f}（输入全部按缓存未命中计算）

## 当前失败类型

{failure_lines}
"""
    (REPORTS / "STATUS.md").write_text(markdown, encoding="utf-8")
    print(json.dumps(status, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
