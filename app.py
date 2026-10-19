import gradio as gr
import argparse
import html
import json
import os
import re
import uuid
import warnings
from datetime import datetime
from pathlib import Path

# Gradio 5.50 announces constructor/launch changes that only become available
# in Gradio 6, and OpenAI 1.69 imports a legacy Pydantic compatibility module
# on Python 3.14. Keep these known startup notices quiet without hiding runtime
# errors or unrelated warnings.
warnings.filterwarnings(
    "ignore",
    message=r"Core Pydantic V1 functionality isn't compatible with Python 3\.14 or greater\.",
    category=UserWarning,
)
for deprecated_parameter in ("theme", "css", "show_api"):
    warnings.filterwarnings(
        "ignore",
        message=rf"The '{deprecated_parameter}' parameter .* will be removed in Gradio 6\.0\..*",
        category=DeprecationWarning,
    )
warnings.filterwarnings(
    "ignore",
    message=r"The default value of 'allow_tags' in gr\.Chatbot will be changed .*",
    category=DeprecationWarning,
)

from openai import OpenAI
from PIL import Image, ImageDraw, ImageFont
from rag_store import (
    chunk_history_stats,
    count_original_chunks,
    fetch_original_chunks,
    historical_chunk_priors,
    record_retrieval_feedback,
    retrieval_question_count,
    search_global,
)
from prompts import LITERATURE_ANALYSIS_PROMPT, QUESTION_ANSWER_PROMPT
from graph_store import (
    active_graph_document_ids,
    citation_metadata_index,
    graph_evidence,
    graph_stats,
    make_graph_html,
    parsed_corpus_stats,
)
from account_store import (
    authenticate_or_register,
    record_authenticated_access,
    record_online_presence,
)

# Keep localhost traffic local if standard proxy environment variables happen
# to be present. This does not enable, require, or assume any proxy software.
for proxy_bypass_key in ("NO_PROXY", "no_proxy"):
    bypass_values = [value.strip() for value in os.environ.get(proxy_bypass_key, "").split(",") if value.strip()]
    for local_host in ("127.0.0.1", "localhost"):
        if local_host not in bypass_values:
            bypass_values.append(local_host)
    os.environ[proxy_bypass_key] = ",".join(bypass_values)

# Configure an optional OpenAI-compatible model. Retrieval always runs locally.
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
    model = config['model']
    api_key = config.get('api_key', '')
    base_url = config.get('base_url', '').strip()


def _positive_integer(value, fallback, minimum=1):
    """Read an integer UI/config value without imposing an arbitrary upper cap."""
    try:
        return max(minimum, int(float(value)))
    except (TypeError, ValueError, OverflowError):
        return max(minimum, int(fallback))


GRAPH_NODE_SLIDER_MAX = _positive_integer(config.get("graph_max_nodes_upper", 300), 300, 10)
GRAPH_HOP_SLIDER_MAX = _positive_integer(config.get("graph_hops_upper", 6), 6, 1)
GRAPH_NODE_DEFAULT = min(
    _positive_integer(config.get("graph_max_nodes", 100), 100, 10),
    GRAPH_NODE_SLIDER_MAX,
)
GRAPH_HOP_DEFAULT = min(
    _positive_integer(config.get("graph_hops", 2), 2, 1),
    GRAPH_HOP_SLIDER_MAX,
)

client = OpenAI(api_key=api_key or "local", base_url=base_url) if base_url else None

HISTORY_DIR = "chat_history"
LOADING_MESSAGE_ID = "answer-loading-dots"
LOADING_DOTS_HTML = (
    '<span class="answer-loading-dots" role="status" aria-label="Generating an answer">'
    '<i></i><i></i><i></i></span>'
)


def is_loading_message(message):
    """Return whether a Gradio chat message is the temporary loading row.

    Gradio may normalize an explicitly supplied ``metadata`` value to ``None``
    while passing chatbot messages between event callbacks, so metadata cannot
    be assumed to remain a dictionary.
    """
    if not isinstance(message, dict) or message.get("role") != "assistant":
        return False
    metadata = message.get("metadata")
    metadata_id = metadata.get("id") if isinstance(metadata, dict) else None
    return (
        metadata_id == LOADING_MESSAGE_ID
        or message.get("content") in {"...", LOADING_DOTS_HTML}
    )


