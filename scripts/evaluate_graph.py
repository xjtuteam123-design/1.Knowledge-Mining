"""Generate a local quality and coverage report for the GraphRAG database."""

from __future__ import annotations

import json
import sqlite3
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from graph_store import GRAPH_DB_PATH, make_graph_figure  # noqa: E402


def decode(value: str, fallback):
    try:
        return json.loads(value)
    except (TypeError, json.JSONDecodeError):
        return fallback


def main() -> int:
    if not GRAPH_DB_PATH.exists():
        print("Graph database does not exist.")
        return 1
    connection = sqlite3.connect(GRAPH_DB_PATH)
    connection.row_factory = sqlite3.Row
    try:
        papers = [dict(row) for row in connection.execute(
            "SELECT * FROM graph_papers WHERE status='complete' ORDER BY name"
        )]
        failures = [dict(row) for row in connection.execute(
            "SELECT name,error FROM graph_papers WHERE status='failed' ORDER BY name"
        )]
        node_types = dict(connection.execute(
            "SELECT type,COUNT(*) FROM nodes GROUP BY type ORDER BY COUNT(*) DESC"
        ).fetchall())
        predicates = dict(connection.execute(
            "SELECT predicate,COUNT(*) FROM edges GROUP BY predicate ORDER BY COUNT(*) DESC"
        ).fetchall())
        assertion_levels = dict(connection.execute(
            "SELECT COALESCE(assertion_level,'unspecified'),COUNT(*) FROM edges GROUP BY assertion_level"
        ).fetchall())
        node_count = connection.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
        edge_count = connection.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
        unresolved = connection.execute("SELECT COUNT(*) FROM nodes WHERE type='UnresolvedEntity'").fetchone()[0]
        observations = [dict(row) for row in connection.execute(
            "SELECT attributes_json,evidence_json FROM nodes WHERE type='Property'"
        )]
        property_with_value = 0
        property_with_temperature = 0
        property_with_evidence = 0
        for row in observations:
            attributes = decode(row["attributes_json"], {})
            evidence = decode(row["evidence_json"], [])
            if attributes.get("value") is not None or attributes.get("min_value") is not None or attributes.get("max_value") is not None:
                property_with_value += 1
            conditions = attributes.get("conditions") if isinstance(attributes.get("conditions"), dict) else {}
            if conditions.get("temperature_c") is not None:
                property_with_temperature += 1
            if evidence:
                property_with_evidence += 1
        edge_evidence = connection.execute(
            "SELECT COUNT(*) FROM edges WHERE evidence_json NOT IN ('[]','', 'null')"
        ).fetchone()[0]
    finally:
        connection.close()

    prompt_tokens = sum(int(row.get("prompt_tokens") or 0) for row in papers)
    completion_tokens = sum(int(row.get("completion_tokens") or 0) for row in papers)
    all_time_usage_by_model: dict[str, dict[str, int]] = {}
    usage_log = ROOT / "reports" / "graph_api_usage.jsonl"
    if usage_log.exists():
        for line in usage_log.read_text(encoding="utf-8").splitlines():
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            model = str(item.get("model") or "unknown")
            totals = all_time_usage_by_model.setdefault(
                model, {"requests": 0, "prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
            )
            totals["requests"] += 1
            for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
                totals[key] += int(item.get(key) or 0)
    pro_usage = all_time_usage_by_model.get("deepseek-v4-pro", {})
    pro_estimated_cost = (
        int(pro_usage.get("prompt_tokens", 0)) / 1_000_000 * 4.5
        + int(pro_usage.get("completion_tokens", 0)) / 1_000_000 * 13.5
    )
    all_time_logged_prompt_tokens = sum(value["prompt_tokens"] for value in all_time_usage_by_model.values())
    all_time_logged_completion_tokens = sum(value["completion_tokens"] for value in all_time_usage_by_model.values())
    failure_groups = Counter(
        "Insufficient Balance (402)" if "402" in (row.get("error") or "") else
        "Connection error" if "Connection error" in (row.get("error") or "") else
        "JSON format error" if any(marker in (row.get("error") or "") for marker in ("delimiter", "Unterminated", "JSON")) else
        "Other"
        for row in failures
    )
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "target_papers": 50,
        "completed_papers": len(papers),
        "remaining_papers": max(0, 50 - len(papers)),
        "failed_records": len(failures),
        "failure_groups": dict(failure_groups),
        "nodes": node_count,
        "edges": edge_count,
        "node_types": node_types,
        "predicates": predicates,
        "assertion_levels": assertion_levels,
        "unresolved_nodes": unresolved,
        "property_observations": len(observations),
        "property_observations_with_values": property_with_value,
        "property_observations_with_temperature": property_with_temperature,
        "property_observations_with_evidence": property_with_evidence,
        "edges_with_evidence": edge_evidence,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "total_tokens": prompt_tokens + completion_tokens,
        "token_scope": "successful responses stored in the active graph; retries excluded",
        "all_time_logged_prompt_tokens": all_time_logged_prompt_tokens,
        "all_time_logged_completion_tokens": all_time_logged_completion_tokens,
        "all_time_logged_total_tokens": all_time_logged_prompt_tokens + all_time_logged_completion_tokens,
        "all_time_usage_by_model": all_time_usage_by_model,
        "estimated_v4_pro_subset_off_peak_cost_cny": round(pro_estimated_cost, 2),
        "completed_document_names": [row["name"] for row in papers],
    }
    reports = ROOT / "reports"
    reports.mkdir(parents=True, exist_ok=True)
    (reports / "graph_quality.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    pct = lambda part, total: (part / total * 100) if total else 0.0
    type_lines = "\n".join(f"- {name}: {count}" for name, count in node_types.items()) or "- 无"
    relation_lines = "\n".join(f"- {name}: {count}" for name, count in predicates.items()) or "- 无"
    failure_lines = "\n".join(f"- {name}: {count}" for name, count in failure_groups.items()) or "- 无"
    paper_lines = "\n".join(f"- {row['name']}" for row in papers) or "- 无"
    usage_lines = "\n".join(
        f"- {name}: {values['requests']} 次请求，输入 {values['prompt_tokens']:,}，"
        f"输出 {values['completion_tokens']:,}，总计 {values['total_tokens']:,} tokens"
        for name, values in sorted(all_time_usage_by_model.items())
    ) or "- 无"
    markdown = f"""# GraphRAG 试运行质量报告

生成时间：{payload['generated_at']}

## 进度

- 目标：50 篇
- 已完成：{len(papers)} 篇
- 尚需完成：{payload['remaining_papers']} 篇
- 当前失败记录：{len(failures)} 篇（断点续跑时会自动重试）

## 图谱规模

- 节点：{node_count:,}
- 关系：{edge_count:,}
- 未解析占位节点：{unresolved:,}
- 性能观察节点：{len(observations):,}

## 性能数据质量

- 有明确数值或范围：{property_with_value}/{len(observations)}（{pct(property_with_value, len(observations)):.1f}%）
- 有测试温度：{property_with_temperature}/{len(observations)}（{pct(property_with_temperature, len(observations)):.1f}%）
- 有原文证据：{property_with_evidence}/{len(observations)}（{pct(property_with_evidence, len(observations)):.1f}%）
- 有原文证据的关系：{edge_evidence}/{edge_count}（{pct(edge_evidence, edge_count):.1f}%）

## 节点类型

{type_lines}

## 关系类型

{relation_lines}

## API 用量

- 当前活动图谱成功响应输入 tokens：{prompt_tokens:,}
- 当前活动图谱成功响应输出 tokens：{completion_tokens:,}
- 当前活动图谱成功响应总 tokens：{prompt_tokens + completion_tokens:,}
- 全历史日志总 tokens（包含重试及已归档批次）：{all_time_logged_prompt_tokens + all_time_logged_completion_tokens:,}

全历史日志按模型拆分：

{usage_lines}

- 其中 v4-pro 部分按项目既有低峰价格公式估算：约 ¥{pro_estimated_cost:.2f}

说明：当前活动图谱数字来自成功入库记录，不包含无效 JSON 重试；全历史日志包含当前目录保留的重试和已归档批次，因此两者不能当作同一批次费用。上述金额仅估算 v4-pro 部分，不包含 Flash，也不是 DeepSeek 账单实扣金额。新版抽取任务会写入 run_id 和包含重试的批次用量。

## 未完成原因

{failure_lines}

## 已完成论文

{paper_lines}
"""
    (reports / "GRAPH_PILOT_REPORT.md").write_text(markdown, encoding="utf-8")
    figure, _, _ = make_graph_figure("", 70, 1)
    figure.write_html(
        reports / "graph_preview.html",
        include_plotlyjs=True,
        full_html=True,
        auto_open=False,
    )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