def env_flag(name, default=False):
    return os.getenv(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


PUBLIC_MODE = env_flag("RAG_PUBLIC_MODE")
PUBLIC_READONLY = env_flag("RAG_PUBLIC_READONLY", PUBLIC_MODE)
SHARE_PUBLICLY = env_flag("GRADIO_SHARE")
AUTH_USER = os.getenv("GRADIO_AUTH_USER", "").strip()
AUTH_PASSWORD = os.getenv("GRADIO_AUTH_PASSWORD", "")
if PUBLIC_MODE:
    LAUNCH_AUTH = authenticate_or_register
    AUTH_MESSAGE = (
        "## Register or sign in\n"
        "Enter a username (3–32 letters, numbers, `.`, `_`, or `-`) and a password "
        "of at least 8 characters. A new username creates an account automatically; "
        "an existing username requires its original password."
    )
else:
    LAUNCH_AUTH = (AUTH_USER, AUTH_PASSWORD) if AUTH_USER and AUTH_PASSWORD else None
    AUTH_MESSAGE = "Refractory Literature RAG — authorized users only" if LAUNCH_AUTH else None


def _public_request_details(request: gr.Request) -> tuple[str, str, str, str]:
    headers = {str(key).lower(): str(value) for key, value in dict(request.headers).items()}
    forwarded_ip = (
        headers.get("cf-connecting-ip")
        or headers.get("true-client-ip")
        or headers.get("x-real-ip")
        or headers.get("x-forwarded-for", "").split(",", 1)[0].strip()
    )
    direct_ip = getattr(getattr(request, "client", None), "host", "")
    ip_address = (forwarded_ip or direct_ip or "unknown")[:128]
    return (
        request.username or "",
        ip_address,
        headers.get("user-agent", ""),
        request.session_hash or "",
    )


def record_public_registration(request: gr.Request) -> None:
    """Attach the authenticated visitor IP to a newly registered account."""
    if not PUBLIC_MODE or request is None or not request.username:
        return
    username, ip_address, user_agent, session_hash = _public_request_details(request)
    record_authenticated_access(
        username,
        ip_address,
        user_agent,
        session_hash,
    )


def refresh_public_presence(request: gr.Request) -> None:
    """Keep an authenticated browser session in the terminal online count."""
    if not PUBLIC_MODE or request is None or not request.username:
        return
    username, ip_address, _, session_hash = _public_request_details(request)
    record_online_presence(username, ip_address, session_hash)

SYSTEM_PROMPT = QUESTION_ANSWER_PROMPT

RETRIEVAL_MODES = {
    "Targeted Q&A — Relevance 0.8": 80.0,
    "Standard Q&A — Relevance 0.6": 60.0,
    "Deep Q&A — Relevance 0.3": 30.0,
    "Full Knowledge Base Q&A — Relevance 0.1": 10.0,
}
DEFAULT_RETRIEVAL_MODE = "Standard Q&A — Relevance 0.6"


# Override legacy labels (some earlier files carried mojibake dash characters)
# with stable English UI labels and per-mode retrieval breadth.
RETRIEVAL_MODES = {
    "Targeted Q&A — Relevance 0.8": 80.0,
    "Standard Q&A — Relevance 0.6": 60.0,
    "Deep Q&A — Relevance 0.3": 30.0,
    "Full Knowledge Base Q&A — Relevance 0.1": 10.0,
}
RETRIEVAL_PROFILES = {
    "Targeted Q&A — Relevance 0.8": {
        "graph_nodes": 90, "graph_hops": 1, "context_budget": 35_000,
    },
    "Standard Q&A — Relevance 0.6": {
        "graph_nodes": 160, "graph_hops": 2, "context_budget": 60_000,
    },
    "Deep Q&A — Relevance 0.3": {
        "graph_nodes": 300, "graph_hops": 3, "context_budget": 100_000,
    },
    "Full Knowledge Base Q&A — Relevance 0.1": {
        "graph_nodes": 500, "graph_hops": 4, "context_budget": 160_000,
    },
}
DEFAULT_RETRIEVAL_MODE = "Standard Q&A — Relevance 0.6"


def resolve_retrieval_mode(value):
    """Resolve a UI mode label while accepting legacy numeric thresholds."""
    if value in RETRIEVAL_MODES:
        return str(value), RETRIEVAL_MODES[str(value)]
    try:
        threshold = float(value)
    except (TypeError, ValueError):
        return DEFAULT_RETRIEVAL_MODE, RETRIEVAL_MODES[DEFAULT_RETRIEVAL_MODE]
    if 0 <= threshold <= 1:
        threshold *= 100
    threshold = max(0.0, min(threshold, 100.0))
    return f"Custom relevance {threshold / 100:g}", threshold


def is_greeting_only(text):
    """Recognize standalone greetings that should not query the literature."""
    normalized = re.sub(r"[^a-z\u3400-\u9fff]+", " ", str(text or "").casefold()).strip()
    compact = normalized.replace(" ", "")
    english_greeting = re.fullmatch(
        r"(?:hello|hi|hey|goodmorning|goodafternoon|goodevening)(?:there)?",
        compact,
    )
    chinese_greeting = re.fullmatch(
        r"(?:(?:你|您)好(?:呀|啊|哇)?|嗨|哈[啰罗喽]|早上好|下午好|晚上好)",
        compact,
    )
    return bool(english_greeting or chinese_greeting)


def greeting_response(text):
    if re.search(r"[\u3400-\u9fff]", str(text or "")):
        return "你好！请告诉我你想了解的合金、成分、工艺、组织或性能问题。"
    return "Hello! Please ask me about an alloy, composition, process, microstructure, or property."


def analyze_paper(filename, paper_text):
    """Use the configured model to turn a paper into structured RAG knowledge."""
    if client is None:
        return ""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": LITERATURE_ANALYSIS_PROMPT},
            {
                "role": "user",
                "content": f"Paper file name: {filename}\n\nFull paper text:\n\n{paper_text}",
            },
        ],
        stream=False,
        max_tokens=config.get("ingestion_max_tokens", 8192),
        extra_body={"thinking": {"type": "disabled"}},
    )
    return response.choices[0].message.content or ""


def _reference_key(result):
    return str(result.get("document_id") or result.get("source") or "Unknown source").casefold()


def _reference_numbers(results):
    numbers = {}
    for result in results:
        key = _reference_key(result)
        if key not in numbers:
            numbers[key] = len(numbers) + 1
    return numbers


def _cited_reference_numbers(answer):
    return {
        int(value)
        for value in re.findall(
            r"\[(?:Source\s*)?(\d+)\]",
            str(answer or ""),
            flags=re.IGNORECASE,
        )
    }


def _citation_coverage_instruction(results):
    required = sorted(set(_reference_numbers(results).values()))
    labels = ", ".join(f"[{number}]" for number in required)
    return (
        f"Mandatory citation coverage: the evidence contains {len(required)} unique "
        f"numbered references. The final answer must cite every one at least once: {labels}. "
        "Attach each citation to a statement it actually supports. References supporting the "
        "same statement may be grouped together."
    )


def format_sources(results):
    """Format retrieved chunks for prompts and source display."""
    numbers = _reference_numbers(results)
    sections = []
    for result in results:
        index = numbers[_reference_key(result)]
        page = f", page {result['page']}" if result.get("page") else ""
        relation = f", graph relation: {result['relation']}" if result.get("relation") else ""
        sections.append(f"[{index}] Evidence from {result['source']}{page}{relation}:\n{result['text']}")
    return "\n\n".join(sections)


def _format_authors(value):
    authors = value if isinstance(value, list) else [value] if value else []
    authors = [str(author).strip() for author in authors if str(author).strip()]
    if len(authors) > 6:
        return ", ".join(authors[:3]) + ", et al."
    return ", ".join(authors)


def _page_sort_key(page):
    match = re.match(r"^\s*(\d+)", str(page))
    return (0, int(match.group(1)), str(page)) if match else (1, 0, str(page).casefold())


def format_reference_list(results):
    """Render deduplicated numbered references with merged evidence pages."""
    numbers = _reference_numbers(results)
    grouped = {}
    for result in results:
        key = _reference_key(result)
        item = grouped.setdefault(
            key,
            {"result": result, "pages": [], "evidence_count": 0, "chunk_ids": set()},
        )
        page = str(result.get("page") or "").strip()
        if page and page not in item["pages"]:
            item["pages"].append(page)
        item["evidence_count"] += 1
        if result.get("chunk_id") is not None:
            item["chunk_ids"].add(int(result["chunk_id"]))

    history = chunk_history_stats(
        {
            chunk_id
            for item in grouped.values()
            for chunk_id in item["chunk_ids"]
        }
    )
    total_historical_questions = retrieval_question_count()

    metadata = citation_metadata_index(
        {
            str(result.get("document_id"))
            for result in results
            if result.get("document_id")
        }
    )
    references = []
    for key, item in sorted(grouped.items(), key=lambda pair: numbers[pair[0]]):
        result = item["result"]
        document_id = str(result.get("document_id") or "")
        source = str(result.get("source") or "Unknown source")
        record = metadata["by_document_id"].get(document_id)
        if record is None:
            record = metadata["by_source"].get(source.casefold(), {})

        authors = _format_authors(record.get("authors"))
        title = str(record.get("title") or Path(source).stem).strip()
        journal = str(record.get("journal") or "").strip()
        year = str(record.get("year") or "").strip()
        doi = str(record.get("doi") or "").strip()

        parts = []
        if authors:
            parts.append(authors.rstrip("."))
        parts.append(title.rstrip("."))
        publication = ", ".join(value for value in (journal, year) if value)
        if publication:
            parts.append(publication.rstrip("."))
        if doi:
            parts.append(f"DOI: {doi}")
        citation = ". ".join(parts) + "."

        pages = sorted(item["pages"], key=_page_sort_key)
        evidence_note = [f"PDF: {source}"]
        evidence_note.append(
            "Pages: " + (", ".join(pages) if pages else "not specified")
        )
        evidence_note.append(
            f"Evidence chunks: {item['evidence_count']}"
        )
        question_uses = sum(
            int(history.get(chunk_id, {}).get("question_count", 0))
            for chunk_id in item["chunk_ids"]
        )
        citation_uses = sum(
            int(history.get(chunk_id, {}).get("citation_count", 0))
            for chunk_id in item["chunk_ids"]
        )
        citation_rate = citation_uses / question_uses if question_uses else 0.0
        question_rate_denominator = total_historical_questions * max(1, len(item["chunk_ids"]))
        question_rate = question_uses / question_rate_denominator if question_rate_denominator else 0.0
        evidence_note.append(f"Historical question hits: {question_uses}")
        evidence_note.append(f"Average chunk question-use rate: {question_rate:.1%}")
        evidence_note.append(f"Answer citation rate: {citation_rate:.0%}")
        references.append(
            f"**[{numbers[key]}]** {html.escape(citation)} "
            f"({html.escape('; '.join(evidence_note))})"
        )

    return (
        f"**{len(references)} references from {len(results)} evidence chunks**\n\n"
        + "\n\n".join(references)
    )


def retrieve_hybrid(query, retrieval_mode=None):
    """Recall globally, expand through the graph, rerank, and pack evidence."""
    mode_name, threshold = resolve_retrieval_mode(
        retrieval_mode if retrieval_mode is not None else config.get("retrieval_mode", DEFAULT_RETRIEVAL_MODE)
    )
    profile = RETRIEVAL_PROFILES.get(
        mode_name,
        RETRIEVAL_PROFILES[DEFAULT_RETRIEVAL_MODE],
    )
    active_ids = active_graph_document_ids()
    scope_chunks = count_original_chunks(active_ids)

    # Stage 1: full-corpus indexed lexical recall. There is intentionally no
    # top-k here; the relevance threshold determines how many chunks qualify.
    global_text_results = search_global(
        query,
        document_ids=active_ids,
        minimum_relevance=threshold,
    )

    # Stage 2: a bounded historical prior from similar previous questions.
    # Previously useful chunks may be recalled even when the new wording uses
    # a synonym, but history contributes at most a small part of the rank.
    priors = historical_chunk_priors(query, active_ids)
    by_chunk_id = {
        int(result["chunk_id"]): result
        for result in global_text_results
        if result.get("chunk_id") is not None
    }
    missing_history_ids = set(priors).difference(by_chunk_id)
    for result in fetch_original_chunks(missing_history_ids):
        result["lexical_relevance"] = 0.0
        result["score"] = 0.0
        result["relevance"] = 0.0
        by_chunk_id[int(result["chunk_id"])] = result
        global_text_results.append(result)

    history_promoted = 0
    for result in global_text_results:
        chunk_id = int(result.get("chunk_id") or 0)
        prior = priors.get(chunk_id, {})
        lexical = float(result.get("lexical_relevance", result.get("relevance", 0.0)))
        history_score = float(prior.get("history_score", 0.0))
        query_similarity = float(prior.get("query_similarity", 0.0))
        numeric_bonus = 2.0 if lexical > 0 and re.search(r"\d", str(result.get("text") or "")) else 0.0
        ranked = lexical + 8.0 * history_score + numeric_bonus
        if query_similarity:
            ranked = max(ranked, 75.0 * query_similarity + 10.0 * history_score)
        result["history_score"] = history_score
        result["history_question_count"] = int(prior.get("question_count", 0))
        result["history_citation_count"] = int(prior.get("citation_count", 0))
        result["relevance"] = round(min(100.0, ranked), 2)
        result["score"] = result["relevance"]
        if lexical < threshold <= result["relevance"] and history_score > 0:
            history_promoted += 1

    # Stage 3: relation-aware graph expansion. Breadth and hops grow by mode;
    # evidence count is not fixed and is governed by the shared context budget.
    graph_results = graph_evidence(
        query,
        limit=None,
        max_nodes=int(profile["graph_nodes"]),
        hops=int(profile["graph_hops"]),
    )
    graph_document_ids = {
        str(result.get("document_id"))
        for result in graph_results
        if result.get("document_id")
    }
    for result in global_text_results:
        if str(result.get("document_id") or "") in graph_document_ids:
            result["relevance"] = round(
                min(100.0, float(result.get("relevance", 0.0)) + 5.0),
                2,
            )

    eligible_text_results = [
        result
        for result in global_text_results
        if float(result.get("relevance", 0.0)) >= threshold
    ]
    graph_threshold = max(48.0, threshold * 0.72)
    eligible_graph_results = [
        result
        for result in graph_results
        if float(result.get("relevance", 0.0)) >= graph_threshold
    ]

    # Unified ranking with document round-robin prevents one long review paper
    # from consuming the complete prompt while retaining score order inside
    # every source. This limits characters, not the number of chunks searched.
    def diversify_by_document(items):
        items = sorted(
            items,
            key=lambda item: float(item.get("relevance", 0.0)),
            reverse=True,
        )
        grouped: dict[str, list[dict]] = {}
        order: list[str] = []
        for item in items:
            key = _reference_key(item)
            if key not in grouped:
                grouped[key] = []
                order.append(key)
            grouped[key].append(item)
        diversified = []
        depth = 0
        while True:
            added = False
            for key in order:
                if depth < len(grouped[key]):
                    diversified.append(grouped[key][depth])
                    added = True
            if not added:
                return diversified
            depth += 1

    text_order = diversify_by_document(eligible_text_results)
    graph_order = diversify_by_document(eligible_graph_results)
    ordered: list[dict] = []
    text_index = graph_index = 0
    # Preserve a meaningful graph share: two exact page chunks followed by one
    # relation item. Either side can continue alone when the other is exhausted.
    while text_index < len(text_order) or graph_index < len(graph_order):
        for _ in range(2):
            if text_index < len(text_order):
                ordered.append(text_order[text_index])
                text_index += 1
        if graph_index < len(graph_order):
            ordered.append(graph_order[graph_index])
            graph_index += 1

    combined: list[dict] = []
    seen = set()
    configured_standard_budget = max(
        10_000,
        min(int(config.get("retrieval_context_char_budget", 60_000)), 500_000),
    )
    budget_scale = configured_standard_budget / 60_000
    character_budget = max(
        10_000,
        min(int(float(profile["context_budget"]) * budget_scale), 500_000),
    )
    used_characters = 0
    budget_limited = False
    for result in ordered:
        marker = (
            result.get("source"),
            str(result.get("page") or ""),
            str(result.get("text") or "").strip(),
        )
        if marker in seen:
            continue
        evidence_size = len(str(result.get("text") or "")) + len(str(result.get("source") or "")) + 120
        if combined and used_characters + evidence_size > character_budget:
            budget_limited = True
            continue
        seen.add(marker)
        combined.append(result)
        used_characters += evidence_size

    selected_text = [result for result in combined if result.get("kind") != "graph_evidence"]
    selected_graph = [result for result in combined if result.get("kind") == "graph_evidence"]
    represented_documents = {
        str(result.get("document_id") or result.get("source") or "")
        for result in combined
        if result.get("document_id") or result.get("source")
    }
    stats = {
        "scope_chunks": scope_chunks,
        "positive_chunks": len(global_text_results),
        "threshold_chunks": len(eligible_text_results),
        "graph_candidates": len(eligible_graph_results),
        "history_promoted_chunks": history_promoted,
        "selected_text_chunks": len(selected_text),
        "selected_graph_items": len(selected_graph),
        "total_evidence": len(combined),
        "documents": len(represented_documents),
        "mode": mode_name,
        "threshold": threshold,
        "context_limited": budget_limited,
        "character_budget": character_budget,
    }
    return combined, stats


def format_retrieval_status(stats):
    if not stats:
        return "No retrieval has run for the current answer."
    context_note = (
        " Context capacity limited the final evidence set."
        if stats.get("context_limited")
        else ""
    )
    return (
        f"**Evidence used: {stats['total_evidence']}** "
        f"({stats['selected_text_chunks']} text chunks + "
        f"{stats['selected_graph_items']} graph relations) from "
        f"{stats['documents']} documents. Global search scanned "
        f"{stats['scope_chunks']} active chunks; {stats['threshold_chunks']} passed "
        f"the {stats['mode']} threshold (≥{stats['threshold'] / 100:g}).{context_note}"
    )

def format_retrieval_status(stats):
    """Summarize the completed retrieval without exposing internal tracing."""
    if not stats:
        return "No retrieval has run for the current answer."
    context_note = (
        " Context capacity limited the final evidence set."
        if stats.get("context_limited")
        else ""
    )
    citation_note = ""
    if stats.get("reference_documents") is not None:
        citation_note = (
            f" Answer citations: {stats.get('cited_documents', 0)}/"
            f"{stats['reference_documents']} retrieved references."
        )
    return (
        f"**Evidence used: {stats['total_evidence']}** "
        f"({stats['selected_text_chunks']} text chunks + "
        f"{stats['selected_graph_items']} graph relations) from "
        f"{stats['documents']} documents. The indexed global search covered "
        f"{stats['scope_chunks']} active chunks; {stats['threshold_chunks']} text chunks "
        f"passed the {stats['mode']} threshold (≥ {stats['threshold'] / 100:g}). "
        f"Historical retrieval promoted {stats.get('history_promoted_chunks', 0)} chunks."
        f"{citation_note}{context_note}"
    )


def _cited_document_ids(answer, results):
    """Map model reference numbers back to GraphRAG document IDs."""
    cited_numbers = _cited_reference_numbers(answer)
    numbers = _reference_numbers(results)
    cited_ids = set()
    for result in results:
        if numbers.get(_reference_key(result)) not in cited_numbers:
            continue
        document_id = str(result.get("document_id") or "")
        if document_id:
            cited_ids.add(document_id)
    return cited_ids


def ask_bot(prompt, history_messages, retrieval_mode=None):
    """Retrieve local evidence and optionally ask an OpenAI-compatible model."""
    try:
        if is_greeting_only(prompt):
            return (
                greeting_response(prompt),
                "No references retrieved for a conversational greeting.",
                "Conversational greeting detected; global retrieval was not needed.",
            )
        results, retrieval_stats = retrieve_hybrid(prompt, retrieval_mode)
        retrieval_status = format_retrieval_status(retrieval_stats)
        if not results:
            return "No relevant answer was found in the knowledge base!", "No references retrieved.", retrieval_status

        retrieval_stats["reference_documents"] = len(_reference_numbers(results))
        retrieval_stats["cited_documents"] = 0
        retrieval_status = format_retrieval_status(retrieval_stats)
        sources = format_sources(results)
        if client is None:
            mode_name, _ = resolve_retrieval_mode(retrieval_mode)
            record_retrieval_feedback(prompt, mode_name, results, set())
            source_list = format_reference_list(results)
            return "No generation model is configured.", source_list, retrieval_status

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for msg in history_messages[-8:]:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            if role not in ("user", "assistant"):
                continue
            messages.append({"role": role, "content": content})
        coverage_instruction = _citation_coverage_instruction(results)
        messages.append({
            "role": "user",
            "content": (
                f"Reference material:\n\n{sources}\n\nUser question: {prompt}\n\n"
                f"{coverage_instruction}"
            ),
        })

        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=False,
            max_tokens=config.get("max_tokens", 4000),
            extra_body={"thinking": {"type": "disabled"}},
        )
        answer = normalize_numeric_ranges(completion.choices[0].message.content)
        required_numbers = set(_reference_numbers(results).values())
        missing_numbers = sorted(required_numbers - _cited_reference_numbers(answer))
        if missing_numbers:
            missing_labels = ", ".join(f"[{number}]" for number in missing_numbers)
            revision_messages = messages + [
                {"role": "assistant", "content": answer},
                {
                    "role": "user",
                    "content": (
                        "Revise the complete answer so every retrieved reference is attached "
                        "to a statement it genuinely supports. The draft omitted these required "
                        f"references: {missing_labels}. Return only the complete revised answer. "
                        f"{coverage_instruction}"
                    ),
                },
            ]
            revision = client.chat.completions.create(
                model=model,
                messages=revision_messages,
                stream=False,
                max_tokens=config.get("max_tokens", 4000),
                extra_body={"thinking": {"type": "disabled"}},
            )
            answer = normalize_numeric_ranges(revision.choices[0].message.content)

        cited_numbers = _cited_reference_numbers(answer)
        still_missing = sorted(required_numbers - cited_numbers)
        if still_missing:
            missing_labels = " ".join(f"[{number}]" for number in still_missing)
            answer += (
                "\n\n**Retrieved references not separately expanded in the generated answer:** "
                + missing_labels
            )
            cited_numbers.update(still_missing)
        retrieval_stats["cited_documents"] = len(cited_numbers & required_numbers)
        retrieval_status = format_retrieval_status(retrieval_stats)
        mode_name, _ = resolve_retrieval_mode(retrieval_mode)
        record_retrieval_feedback(
            prompt,
            mode_name,
            results,
            _cited_document_ids(answer, results),
        )
        source_list = format_reference_list(results)
        return answer, source_list, retrieval_status

    except Exception as e:
        return (
            f"Question answering failed: {str(e)}",
            "No references available.",
            "Retrieval failed before an evidence count could be produced.",
        )


def normalize_numeric_ranges(content):
    """Prevent Markdown from rendering numeric range tildes as strikethrough."""
    return re.sub(
        r"(?<=[\d%‰℃°])\s*[~～]{1,2}\s*(?=[+-]?\d)",
        "–",
        str(content or ""),
    )


def strip_legacy_embedded_sources(content):
    """Clean assistant text saved by earlier UI implementations."""
    cleaned = re.sub(
        r"\s*<details><summary>Retrieved sources \(\d+\)</summary>.*?</details>\s*$",
        "",
        str(content or ""),
        flags=re.DOTALL | re.IGNORECASE,
    ).rstrip()
    return normalize_numeric_ranges(cleaned)


def repair_legacy_mojibake(content):
    """Repair common GBK/UTF-8 decoding mistakes in older saved chats."""
    text = str(content or "")
    suspicious = set("ÄãºÃ£¡ÎÒËÊ½µ浣犲ソ")

    def quality(value):
        cjk = len(re.findall(r"[\u3400-\u9fff]", value))
        noise = sum(value.count(marker) for marker in suspicious)
        replacements = value.count("�")
        return 2 * cjk - 3 * noise - 10 * replacements

    candidates = [text]
    for source_encoding, target_encoding in (
        ("latin1", "gb18030"),
        ("gb18030", "utf-8"),
        ("latin1", "utf-8"),
    ):
        try:
            candidates.append(text.encode(source_encoding).decode(target_encoding))
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass
    best = max(candidates, key=quality)
    return best if quality(best) > quality(text) else text


def first_user_question(messages):
    """Return the first real user turn, never an assistant/loading message."""
    for message in messages or []:
        if not isinstance(message, dict) or message.get("role") != "user":
            continue
        content = repair_legacy_mojibake(message.get("content"))
        content = re.sub(r"\s+", " ", str(content)).strip()
        if content:
            return content
    return "Empty chat"

def _history_directory(request: gr.Request | None = None) -> str:
    """Return a private history folder for the authenticated public user."""
    if PUBLIC_MODE:
        username = ((getattr(request, "username", "") if request else "") or "").strip()
        safe_username = re.sub(r"[^A-Za-z0-9_.-]+", "_", username).strip("._")
        if not safe_username:
            # Never expose the shared/local history when a public identity is missing.
            safe_username = "_unidentified"
        return os.path.join(HISTORY_DIR, "users", safe_username)
    return HISTORY_DIR


def save_chat(session_id, messages, request: gr.Request | None = None):
    """Save chat history to file"""
    history_directory = _history_directory(request)
    os.makedirs(history_directory, exist_ok=True)
    filepath = os.path.join(history_directory, f"{session_id}.json")
    created_at = datetime.now().isoformat()
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as existing_file:
                created_at = json.load(existing_file).get("created_at") or created_at
        except (OSError, ValueError, TypeError):
            pass
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump({
            "session_id": session_id,
            "messages": messages,
            "title": first_user_question(messages),
            "created_at": created_at,
            "updated_at": datetime.now().isoformat(),
        }, f, ensure_ascii=False, indent=2)

def load_chat(session_id, request: gr.Request | None = None):
    """Load chat history"""
    filepath = os.path.join(_history_directory(request), f"{session_id}.json")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            messages = data.get("messages", [])
            # Migrate old tuple-format messages to dict format
            migrated = []
            for msg in messages:
                if isinstance(msg, dict):
                    copied = dict(msg)
                    copied["content"] = repair_legacy_mojibake(copied.get("content"))
                    if copied.get("role") == "assistant":
                        copied["content"] = strip_legacy_embedded_sources(copied.get("content"))
                    migrated.append(copied)
                elif isinstance(msg, (list, tuple)) and len(msg) == 2:
                    migrated.append({"role": "user", "content": str(msg[0])})
                    if msg[1]:
                        migrated.append({
                            "role": "assistant",
                            "content": strip_legacy_embedded_sources(msg[1]),
                        })
            return migrated
    return []

def get_chat_list(request: gr.Request | None = None):
    """Get all historical chat sessions"""
    history_directory = _history_directory(request)
    if not os.path.exists(history_directory):
        return []
    files = []
    for f in os.listdir(history_directory):
        if f.endswith('.json'):
            filepath = os.path.join(history_directory, f)
            mtime = datetime.fromtimestamp(os.path.getmtime(filepath))
            messages = load_chat(f[:-5], request)
            question = first_user_question(messages)
            preview = question if len(question) <= 80 else question[:77].rstrip() + "..."
            files.append({
                "name": f"{preview}",
                "date": mtime.strftime("%Y-%m-%d %H:%M"),
                "session_id": f[:-5],
                "mtime": os.path.getmtime(filepath),
            })
    # Use the precise timestamp plus session ID. Sorting only by the displayed
    # minute could reorder same-minute rows between drawing and clicking, which
    # loaded a different conversation than the title the user selected.
    files.sort(key=lambda x: (x["mtime"], x["session_id"]), reverse=True)
    return files

def new_chat():
    """Create new chat"""
    return (
        [],
        str(uuid.uuid4()),
        "No references for the current chat.",
        gr.update(open=False),
        "No retrieval has run for the current answer.",
    )

def switch_chat(session_id, current_history):
    """Switch to specified history session"""
    if not session_id:
        return [], str(uuid.uuid4())
    messages = load_chat(session_id)
    for msg in messages:
        if msg.get("role") == "user":
            msg["name"] = "User"
        elif msg.get("role") == "assistant":
            msg["name"] = "Chatbot"
    return messages, session_id

def delete_chat(session_id):
    """Delete specified session"""
    filepath = os.path.join(HISTORY_DIR, f"{session_id}.json")
    if os.path.exists(filepath):
        os.remove(filepath)

def clear_all_history(request: gr.Request | None = None):
    """Clear all history"""
    history_directory = _history_directory(request)
    if os.path.exists(history_directory):
        for f in os.listdir(history_directory):
            if f.endswith('.json'):
                os.remove(os.path.join(history_directory, f))
    return (
        [],
        str(uuid.uuid4()),
        "No references for the current chat.",
        gr.update(open=False),
        "No retrieval has run for the current answer.",
    )

def select_history_item(session_id):
    """Load session when history item is clicked"""
    if session_id:
        messages = load_chat(session_id)
        for msg in messages:
            if msg.get("role") == "user":
                msg["name"] = "User"
            elif msg.get("role") == "assistant":
                msg["name"] = "Chatbot"
        return messages, session_id
    return [], str(uuid.uuid4())

def load_history(request: gr.Request | None = None):
    """Load chat history list"""
    files = get_chat_list(request)
    return [[f"{item['name']} ({item['date']})"] for item in files]

def get_model_display_name():
    # Get model display name
    return str(config.get("model_display_name") or model) if client else "Local BM25 Retrieval"


def render_parsed_corpus_stats():
    stats = parsed_corpus_stats()
    cards = (
        ("Chinese Papers", stats["chinese_papers"]),
        ("English Papers", stats["english_papers"]),
        ("Patents", stats["patents"]),
        ("Searchable Chunks", stats["chunks"]),
        ("Relations", stats["relations"]),
        ("Extracted Alloys", stats["alloys"]),
    )
    card_html = "".join(
        f"<div class='corpus-stat-card'><strong>{value:,}</strong><span>{label}</span></div>"
        for label, value in cards
    )
    return (
        "<section class='corpus-overview'>"
        "<h3>Parsed Corpus</h3>"
        f"<p>{stats['papers']:,} completed GraphRAG documents</p>"
        f"<div class='corpus-stat-grid'>{card_html}</div>"
        "</section>"
    )


def render_knowledge_graph(query, max_nodes, hops):
    """Refresh the bounded interactive graph shown in the UI."""
    graph_html, matched_rows, relation_rows, status = make_graph_html(
        (query or "").strip(),
        max_nodes=int(max_nodes or 60),
        hops=int(hops or 1),
    )
    stats = graph_stats()
    summary = (
        f"{status}\n\nGraph database: {stats['papers']} papers, {stats['nodes']} nodes, "
        f"{stats['edges']} relations, {stats['fabrication_processes']} fabrication-process nodes, "
        f"{stats['post_treatments']} post-treatment nodes, and "
        f"{stats['observations']} property nodes. The canvas is a bounded, type-balanced view; "
        "Graph Search can isolate all matching heat-treatment or property neighborhoods."
    )
    return graph_html, matched_rows, relation_rows, summary


def update_graph_slider_limits(node_upper, hop_upper, current_nodes, current_hops):
    """Update both slider ranges while retaining valid current selections."""
    node_limit = _positive_integer(node_upper, GRAPH_NODE_SLIDER_MAX, 10)
    hop_limit = _positive_integer(hop_upper, GRAPH_HOP_SLIDER_MAX, 1)
    node_value = min(_positive_integer(current_nodes, GRAPH_NODE_DEFAULT, 10), node_limit)
    hop_value = min(_positive_integer(current_hops, GRAPH_HOP_DEFAULT, 1), hop_limit)
    return (
        gr.update(maximum=node_limit, value=node_value),
        gr.update(maximum=hop_limit, value=hop_value),
    )

# ======================== Gradio UI ========================
css = """
/* Container */
.gradio-container {
    font-family: 'Segoe UI', -apple-system, sans-serif !important;
}

/* Hide scrollbars globally */
* {
    scrollbar-width: none !important;
    -ms-overflow-style: none !important;
}
*::-webkit-scrollbar {
    display: none !important;
}

/* Title area */
.title-header {
    text-align: center;
    padding: 20px 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    margin: -20px -20px 20px -20px;
    border-radius: 0 0 20px 20px;
}

.title-header h1 {
    color: white !important;
    font-size: 2em !important;
    font-weight: 600 !important;
    margin: 0 !important;
    letter-spacing: 1px;
}

.title-header p {
    color: rgba(255,255,255,0.9) !important;
    font-size: 0.9em !important;
    margin: 8px 0 0 0 !important;
}

/* Sidebar */
#chatbot {
    height: 450px;
}

.sidebar {
    background: #f8f9fa;
    border-radius: 12px;
    padding: 15px;
    height: 100%;
}

.sidebar-btn {
    width: 100%;
    margin-bottom: 8px;
    border-radius: 8px !important;
    transition: all 0.2s;
}

.sidebar-btn:hover {
    transform: translateX(5px);
}

.new-chat-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
    font-weight: 500;
}

.clear-btn {
    background: #ff4757 !important;
    color: white !important;
    border: none !important;
}

.history-item {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 10px 12px;
    margin-bottom: 6px;
    cursor: pointer;
    transition: all 0.2s;
}

.history-item:hover {
    border-color: #667eea;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.2);
}

.history-item .session-title {
    font-size: 0.85em;
    font-weight: 500;
    color: #333;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.history-item .session-date {
    font-size: 0.75em;
    color: #999;
    margin-top: 4px;
}

/* Chat area */
.chat-container {
    background: white;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    padding: 20px;
    height: 100%;
}

/* Chat messages */
.user-message {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 18px 18px 4px 18px;
    padding: 12px 16px;
    max-width: 75%;
    margin-left: auto;
    font-size: 0.95em;
    line-height: 1.5;
}

.bot-message {
    background: #ffffff;
    color: #333;
    border-radius: 18px 18px 18px 4px;
    padding: 12px 16px;
    max-width: 75%;
    font-size: 0.95em;
    line-height: 1.5;
}

/* Avatar image size override */
#chatbot .avatar-container,
#chatbot picture,
.grado-avatar,
.gradio-container img.avatar,
img.avatar {
    width: 52px !important;
    height: 52px !important;
    min-width: 52px !important;
    min-height: 52px !important;
    border-radius: 50% !important;
    overflow: hidden !important;
}

/* Avatar image overrides */
#chatbot .avatar-container img,
#chatbot picture img,
.svelte-vlp1qv img,
.gradio-container img.avatar,
img.avatar {
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    object-position: center !important;
    border-radius: 50% !important;
}
.message.svelte-vlp1qv[data-testid="user"] > .avatar {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}
.message.svelte-vlp1qv[data-testid="bot"] > .avatar {
    background: transparent !important;
    color: #333;
}

/* Keep assistant rows and the chatbot GIF on the white chat background. */
#chatbot .message.bot,
#chatbot [data-testid="bot"],
#chatbot [data-testid="bot"] > .message,
#chatbot [data-testid="bot"] .message-content,
#chatbot [data-testid="bot"] .bubble-wrap {
    background: #ffffff !important;
}
#chatbot [data-testid="bot"] img {
    filter: none !important;
    opacity: 1 !important;
}

/* Three colorful dots float in sequence beside the original chatbot GIF. */
#chatbot .answer-loading-dots {
    display: inline-flex;
    align-items: center;
    justify-content: flex-start;
    gap: 6px;
    height: 30px;
    padding: 2px 5px;
    vertical-align: middle;
}
#chatbot .answer-loading-dots i {
    display: block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea 0%, #7c3aed 100%);
    box-shadow: 0 2px 7px rgba(102, 126, 234, 0.28);
    animation: answer-dot-float 1.15s cubic-bezier(.45, 0, .25, 1) infinite;
    will-change: transform, opacity;
}
#chatbot .answer-loading-dots i:nth-child(2) {
    animation-delay: .15s;
    background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
}
#chatbot .answer-loading-dots i:nth-child(3) {
    animation-delay: .30s;
    background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
}
@keyframes answer-dot-float {
    0%, 65%, 100% {
        transform: translateY(3px) scale(.82);
        opacity: .42;
    }
    32% {
        transform: translateY(-6px) scale(1.08);
        opacity: 1;
    }
}
@media (prefers-reduced-motion: reduce) {
    #chatbot .answer-loading-dots i {
        animation-duration: 1.8s;
        transform: none;
    }
}

/* Input area */
.input-area {
    margin-top: 20px;
}

.input-row {
    display: flex !important;
    gap: 12px;
    flex-wrap: nowrap !important;
    align-items: center;
    width: 100%;
}

#message {
    flex: 5 !important;
    min-width: 0;
    border-radius: 24px !important;
    border: 2px solid #e0e0e0 !important;
    padding: 14px 20px !important;
    font-size: 1em !important;
    transition: all 0.2s;
}

#submit {
    flex: 0 0 auto !important;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 24px !important;
    padding: 12px 28px !important;
    font-weight: 500 !important;
    transition: all 0.2s;
}

#message:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.15) !important;
}

#submit:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
}

/* Model info */
.model-info {
    text-align: center;
    padding: 12px;
    background: #f8f9fa;
    border-radius: 10px;
    margin-bottom: 15px;
    font-size: 0.85em;
    color: #666;
}

/* Chat history list */
.chat-history-item {
    background: white;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 10px 12px;
    margin-bottom: 6px;
    cursor: pointer;
    transition: all 0.2s;
    position: relative;
}

.chat-history-item:hover {
    border-color: #667eea;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.2);
}

.chat-history-item.selected {
    border-color: #667eea;
    background: #f0f1ff;
}

.chat-history-item .session-title {
    font-size: 0.85em;
    font-weight: 500;
    color: #333;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    padding-right: 30px;
}

.chat-history-item .session-date {
    font-size: 0.75em;
    color: #999;
    margin-top: 4px;
}

.chat-history-item .delete-btn {
    position: absolute;
    top: 8px;
    right: 8px;
    background: #ff4757;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 0.75em;
    padding: 2px 8px;
    cursor: pointer;
    opacity: 0;
    transition: opacity 0.2s;
}

.chat-history-item:hover .delete-btn {
    opacity: 1;
}

/* Hide default Gradio elements */
footer {
    display: none !important;
}

/* Obsidian-inspired graph canvas */
#knowledge-graph {
    overflow: hidden;
    border: 1px solid #2b2f39;
    border-radius: 14px;
    background: #111318;
    box-shadow: 0 16px 38px rgba(17, 19, 24, 0.18);
}

.graph-help {
    color: #6b7280;
    font-size: 0.9rem;
}

.corpus-overview {
    padding: 14px;
    border: 1px solid #e1e4ea;
    border-radius: 12px;
    background: rgba(255,255,255,.72);
}
.corpus-overview h3 { margin: 0; font-size: 1rem; color: #303545; }
.corpus-overview > p { margin: 4px 0 12px; color: #73798a; font-size: .82rem; }
.corpus-stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.corpus-stat-card {
    min-height: 68px;
    padding: 10px;
    box-sizing: border-box;
    border: 1px solid #e3e6ed;
    border-radius: 10px;
    background: #f8f9fc;
}
.corpus-stat-card strong { display: block; color: #5b4fc4; font-size: 1.25rem; line-height: 1.2; }
.corpus-stat-card span { display: block; margin-top: 4px; color: #666d7d; font-size: .75rem; line-height: 1.25; }
#retrieved-sources { margin-top: 8px; }

.public-session-bar {
    display: flex;
    justify-content: flex-end;
    margin: 0 0 8px;
}
.public-session-bar form { margin: 0; }
.public-signout {
    border: 1px solid #d9dce6;
    border-radius: 9px;
    padding: 7px 13px;
    color: #555d70;
    background: rgba(255,255,255,.85);
    font: inherit;
    font-size: .82rem;
    font-weight: 650;
    cursor: pointer;
}
.public-signout:hover { border-color: #8b5cf6; color: #6d5ce7; }

"""

with gr.Blocks(css=css, theme=gr.themes.Soft()) as demo:
    session_id = gr.State(value=str(uuid.uuid4()))

    if PUBLIC_MODE:
        gr.HTML(
            '<div class="public-session-bar"><form method="post" action="/auth/logout">'
            '<button class="public-signout" type="submit">Sign Out</button>'
            '</form></div>'
        )

    with gr.Row():
        with gr.Column(scale=2):
                # Main chat area
                with gr.Column(elem_classes="chat-container"):
                    gr.HTML("""
                    <div class="title-header">
                        <h1>Knowledge Mining</h1>
                        <p>Intelligent Knowledge Mining & Q&A System</p>
                    </div>
                    """)

                    chatbot = gr.Chatbot(
                        type='messages',
                        allow_tags=False,
                        show_label=False,
                        avatar_images=("user.jpg", "chatbot.gif"),
                        elem_id="chatbot",
                        min_height=600,
                    )

                    with gr.Row(elem_classes="input-row"):
                        message = gr.Textbox(
                            placeholder="Ask a question and start chatting...",
                            scale=5,
                            autofocus=True,
                            lines=1,
                            container=False,
                            elem_id="message",
                        )
                        submit = gr.Button("Send", scale=1, variant="primary", elem_id="submit")

                    model_info = gr.Markdown(
                        f"**Model:** `{get_model_display_name()}`",
                        elem_classes="model-info",
                    )
                    retrieval_status = gr.Markdown(
                        "No retrieval has run for the current answer.",
                        elem_classes="model-info",
                        visible=False,
                    )
                    with gr.Accordion(
                        "References",
                        open=False,
                        elem_id="retrieved-sources",
                    ) as sources_accordion:
                        retrieved_sources = gr.Markdown("No references for the current chat.")

        with gr.Column(scale=1, min_width=220):
            # Sidebar
            with gr.Column(elem_classes="sidebar"):
                new_btn = gr.Button("+ New Chat", elem_classes="sidebar-btn new-chat-btn")
                clear_all_btn = gr.Button(
                    "Clear All History",
                    elem_classes="sidebar-btn clear-btn",
                    visible=True,
                )

                gr.HTML(
                    "<hr style='margin: 15px 0; border: none; border-top: 1px solid #e0e0e0;'>",
                    visible=True,
                )
                gr.HTML(
                    "<p style='font-size: 0.85em; color: #666; margin-bottom: 10px;'>📁 Chat History</p>",
                    visible=True,
                )

                # Hidden field to store selected session_id
                selected_session = gr.Textbox(visible=False, value="")

                # Chat history list (clickable)
                chat_list = gr.Dataframe(
                    headers=["Session"],
                    datatype=["str"],
                    interactive=False,
                    elem_id="chat-list",
                    visible=True,
                )

                # Delete selected session button
                delete_btn = gr.Button(
                    "Delete Selected",
                    elem_classes="sidebar-btn",
                    variant="stop",
                    visible=True,
                )

                corpus_stats_panel = gr.HTML(render_parsed_corpus_stats())
                retrieval_mode = gr.Radio(
                    choices=list(RETRIEVAL_MODES),
                    value=config.get("retrieval_mode", DEFAULT_RETRIEVAL_MODE),
                    label="Retrieval Mode",
                )
                gr.Markdown(
                    "Every mode scans all chunks in the active GraphRAG corpus. Targeted uses the strictest relevance "
                    "threshold; Full Knowledge Base uses the broadest, subject to the model-context safety budget.",
                    elem_classes="graph-help",
                )

    with gr.Accordion("Interactive Knowledge Graph (GraphRAG)", open=True):
        gr.Markdown(
            "Explore literature relationships in an Obsidian-style graph. Drag nodes to rearrange the layout; "
            "click a node to focus on its neighbors, double-click to zoom in, or click empty space to reset. "
            "Switch among Core, All, and Hidden label modes; search within the graph, toggle entity types, "
            "and zoom or pan with the toolbar or mouse wheel. In 3D, highly connected nodes gravitate toward "
            "the center while low-degree nodes occupy outer layers. Click a node or relation to inspect source evidence.",
            elem_classes="graph-help",
        )
        with gr.Row():
            graph_query = gr.Textbox(
                label="Graph Search",
                placeholder="For example: Nb-W ZrC high-temperature strength, or LPBF cracking",
                scale=5,
            )
            graph_search_btn = gr.Button("Search and Draw", variant="primary", scale=1)
        with gr.Row():
            graph_max_nodes = gr.Slider(
                minimum=10,
                maximum=GRAPH_NODE_SLIDER_MAX,
                value=GRAPH_NODE_DEFAULT,
                step=10,
                label="Maximum Nodes",
                info="Maximum number of nodes drawn in the current graph.",
                scale=5,
            )
            graph_node_upper = gr.Number(
                value=GRAPH_NODE_SLIDER_MAX,
                minimum=10,
                step=10,
                precision=0,
                label="Upper Limit",
                info="Maximum Nodes slider range.",
                scale=1,
                min_width=140,
            )
        with gr.Row():
            graph_hops = gr.Slider(
                minimum=1,
                maximum=GRAPH_HOP_SLIDER_MAX,
                value=GRAPH_HOP_DEFAULT,
                step=1,
                label="Relationship Hops",
                info="Number of relationship layers expanded from directly matched nodes.",
                scale=5,
            )
            graph_hop_upper = gr.Number(
                value=GRAPH_HOP_SLIDER_MAX,
                minimum=1,
                step=1,
                precision=0,
                label="Upper Limit",
                info="Relationship Hops slider range.",
                scale=1,
                min_width=140,
            )
        initial_graph, initial_matches, initial_edges, initial_graph_status = render_knowledge_graph(
            "", GRAPH_NODE_DEFAULT, GRAPH_HOP_DEFAULT
        )
        graph_status = gr.Markdown(initial_graph_status)
        with gr.Accordion("Matched Nodes", open=True):
            graph_matches = gr.Dataframe(
                value=initial_matches,
                headers=["Node", "Entity Type", "Connections", "Alloy System", "Material State"],
                datatype=["str", "str", "number", "str", "str"],
                interactive=False,
                wrap=True,
                label="Nodes Directly Matched by Graph Search",
            )
        graph_view = gr.HTML(
            initial_graph,
            container=False,
            elem_id="knowledge-graph",
        )
        with gr.Accordion("Relations and Source Evidence", open=False):
            graph_edges = gr.Dataframe(
                value=initial_edges,
                headers=["Source", "Relation", "Target", "Evidence Level", "Source Evidence"],
                datatype=["str", "str", "str", "str", "str"],
                interactive=False,
                wrap=True,
                label="Current Graph Relations and Evidence",
            )

    # ==================== Event Bindings ===================

    # Step 1: Add user message immediately, clear input
    def on_submit(inputs, history, session_id, request: gr.Request):
        if not inputs or not inputs.strip():
            return history, "", session_id, load_history(request)
        history = history or []
        saved_history = history + [
            {"role": "user", "content": inputs.strip(), "name": "User"},
        ]
        # Save the real user turn immediately. In public mode the request
        # identity routes it to that account's private history folder.
        save_chat(session_id, saved_history, request)
        display_history = saved_history + [
            {
                "role": "assistant",
                # A plain HTML string survives Gradio's message
                # serialization and gives the response callback a stable
                # fallback marker if metadata is normalized to None.
                "content": LOADING_DOTS_HTML,
                "metadata": {"id": LOADING_MESSAGE_ID},
                "name": "Chatbot",
            },
        ]
        return display_history, "", session_id, load_history(request)

    # Step 2: Call API and add bot response (chained after step 1)
    def on_bot_response(history, session_id, selected_retrieval_mode, request: gr.Request):
        history = history or []
        has_loading_row = bool(history and is_loading_message(history[-1]))
        answer_history = history[:-1] if has_loading_row else history
        user_input = (
            answer_history[-1]["content"]
            if answer_history and answer_history[-1].get("role") == "user"
            else ""
        )
        if not user_input:
            return (
                answer_history,
                session_id,
                "No references for the current chat.",
                gr.update(open=False),
                "No retrieval has run for the current answer.",
            )
        response, source_list, evidence_status = ask_bot(
            user_input,
            answer_history[:-1],
            selected_retrieval_mode,
        )
        history = answer_history + [{"role": "assistant", "content": response, "name": "Chatbot"}]
        save_chat(session_id, history, request)
        return (
            history,
            session_id,
            source_list,
            gr.update(open=False),
            evidence_status,
        )

    submit.click(
        on_submit,
        [message, chatbot, session_id],
        [chatbot, message, session_id, chat_list],
        show_progress="hidden",
    ).then(
        on_bot_response,
        [chatbot, session_id, retrieval_mode],
        [chatbot, session_id, retrieved_sources, sources_accordion, retrieval_status],
        show_progress="hidden",
    )
    message.submit(
        on_submit,
        [message, chatbot, session_id],
        [chatbot, message, session_id, chat_list],
        show_progress="hidden",
    ).then(
        on_bot_response,
        [chatbot, session_id, retrieval_mode],
        [chatbot, session_id, retrieved_sources, sources_accordion, retrieval_status],
        show_progress="hidden",
    )

    graph_search_btn.click(
        render_knowledge_graph,
        inputs=[graph_query, graph_max_nodes, graph_hops],
        outputs=[graph_view, graph_matches, graph_edges, graph_status],
        show_progress="hidden",
    )
    graph_query.submit(
        render_knowledge_graph,
        inputs=[graph_query, graph_max_nodes, graph_hops],
        outputs=[graph_view, graph_matches, graph_edges, graph_status],
        show_progress="hidden",
    )
    graph_node_upper.change(
        update_graph_slider_limits,
        inputs=[graph_node_upper, graph_hop_upper, graph_max_nodes, graph_hops],
        outputs=[graph_max_nodes, graph_hops],
    )
    graph_hop_upper.change(
        update_graph_slider_limits,
        inputs=[graph_node_upper, graph_hop_upper, graph_max_nodes, graph_hops],
        outputs=[graph_max_nodes, graph_hops],
    )

    # New chat
    new_btn.click(
        new_chat,
        outputs=[chatbot, session_id, retrieved_sources, sources_accordion, retrieval_status],
    )

    # Clear all history
    clear_all_btn.click(
        clear_all_history,
        outputs=[chatbot, session_id, retrieved_sources, sources_accordion, retrieval_status]
    ).then(load_history, outputs=[chat_list])

    # Click history → switch session + update selected_session
    def handle_select(evt: gr.SelectData, current_chat, current_session, request: gr.Request):
        """Load session for clicked row and record selected ID"""
        files = get_chat_list(request)
        row = evt.index[0] if isinstance(evt.index, (list, tuple)) else evt.index
        if row < len(files):
            item = files[row]
            messages = load_chat(item["session_id"], request)
            for msg in messages:
                if msg.get("role") == "user":
                    msg["name"] = "User"
                elif msg.get("role") == "assistant":
                    msg["name"] = "Chatbot"
            return (
                messages,
                item["session_id"],
                item["session_id"],
                "Sources are shown for new answers only.",
                gr.update(open=False),
                "Retrieval details are shown for new answers only.",
            )
        return (
            current_chat,
            current_session,
            None,
            "No references for the current chat.",
            gr.update(open=False),
            "No retrieval has run for the current answer.",
        )

    chat_list.select(
        handle_select,
        [chatbot, session_id],
        [
            chatbot,
            session_id,
            selected_session,
            retrieved_sources,
            sources_accordion,
            retrieval_status,
        ]
    )

    # Delete button → read selected_session, delete file, refresh list
    def do_delete(sid, request: gr.Request):
        if sid:
            filepath = os.path.join(_history_directory(request), f"{sid}.json")
            if os.path.exists(filepath):
                os.remove(filepath)
        return ""

    delete_btn.click(
        do_delete,
        [selected_session],
        [selected_session]
    ).then(
        load_history,
        outputs=[chat_list]
    )

    # Load history list on page load
    demo.load(load_history, outputs=[chat_list])
    demo.load(render_parsed_corpus_stats, outputs=[corpus_stats_panel])
    if PUBLIC_MODE:
        demo.load(record_public_registration, show_progress="hidden")
        public_presence_timer = gr.Timer(value=20, active=True)
        public_presence_timer.tick(
            refresh_public_presence,
            show_progress="hidden",
            queue=False,
            show_api=False,
        )

if __name__ == "__main__":
    demo.queue(default_concurrency_limit=4)
    demo.launch(
        debug=False,
        show_api=False,
        # Leave the port unset for local launches so Gradio can fall back to
        # 7861, 7862, ... when an older app instance already owns port 7860.
        # Public launchers set GRADIO_SERVER_PORT explicitly and keep their
        # tunnel bound to that exact port.
        server_port=(
            int(os.environ["GRADIO_SERVER_PORT"])
            if os.getenv("GRADIO_SERVER_PORT")
            else None
        ),
        share=SHARE_PUBLICLY,
        auth=LAUNCH_AUTH,
        auth_message=AUTH_MESSAGE,
        quiet=PUBLIC_MODE and not SHARE_PUBLICLY,
    )
