"""Local evidence-grounded graph store and visualization helpers."""

from __future__ import annotations

import hashlib
import html as html_lib
import json
import re
import sqlite3
import threading
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


BASE_DIR = Path(__file__).resolve().parent
GRAPH_DIR = BASE_DIR / "data" / "graph"
GRAPH_RAW_DIR = GRAPH_DIR / "chunk_extractions"
GRAPH_PAPERS_DIR = GRAPH_DIR / "paper_graphs"
GRAPH_FAILED_DIR = GRAPH_DIR / "failed"
GRAPH_DB_PATH = GRAPH_DIR / "graph.db"
GRAPH_REPORTS_DIR = BASE_DIR / "reports"
LITERATURE_DB_PATH = BASE_DIR / "data" / "index" / "literature.db"
STRUCTURED_DIR = BASE_DIR / "data" / "structured"
_LOCK = threading.RLock()

QUERY_SYNONYMS = {
    "合金": "alloy alloy system",
    "成分": "composition element",
    "工艺": "process processing treatment",
    "热处理": "heat treatment",
    "退火": "annealing annealed",
    "均匀化": "homogenization homogenized",
    "烧结": "sintering sintered",
    "增材制造": "additive manufacturing LPBF SLM DED",
    "相组成": "phase constitution",
    "析出相": "precipitate precipitation phase",
    "碳化物": "carbide",
    "硼化物": "boride",
    "硅化物": "silicide",
    "氧化物": "oxide",
    "晶粒": "grain grain size",
    "晶界": "grain boundary",
    "强化": "strengthening",
    "固溶强化": "solid solution strengthening",
    "析出强化": "precipitation strengthening",
    "弥散强化": "dispersion strengthening ODS",
    "屈服强度": "yield strength",
    "抗拉强度": "ultimate tensile strength tensile strength",
    "拉伸强度": "tensile strength",
    "高温强度": "high temperature strength",
    "延伸率": "elongation ductility",
    "塑性": "plasticity ductility elongation",
    "硬度": "hardness",
    "蠕变": "creep",
    "断裂韧性": "fracture toughness",
    "耐氧化": "oxidation resistance",
    "氧化": "oxidation oxide scale",
    "裂纹": "crack cracking",
    "孔隙": "pore porosity",
    "密度": "density",
}

ALLOWED_PREDICATES = {
    "STUDIES", "INSTANCE_OF", "CONTAINS_ELEMENT", "UNDERGOES_PROCESS",
    "CONTAINS_PHASE", "HAS_MICROSTRUCTURE",
    "HAS_PROPERTY_OBSERVATION", "LOCATED_AT", "FORMS", "DISSOLVES",
    "TRANSFORMS_TO", "PROMOTES", "SUPPRESSES", "REFINES", "COARSENS",
    "STABILIZES", "DESTABILIZES", "ACTIVATES_MECHANISM", "IMPROVES",
    "DEGRADES", "INCREASES", "DECREASES", "CORRELATES_WITH",
    "CAUSES_TRADEOFF", "COMPARED_WITH",
    "FOLLOWED_BY", "OBSERVED_AFTER_PROCESS", "ASSOCIATED_WITH_MECHANISM",
    "HAS_COMPOSITION", "HAS_SAMPLE", "HAS_DEFECT", "USES_MODEL", "PREDICTS",
    "FABRICATED_BY", "PRODUCES",
}
PREDICATE_ALIASES = {
    "EXHIBITS": "HAS_MICROSTRUCTURE",
    "HAS_MECHANISM": "ACTIVATES_MECHANISM",
    "CAUSES": "CORRELATES_WITH",
}


def _connect() -> sqlite3.Connection:
    for directory in (GRAPH_DIR, GRAPH_RAW_DIR, GRAPH_PAPERS_DIR, GRAPH_FAILED_DIR, GRAPH_REPORTS_DIR):
        directory.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(GRAPH_DB_PATH, timeout=60)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA journal_mode=WAL")
    connection.execute("PRAGMA foreign_keys=ON")
    connection.executescript(
        """
        CREATE TABLE IF NOT EXISTS graph_papers (
            document_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            document_type TEXT NOT NULL DEFAULT 'literature',
            status TEXT NOT NULL,
            themes TEXT NOT NULL DEFAULT '[]',
            graph_path TEXT,
            source_chunks INTEGER NOT NULL DEFAULT 0,
            node_count INTEGER NOT NULL DEFAULT 0,
            edge_count INTEGER NOT NULL DEFAULT 0,
            prompt_tokens INTEGER NOT NULL DEFAULT 0,
            completion_tokens INTEGER NOT NULL DEFAULT 0,
            error TEXT,
            updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS nodes (
            node_key TEXT PRIMARY KEY,
            document_id TEXT,
            local_id TEXT,
            type TEXT NOT NULL,
            name TEXT NOT NULL,
            canonical_name TEXT NOT NULL,
            sample_key TEXT,
            material_state TEXT,
            attributes_json TEXT NOT NULL DEFAULT '{}',
            evidence_json TEXT NOT NULL DEFAULT '[]'
        );
        CREATE TABLE IF NOT EXISTS node_sources (
            node_key TEXT NOT NULL,
            document_id TEXT NOT NULL,
            local_id TEXT NOT NULL DEFAULT '',
            source_name TEXT NOT NULL,
            attributes_json TEXT NOT NULL DEFAULT '{}',
            evidence_json TEXT NOT NULL DEFAULT '[]',
            PRIMARY KEY (node_key, document_id, local_id)
        );
        CREATE TABLE IF NOT EXISTS edges (
            edge_key TEXT PRIMARY KEY,
            document_id TEXT NOT NULL,
            source_key TEXT NOT NULL,
            predicate TEXT NOT NULL,
            target_key TEXT NOT NULL,
            sample_key TEXT,
            material_state TEXT,
            polarity TEXT,
            assertion_level TEXT,
            attributes_json TEXT NOT NULL DEFAULT '{}',
            evidence_json TEXT NOT NULL DEFAULT '[]'
        );
        CREATE INDEX IF NOT EXISTS idx_nodes_document ON nodes(document_id);
        CREATE INDEX IF NOT EXISTS idx_nodes_type_name ON nodes(type, canonical_name);
        CREATE INDEX IF NOT EXISTS idx_edges_document ON edges(document_id);
        CREATE INDEX IF NOT EXISTS idx_edges_source ON edges(source_key);
        CREATE INDEX IF NOT EXISTS idx_edges_target ON edges(target_key);
        CREATE VIRTUAL TABLE IF NOT EXISTS node_fts USING fts5(
            node_key UNINDEXED,
            name,
            canonical_name,
            tokens,
            tokenize='unicode61'
        );
        """
    )
    graph_paper_columns = {
        str(row["name"])
        for row in connection.execute("PRAGMA table_info(graph_papers)").fetchall()
    }
    if "document_type" not in graph_paper_columns:
        connection.execute(
            "ALTER TABLE graph_papers ADD COLUMN "
            "document_type TEXT NOT NULL DEFAULT 'literature'"
        )
    for original, canonical in PREDICATE_ALIASES.items():
        connection.execute(
            "UPDATE edges SET predicate=? WHERE predicate=?", (canonical, original)
        )
    return connection


def initialize_graph() -> None:
    with closing(_connect()) as connection, connection:
        pass


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _as_list(value: Any) -> list:
    return value if isinstance(value, list) else []


def _as_dict(value: Any) -> dict:
    return value if isinstance(value, dict) else {}


def _json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), default=str)


def _canonical(value: Any) -> str:
    text = str(value or "").strip().lower()
    text = text.replace("–", "-").replace("—", "-").replace("−", "-")
    text = re.sub(r"\s+", " ", text)
    return text


def _safe_name(value: Any, fallback: str) -> str:
    text = str(value or "").strip()
    return text or fallback


def _local_key(document_id: str, local_id: str) -> str:
    return f"local:{document_id}:{local_id}"


def _concept_key(entity_type: str, name: str) -> str:
    canonical = _canonical(name)
    digest = hashlib.sha1(f"{entity_type}:{canonical}".encode("utf-8")).hexdigest()[:20]
    return f"concept:{entity_type}:{digest}"


def _process_key(entity_type: str, method: str, attributes: dict[str, Any]) -> str:
    """Merge only genuinely identical process definitions across sample routes."""

    def compact(value: Any) -> Any:
        if isinstance(value, dict):
            return {
                str(key): compact(item)
                for key, item in sorted(value.items(), key=lambda pair: str(pair[0]))
                if item not in (None, "", [], {})
            }
        if isinstance(value, list):
            return [compact(item) for item in value if item not in (None, "", [], {})]
        if isinstance(value, str):
            return re.sub(r"\s+", " ", value).strip().casefold()
        return value

    identity = {
        "type": entity_type,
        "method": _canonical(method),
        "parameters": compact(_as_dict(attributes.get("parameters"))),
        "input_state": compact(attributes.get("input_state")),
        "output_state": compact(attributes.get("output_state")),
    }
    signature = json.dumps(identity, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha1(signature.encode("utf-8")).hexdigest()[:20]
    return f"process:{digest}"


def _normalize_composition_unit(value: Any) -> str:
    text = re.sub(r"[\s.]", "", str(value or "")).casefold()
    aliases = {
        "wt%": "wt.%",
        "weight%": "wt.%",
        "mass%": "wt.%",
        "at%": "at.%",
        "atomic%": "at.%",
        "vol%": "vol.%",
        "%": "%",
        "ppm": "ppm",
        "ppmw": "ppm",
    }
    return aliases.get(text, str(value or "").strip())


def _format_composition_number(value: Any) -> str:
    if value is None or value == "":
        return ""
    try:
        number = float(value)
        return f"{number:g}"
    except (TypeError, ValueError):
        return str(value).strip()


def _normalized_composition_name(value: Any) -> str:
    text = str(value or "").strip().casefold()
    word_symbols = {
        "tungsten": "w",
        "molybdenum": "mo",
        "niobium": "nb",
        "tantalum": "ta",
        "zirconium": "zr",
        "hafnium": "hf",
        "titanium": "ti",
    }
    for word, symbol in word_symbols.items():
        text = re.sub(rf"\b{word}\b", symbol, text)
    text = re.sub(r"\b(?:pure|commercially|nominal|alloy|sample|specimen)\b", "", text)
    text = re.sub(r"(?:wt|at|vol)(?:\s*\.\s*)?%|mass\s*%", "", text)
    return re.sub(r"[^a-z0-9]+", "", text)


def _is_opaque_sample_name(value: Any) -> bool:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if not text:
        return True
    return bool(
        "#" in text
        or re.fullmatch(r"(?i)(?:sample|specimen|alloy|build|part)\s*[-#]?[a-z0-9]+(?:\s*,\s*.+)?", text)
    )


def _composition_entry_label(entry: dict[str, Any]) -> str:
    element = _safe_name(entry.get("element"), "?")
    unit = _normalize_composition_unit(entry.get("unit"))
    value = _format_composition_number(entry.get("value"))
    minimum = _format_composition_number(entry.get("min_value"))
    maximum = _format_composition_number(entry.get("max_value"))
    role = str(entry.get("role") or "").casefold()
    if role == "balance" and not any((value, minimum, maximum)):
        return f"{element} balance"
    if value:
        amount = value
    elif minimum and maximum:
        amount = f"{minimum}–{maximum}"
    elif minimum:
        amount = f"≥{minimum}"
    elif maximum:
        amount = f"≤{maximum}"
    else:
        amount = ""
    return " ".join(part for part in (element, amount, unit) if part)


def _composition_identity(sample: dict[str, Any], alloy_system_name: str = "") -> tuple[str, str, list[dict]]:
    """Return a cross-paper composition key, a clean label, and normalized components."""
    components: list[dict[str, Any]] = []
    for raw in _as_list(sample.get("composition")):
        if not isinstance(raw, dict):
            continue
        item = {key: value for key, value in raw.items() if key != "evidence"}
        item["element"] = _safe_name(item.get("element"), "?")
        item["unit"] = _normalize_composition_unit(item.get("unit"))
        if item.get("value") in (0, 0.0, "0") and item.get("min_value") in (None, "") and item.get("max_value") in (None, ""):
            continue
        components.append(item)
    components.sort(
        key=lambda item: (
            str(item.get("element") or "").casefold(),
            str(item.get("unit") or "").casefold(),
            str(item.get("value") or ""),
        )
    )

    canonical = re.sub(r"\s+", " ", str(sample.get("canonical_name") or "")).strip()
    usable_canonical = canonical and not _is_opaque_sample_name(canonical)
    labels = [_composition_entry_label(item) for item in components]
    generated = " + ".join(label for label in labels if label)
    label = canonical if usable_canonical else generated
    if not label:
        label = re.sub(r"\s+", " ", str(alloy_system_name or "")).strip() or "Unresolved composition"

    name_signature = _normalized_composition_name(canonical) if usable_canonical else ""
    component_signature = _json(
        [
            {
                "element": str(item.get("element") or "").casefold(),
                "value": item.get("value"),
                "min": item.get("min_value"),
                "max": item.get("max_value"),
                "unit": item.get("unit"),
                "role": str(item.get("role") or "").casefold(),
                "applies_to": str(item.get("applies_to") or "").casefold(),
            }
            for item in components
        ]
    )
    signature = f"name:{name_signature}" if name_signature else f"components:{component_signature}"
    if not name_signature and not components:
        signature = ""
    return signature, label, components


def _composition_key(signature: str, document_id: str, local_id: str) -> str:
    if not signature:
        return _local_key(document_id, local_id)
    digest = hashlib.sha1(signature.encode("utf-8")).hexdigest()[:20]
    return f"composition:{digest}"


def _state_key(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "", _canonical(value))


POST_TREATMENT_TERMS = (
    "anneal", "ageing", "aging", "solution treat", "homogen", "heat treat",
    "quench", "temper", "stress relie", "recrystalli", "post-heat", "post treat",
    "coating", "surface treatment", "surface modification",
)


def _process_entity_type(method: Any) -> str:
    normalized = _canonical(method)
    return "PostTreatment" if any(term in normalized for term in POST_TREATMENT_TERMS) else "FabricationProcess"


DEFECT_TERMS = (
    "crack", "pore", "porosity", "void", "vacancy", "dislocation", "segregation",
    "lack of fusion", "lack-of-fusion", "keyhole", "unmelted", "inclusion",
    "residual stress", "delamination", "hot tearing", "cold shut",
)


def _structure_entity_type(raw_type: Any, name: Any) -> str:
    declared = _canonical(raw_type)
    normalized_name = _canonical(name)
    if declared == "defect" or any(term in normalized_name for term in DEFECT_TERMS):
        return "Defect"
    if declared == "phase":
        return "Phase"
    return "Microstructure"


def _property_has_numeric_value(observation: dict[str, Any]) -> bool:
    """A property node must carry an explicit number or numerical range."""
    for field in ("value", "min_value", "max_value"):
        value = observation.get(field)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return True
        if value not in (None, "") and re.search(r"[-+]?\d+(?:\.\d+)?", str(value)):
            return True
    return False


NON_PERFORMANCE_TERMS = (
    "grain size", "particle size", "precipitate size", "phase fraction",
    "volume fraction", "dimensional shrinkage", "shrinkage", "strain rate",
    "test temperature", "testing temperature", "annealing temperature",
    "processing temperature", "critical al content", "alloying content",
    "composition", "layer thickness", "scan speed", "laser power", "porosity",
)

MATERIAL_PERFORMANCE_TERMS = (
    "strength", "elongation", "ductility", "plasticity", "fracture strain",
    "failure strain", "hardness", "toughness", "elastic modulus", "young's modulus",
    "creep", "rupture life", "fatigue", "wear", "friction", "cof",
    "density", "work-hardening", "work hardening", "tensile-compression asymmetry",
    "yield ratio", "dbtt", "ductile-to-brittle", "thermal conductivity",
    "electrical conductivity", "electrical resistivity", "thermal expansion",
    "oxidation", "corrosion", "mass gain", "mass loss", "loss depth",
    "erosion", "ablation", "impact energy", "impact toughness",
)

MODEL_PERFORMANCE_TERMS = (
    "r2", "r²", "coefficient of determination", "mae", "mse", "rmse",
    "mean absolute error", "mean squared error", "root mean squared error",
    "accuracy", "precision", "recall", "f1", "auc", "roc", "prediction error",
    "validation score",
)


def _property_kind(observation: dict[str, Any], model_property_ids: set[str] | None = None) -> str | None:
    """Classify only decision-relevant material or model performance metrics."""
    if not _property_has_numeric_value(observation):
        return None
    name = re.sub(r"\s+", " ", str(observation.get("property") or "")).strip().casefold()
    if not name or any(term in name for term in NON_PERFORMANCE_TERMS):
        return None
    local_id = str(observation.get("id") or "")
    if any(term in name for term in MODEL_PERFORMANCE_TERMS):
        return "model" if local_id in (model_property_ids or set()) else None
    if any(term in name for term in MATERIAL_PERFORMANCE_TERMS):
        return "material"
    return None


def _property_value_label(observation: dict[str, Any]) -> str:
    value = observation.get("value")
    minimum = observation.get("min_value")
    maximum = observation.get("max_value")
    if value not in (None, ""):
        return str(value).strip()
    if minimum not in (None, "") and maximum not in (None, ""):
        return f"{minimum}–{maximum}"
    if minimum not in (None, ""):
        return f"≥{minimum}"
    if maximum not in (None, ""):
        return f"≤{maximum}"
    return ""


def _component_element_symbols(value: Any) -> list[str]:
    """Resolve an extracted composition component to chemical elements only.

    Models occasionally place an additive formula such as ``La2O3`` or
    ``B4C`` in the schema's ``element`` field.  The graph must not present
    those compounds as chemical elements, so formulas are decomposed while
    the original component remains preserved on the edge attributes.
    """
    raw = re.sub(r"\s+", "", str(value or "").strip())
    if not raw:
        return []
    direct = ELEMENT_SYMBOLS.get(raw.casefold())
    if direct:
        return [direct]
    formatted = _format_alloy_canonical(raw)
    symbols = re.findall(r"[A-Z][a-z]?", formatted)
    if not symbols or any(symbol.casefold() not in ELEMENT_SYMBOLS for symbol in symbols):
        return []
    residue = re.sub(r"[A-Z][a-z]?|[0-9.]+|[₀-₉]+|[()\[\]{},+\-·/]", "", formatted)
    if residue:
        return []
    return list(dict.fromkeys(ELEMENT_SYMBOLS[symbol.casefold()] for symbol in symbols))


PURE_ELEMENT_NAME_ALIASES = {
    "molybdenum": "Mo",
    "tungsten": "W",
    "niobium": "Nb",
    "tantalum": "Ta",
    "titanium": "Ti",
    "zirconium": "Zr",
    "hafnium": "Hf",
}


def _pure_material_symbol(value: Any) -> str | None:
    """Recognize a pure-element material family without creating an Alloy node."""
    text = re.sub(r"\s+", " ", str(value or "").strip()).casefold()
    text = re.sub(r"^(?:commercially\s+)?pure\s+", "", text).strip()
    if text in ELEMENT_SYMBOLS:
        return ELEMENT_SYMBOLS[text]
    return PURE_ELEMENT_NAME_ALIASES.get(text)


def _clean_sample_qualifier(value: Any) -> str:
    """Clean a source-supported state/process phrase for a concise label."""
    text = re.sub(r"\s+", " ", str(value or "").strip())
    replacements = {
        "¦Å": "ε",
        "Îµ": "ε",
        "ε ": "ε",
        "¡ãC": "°C",
        "Â°C": "°C",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    text = re.sub(r"\s*=\s*", "=", text)
    return text


def _process_display_qualifier(step: dict[str, Any] | None) -> str:
    """Return a compact, source-supported discriminator for a sample route."""
    if not step:
        return ""
    method = _clean_sample_qualifier(step.get("method"))
    lowered_method = method.casefold()
    if "spark plasma sinter" in lowered_method:
        method = "SPS"
    elif "hot isostatic press" in lowered_method:
        method = "HIP"
    elif "laser powder bed" in lowered_method:
        method = "LPBF"
    parameters = _as_dict(_as_dict(step.get("attributes")).get("parameters"))
    details: list[str] = []
    temperature = parameters.get("temperature_c")
    if temperature not in (None, ""):
        details.append(f"{temperature} °C")
    duration = parameters.get("time")
    if duration not in (None, ""):
        details.append(_clean_sample_qualifier(duration))
    deformation = parameters.get("deformation")
    if deformation not in (None, ""):
        deformation_text = _clean_sample_qualifier(deformation)
        if "rolling" in lowered_method:
            return f"{deformation_text} hot-rolled"
        details.append(f"{deformation_text} deformation")
    return " · ".join([part for part in (method, *details) if part])


def _single_element_symbol(canonical_name: Any, components: list[dict[str, Any]]) -> str | None:
    """Return the element symbol when the material is chemically a pure element."""
    text = re.sub(r"\b(?:pure|commercially pure|balance)\b", "", str(canonical_name or ""), flags=re.I)
    text = re.sub(r"[^A-Za-z]", "", text).casefold()
    if text in ELEMENT_SYMBOLS:
        return ELEMENT_SYMBOLS[text]
    real_components = [item for item in components if str(item.get("element") or "").strip() not in {"", "?"}]
    if len(real_components) != 1:
        return None
    item = real_components[0]
    role = str(item.get("role") or "").casefold()
    value = item.get("value")
    unit = _normalize_composition_unit(item.get("unit"))
    is_pure = role in {"base", "balance", "matrix", "pure"}
    if isinstance(value, (int, float)) and float(value) >= 99 and unit in {"wt.%", "at.%", "%"}:
        is_pure = True
    symbol = str(item.get("element") or "").casefold()
    return ELEMENT_SYMBOLS.get(symbol) if is_pure else None


def _sequence_sort_key(value: Any) -> tuple[int, float | str]:
    try:
        return (0, float(value))
    except (TypeError, ValueError):
        return (1, str(value or "").casefold())


def _edge_key(document_id: str, *parts: Any) -> str:
    raw = "|".join(str(part or "") for part in (document_id, *parts))
    return "edge:" + hashlib.sha1(raw.encode("utf-8")).hexdigest()


def _search_tokens(text: str) -> str:
    lowered = _canonical(text)
    tokens = re.findall(r"[a-z0-9]+(?:[-_.][a-z0-9]+)*", lowered)
    for run in re.findall(r"[\u3400-\u9fff]+", lowered):
        tokens.append(run)
        tokens.extend(run[index : index + 2] for index in range(max(0, len(run) - 1)))
    return " ".join(dict.fromkeys(token for token in tokens if token))


def _expand_query(text: str) -> str:
    additions = [english for chinese, english in QUERY_SYNONYMS.items() if chinese in text]
    return " ".join((text, *additions))


def _normalize_predicate(value: Any) -> tuple[str, str | None]:
    original = _safe_name(value, "CORRELATES_WITH").upper().replace(" ", "_")
    canonical = PREDICATE_ALIASES.get(original, original)
    if canonical not in ALLOWED_PREDICATES:
        return "CORRELATES_WITH", original
    return canonical, original if canonical != original else None


def _evidence(value: Any, document_id: str, source_name: str, chunk_id: str | None = None) -> list[dict]:
    output: list[dict] = []
    for item in _as_list(value):
        if isinstance(item, str):
            item = {"quote": item}
        if not isinstance(item, dict):
            continue
        quote = str(item.get("quote") or item.get("text") or "").strip()
        if not quote and not any(item.get(key) for key in ("page", "section", "table", "figure")):
            continue
        output.append(
            {
                "document_id": document_id,
                "source": source_name,
                "chunk_id": item.get("chunk_id") or chunk_id,
                "page": item.get("page"),
                "section": item.get("section"),
                "quote": quote[:1200],
                "table": item.get("table"),
                "figure": item.get("figure"),
            }
        )
    return output


def _insert_node(
    connection: sqlite3.Connection,
    *,
    node_key: str,
    document_id: str | None,
    local_id: str,
    entity_type: str,
    name: str,
    canonical_name: str | None = None,
    sample_key: str | None = None,
    material_state: str | None = None,
    attributes: dict | None = None,
    evidence: list | None = None,
    source_document_id: str,
    source_name: str,
) -> None:
    canonical_name = _canonical(canonical_name or name)
    attributes = attributes or {}
    evidence = evidence or []
    connection.execute(
        """
        INSERT INTO nodes(
            node_key, document_id, local_id, type, name, canonical_name,
            sample_key, material_state, attributes_json, evidence_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(node_key) DO UPDATE SET
            name=CASE WHEN length(excluded.name) > length(nodes.name) THEN excluded.name ELSE nodes.name END,
            canonical_name=excluded.canonical_name
        """,
        (
            node_key,
            document_id,
            local_id,
            entity_type,
            name,
            canonical_name,
            sample_key,
            material_state,
            _json(attributes),
            _json(evidence),
        ),
    )
    connection.execute(
        """
        INSERT OR REPLACE INTO node_sources(
            node_key, document_id, local_id, source_name, attributes_json, evidence_json
        ) VALUES (?, ?, ?, ?, ?, ?)
        """,
        (node_key, source_document_id, local_id, source_name, _json(attributes), _json(evidence)),
    )
    connection.execute("DELETE FROM node_fts WHERE node_key=?", (node_key,))
    searchable = " ".join((name, canonical_name, entity_type))
    connection.execute(
        "INSERT INTO node_fts(node_key, name, canonical_name, tokens) VALUES (?, ?, ?, ?)",
        (node_key, name, canonical_name, _search_tokens(searchable)),
    )


def _insert_edge(
    connection: sqlite3.Connection,
    *,
    document_id: str,
    source_key: str,
    predicate: str,
    target_key: str,
    sequence: Any,
    sample_key: str | None = None,
    material_state: str | None = None,
    polarity: str | None = None,
    assertion_level: str | None = None,
    attributes: dict | None = None,
    evidence: list | None = None,
) -> None:
    edge_key = _edge_key(document_id, sequence, source_key, predicate, target_key)
    connection.execute(
        """
        INSERT OR REPLACE INTO edges(
            edge_key, document_id, source_key, predicate, target_key, sample_key,
            material_state, polarity, assertion_level, attributes_json, evidence_json
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            edge_key,
            document_id,
            source_key,
            predicate,
            target_key,
            sample_key,
            material_state,
            polarity,
            assertion_level,
            _json(attributes or {}),
            _json(evidence or []),
        ),
    )


def _remove_document_graph(connection: sqlite3.Connection, document_id: str) -> None:
    local_keys = [
        row[0]
        for row in connection.execute(
            "SELECT node_key FROM nodes WHERE document_id=?", (document_id,)
        ).fetchall()
    ]
    connection.execute("DELETE FROM edges WHERE document_id=?", (document_id,))
    connection.execute("DELETE FROM node_sources WHERE document_id=?", (document_id,))
    for key in local_keys:
        connection.execute("DELETE FROM node_fts WHERE node_key=?", (key,))
    connection.execute("DELETE FROM nodes WHERE document_id=?", (document_id,))


def replace_paper_graph(
    document: dict,
    payload: dict,
    graph_path: str,
    source_chunks: int,
    usage: dict | None = None,
    themes: list[str] | None = None,
) -> dict[str, int]:
    """Atomically replace one paper graph with normalized nodes and edges."""
    document_id = str(document["id"])
    source_name = str(document["name"])
    chunk_id = str(payload.get("chunk_id") or "paper")
    usage = usage or {}
    themes = themes or []

    with _LOCK, closing(_connect()) as connection, connection:
        _remove_document_graph(connection, document_id)
        local_map: dict[str, str] = {}
        alloy_system_names: dict[str, str] = {}
        sample_records: dict[str, dict[str, Any]] = {}
        process_by_sample: dict[str, list[dict[str, Any]]] = {}
        phase_by_sample: dict[str, list[dict[str, Any]]] = {}
        edge_serial = 0

        def add_edge(source_key: str, predicate: str, target_key: str, **kwargs: Any) -> None:
            nonlocal edge_serial
            edge_serial += 1
            _insert_edge(
                connection,
                document_id=document_id,
                source_key=source_key,
                predicate=predicate,
                target_key=target_key,
                sequence=edge_serial,
                **kwargs,
            )

        metadata = _as_dict(payload.get("paper_metadata"))

        for index, alloy in enumerate(_as_list(payload.get("alloy_systems")), 1):
            if not isinstance(alloy, dict):
                continue
            local_id = str(alloy.get("id") or f"alloy_system_{index}")
            name = _safe_name(alloy.get("name"), f"Unspecified alloy system {index}")
            pure_system = _pure_material_symbol(name)
            entity_type = "Element" if pure_system else "Alloy"
            display_name = pure_system or name
            key = _concept_key(entity_type, display_name)
            evidence = _evidence(alloy.get("evidence"), document_id, source_name, chunk_id)
            _insert_node(
                connection,
                node_key=key,
                document_id=None,
                local_id=local_id,
                entity_type=entity_type,
                name=display_name,
                attributes={
                    "material_category": alloy.get("material_category"),
                    "source_system_name": name,
                    "pure_material": bool(pure_system),
                },
                evidence=evidence,
                source_document_id=document_id,
                source_name=source_name,
            )
            local_map[local_id] = key
            alloy_system_names[local_id] = display_name

        for index, sample in enumerate(_as_list(payload.get("samples")), 1):
            if not isinstance(sample, dict):
                continue
            local_id = str(sample.get("id") or f"sample_{index}")
            alloy_system_id = str(sample.get("alloy_system_id") or "")
            signature, name, components = _composition_identity(
                sample,
                alloy_system_names.get(alloy_system_id, ""),
            )
            evidence = _evidence(sample.get("evidence"), document_id, source_name, chunk_id)
            original_name = str(sample.get("original_name") or "").strip()
            pure_element = _single_element_symbol(name, components)
            element_records: list[tuple[str, str, list[dict], dict[str, Any]]] = []
            for comp_index, composition in enumerate(_as_list(sample.get("composition")), 1):
                if not isinstance(composition, dict):
                    continue
                raw_element = _safe_name(composition.get("element"), "Unspecified element")
                comp_evidence = _evidence(composition.get("evidence"), document_id, source_name, chunk_id)
                comp_attributes = {field: value for field, value in composition.items() if field != "evidence"}
                comp_attributes["source_component"] = raw_element
                for symbol_index, element in enumerate(_component_element_symbols(raw_element), 1):
                    element_key = _concept_key("Element", element)
                    _insert_node(
                        connection,
                        node_key=element_key,
                        document_id=None,
                        local_id=f"{local_id}_element_{comp_index}_{symbol_index}",
                        entity_type="Element",
                        name=element,
                        evidence=comp_evidence,
                        source_document_id=document_id,
                        source_name=source_name,
                    )
                    element_records.append((element_key, element, comp_evidence, comp_attributes))

            if pure_element and not any(element == pure_element for _, element, _, _ in element_records):
                element_key = _concept_key("Element", pure_element)
                _insert_node(
                    connection,
                    node_key=element_key,
                    document_id=None,
                    local_id=f"{local_id}_element_pure",
                    entity_type="Element",
                    name=pure_element,
                    evidence=evidence,
                    source_document_id=document_id,
                    source_name=source_name,
                )
                element_records.append((element_key, pure_element, evidence, {"role": "pure"}))

            if pure_element:
                material_key = _concept_key("Element", pure_element)
            else:
                material_key = _composition_key(signature, document_id, local_id)
                _insert_node(
                    connection,
                    node_key=material_key,
                    document_id=None if signature else document_id,
                    local_id=f"{local_id}_composition",
                    entity_type="Composition",
                    name=name,
                    canonical_name=name,
                    material_state=None,
                    attributes={"composition": components},
                    evidence=evidence,
                    source_document_id=document_id,
                    source_name=source_name,
                )

            sample_key = _local_key(document_id, local_id)
            local_map[local_id] = sample_key
            sample_attributes = {
                "alloy_system_id": sample.get("alloy_system_id"),
                "composition": components,
                "composition_name": name,
                "source_designation": original_name or None,
                "source_material_state": sample.get("material_state"),
            }
            _insert_node(
                connection,
                node_key=sample_key,
                document_id=document_id,
                local_id=local_id,
                entity_type="Sample",
                name=f"{name} sample" if name != "Unresolved composition" else "Material sample",
                canonical_name=name,
                sample_key=sample_key,
                material_state=None,
                attributes=sample_attributes,
                evidence=evidence,
                source_document_id=document_id,
                source_name=source_name,
            )
            sample_records[local_id] = {
                "key": sample_key,
                "material_key": material_key,
                "name": name,
                "pure_element": pure_element,
                "material_state": sample.get("material_state"),
                "composition": components,
                "source_designation": original_name,
                "attributes": sample_attributes,
            }
            alloy_key = local_map.get(alloy_system_id)
            if alloy_key:
                if pure_element:
                    if alloy_key != material_key:
                        add_edge(alloy_key, "CONTAINS_ELEMENT", material_key, sample_key=sample_key, evidence=evidence)
                else:
                    add_edge(alloy_key, "HAS_COMPOSITION", material_key, sample_key=sample_key, evidence=evidence)
            if not pure_element:
                for element_key, _, comp_evidence, comp_attributes in element_records:
                    add_edge(
                        material_key,
                        "CONTAINS_ELEMENT",
                        element_key,
                        sample_key=sample_key,
                        material_state=sample.get("material_state"),
                        attributes=comp_attributes,
                        evidence=comp_evidence,
                    )

        for index, process in enumerate(_as_list(payload.get("process_steps")), 1):
            if not isinstance(process, dict):
                continue
            local_id = str(process.get("id") or f"process_{index}")
            method = _safe_name(process.get("method"), f"Process step {index}")
            sample_key = local_map.get(str(process.get("sample_id") or ""))
            evidence = _evidence(process.get("evidence"), document_id, source_name, chunk_id)
            attributes = {
                "sequence": process.get("sequence"),
                "parameters": _as_dict(process.get("parameters")),
                "input_state": process.get("input_state"),
                "output_state": process.get("output_state"),
            }
            entity_type = _process_entity_type(method)
            key = _process_key(entity_type, method, attributes)
            local_map[local_id] = key
            _insert_node(
                connection,
                node_key=key,
                document_id=None,
                local_id=local_id,
                entity_type=entity_type,
                name=method,
                sample_key=None,
                material_state=None,
                attributes=attributes,
                evidence=evidence,
                source_document_id=document_id,
                source_name=source_name,
            )
            if sample_key:
                process_by_sample.setdefault(str(process.get("sample_id") or ""), []).append(
                    {
                        "key": key,
                        "local_id": local_id,
                        "method": method,
                        "sequence": process.get("sequence") if process.get("sequence") is not None else index,
                        "input_state": process.get("input_state"),
                        "output_state": process.get("output_state"),
                        "attributes": attributes,
                        "evidence": evidence,
                    }
                )

        # Build stable, human-readable sample discriminators.  Composition is
        # the identity; state and processing distinguish physical specimens.
        # Author codes remain metadata and are never used as canvas labels.
        state_groups: dict[tuple[str, str], list[str]] = {}
        for sample_id, record in sample_records.items():
            display_state = _clean_sample_qualifier(record.get("material_state"))
            record["attributes"]["display_state"] = display_state or None
            group_key = (str(record.get("material_key") or ""), _canonical(display_state))
            state_groups.setdefault(group_key, []).append(sample_id)

        for sample_ids in state_groups.values():
            process_buckets: dict[str, list[str]] = {}
            use_process = len(sample_ids) > 1
            for sample_id in sample_ids:
                steps = sorted(
                    process_by_sample.get(sample_id, []),
                    key=lambda step: (_sequence_sort_key(step.get("sequence")), step["key"]),
                )
                display_process = _process_display_qualifier(steps[-1] if steps else None) if use_process else ""
                sample_records[sample_id]["attributes"]["display_process"] = display_process or None
                process_buckets.setdefault(_canonical(display_process), []).append(sample_id)
            for bucket in process_buckets.values():
                count = len(bucket)
                for variant_index, sample_id in enumerate(bucket, 1):
                    attributes = sample_records[sample_id]["attributes"]
                    attributes["display_variant_count"] = count
                    attributes["display_variant_index"] = variant_index if count > 1 else None
                    sample_key = sample_records[sample_id]["key"]
                    encoded = _json(attributes)
                    connection.execute(
                        "UPDATE nodes SET attributes_json=? WHERE node_key=?",
                        (encoded, sample_key),
                    )
                    connection.execute(
                        """
                        UPDATE node_sources SET attributes_json=?
                        WHERE node_key=? AND document_id=? AND local_id=?
                        """,
                        (encoded, sample_key, document_id, sample_id),
                    )

        # The manufacturing route is the main material path.  Elements remain
        # leaves of a Composition, while Composition (or a pure Element) enters
        # FabricationProcess, optional PostTreatment, and finally produces the
        # physical Sample. Material state remains an attribute on processes,
        # samples, observations and relations; it is not a standalone entity.
        for sample_id, steps in process_by_sample.items():
            steps.sort(key=lambda step: (_sequence_sort_key(step.get("sequence")), step["key"]))
            sample_key = local_map.get(sample_id)
            if not sample_key or not steps:
                continue
            material_key = sample_records[sample_id]["material_key"]
            process_source = material_key
            link_predicate = "FABRICATED_BY"
            for step in steps:
                add_edge(
                    process_source,
                    link_predicate,
                    step["key"],
                    sample_key=sample_key,
                    attributes=step["attributes"],
                    evidence=step["evidence"],
                )
                process_source = step["key"]
                link_predicate = "FOLLOWED_BY"
            add_edge(
                process_source,
                "PRODUCES",
                sample_key,
                sample_key=sample_key,
                evidence=steps[-1]["evidence"],
            )

        # If the source gives no route at all, preserve a direct material to
        # sample identity link instead of inventing a fabrication process.
        for sample_id, record in sample_records.items():
            if not process_by_sample.get(sample_id):
                add_edge(
                    record["material_key"],
                    "HAS_SAMPLE",
                    record["key"],
                    sample_key=record["key"],
                )

        def process_anchor(sample_id: str, material_state: Any) -> dict[str, Any] | None:
            steps = process_by_sample.get(sample_id, [])
            if not steps:
                return None
            wanted = _state_key(material_state)
            if wanted:
                matching = [
                    step
                    for step in steps
                    if wanted in {
                        _state_key(step.get("input_state")),
                        _state_key(step.get("output_state")),
                    }
                ]
                if matching:
                    return matching[-1]
            return steps[-1]

        for index, phase in enumerate(_as_list(payload.get("phases_and_microstructures")), 1):
            if not isinstance(phase, dict):
                continue
            local_id = str(phase.get("id") or f"phase_{index}")
            raw_name = _safe_name(phase.get("name"), f"Structure {index}")
            entity_type = _structure_entity_type(phase.get("type"), raw_name)
            name = _safe_name(phase.get("name"), f"{entity_type} {index}")
            key = _concept_key(entity_type, name)
            local_map[local_id] = key
            sample_id = str(phase.get("sample_id") or "")
            sample_key = local_map.get(sample_id)
            evidence = _evidence(phase.get("evidence"), document_id, source_name, chunk_id)
            attributes = _as_dict(phase.get("attributes"))
            _insert_node(
                connection,
                node_key=key,
                document_id=None,
                local_id=local_id,
                entity_type=entity_type,
                name=name,
                sample_key=None,
                material_state=None,
                attributes=attributes,
                evidence=evidence,
                source_document_id=document_id,
                source_name=source_name,
            )
            anchor = process_anchor(sample_id, phase.get("material_state"))
            if anchor:
                add_edge(
                    anchor["key"],
                    "OBSERVED_AFTER_PROCESS",
                    key,
                    sample_key=sample_key,
                    material_state=phase.get("material_state"),
                    attributes=attributes,
                    evidence=evidence,
                )
            elif sample_key:
                add_edge(
                    sample_key,
                    "CONTAINS_PHASE" if entity_type == "Phase" else "HAS_DEFECT" if entity_type == "Defect" else "HAS_MICROSTRUCTURE",
                    key,
                    sample_key=sample_key,
                    material_state=phase.get("material_state"),
                    attributes=attributes,
                    evidence=evidence,
                )
            if sample_id:
                phase_by_sample.setdefault(sample_id, []).append(
                    {
                        "key": key,
                        "material_state": phase.get("material_state"),
                        "entity_type": entity_type,
                        "evidence": evidence,
                    }
                )

        def phase_anchor(sample_id: str, material_state: Any) -> dict[str, Any] | None:
            phases = phase_by_sample.get(sample_id, [])
            if not phases:
                return None
            wanted = _state_key(material_state)
            if wanted:
                matching = [
                    phase
                    for phase in phases
                    if _state_key(phase.get("material_state")) == wanted
                ]
                if matching:
                    return matching[0]
                return None
            return phases[0]

        model_property_ids = {
            str(model.get("property_observation_id") or "")
            for model in _as_list(payload.get("machine_learning_models"))
            if isinstance(model, dict) and model.get("property_observation_id")
        }
        filtered_property_ids: set[str] = set()
        for index, observation in enumerate(_as_list(payload.get("property_observations")), 1):
            if not isinstance(observation, dict):
                continue
            local_id = str(observation.get("id") or f"observation_{index}")
            performance_kind = _property_kind(observation, model_property_ids)
            if not performance_kind:
                # Keep qualitative, test-parameter, microstructural and other
                # non-performance measurements out of the Property layer and
                # any later relation that still references them.
                filtered_property_ids.add(local_id)
                continue
            sample_id = str(observation.get("sample_id") or "")
            sample_key = local_map.get(sample_id)
            if performance_kind == "material" and not sample_key:
                # A material performance value without a resolved material is
                # not useful in the graph and would create a floating metric.
                filtered_property_ids.add(local_id)
                continue
            property_name = _safe_name(observation.get("property"), f"Property observation {index}")
            value = _property_value_label(observation)
            unit = observation.get("unit")
            display = f"{property_name}: {value} {unit or ''}".strip()
            key = _local_key(document_id, local_id)
            local_map[local_id] = key
            evidence = _evidence(observation.get("evidence"), document_id, source_name, chunk_id)
            attributes = {item: value_ for item, value_ in observation.items() if item not in {"id", "evidence"}}
            attributes["performance_kind"] = performance_kind
            _insert_node(
                connection,
                node_key=key,
                document_id=document_id,
                local_id=local_id,
                entity_type="Property",
                name=display.strip(),
                canonical_name=property_name,
                sample_key=sample_key,
                material_state=observation.get("material_state"),
                attributes=attributes,
                evidence=evidence,
                source_document_id=document_id,
                source_name=source_name,
            )
            process = process_anchor(sample_id, observation.get("material_state"))
            observation_source = process["key"] if process else sample_key
            if observation_source:
                add_edge(
                    observation_source,
                    "HAS_PROPERTY_OBSERVATION",
                    key,
                    sample_key=sample_key,
                    material_state=observation.get("material_state"),
                    attributes=attributes,
                    evidence=evidence,
                )

        for index, mechanism in enumerate(_as_list(payload.get("mechanisms")), 1):
            if not isinstance(mechanism, dict):
                continue
            local_id = str(mechanism.get("id") or f"mechanism_{index}")
            name = _safe_name(mechanism.get("name"), f"Mechanism {index}")
            key = _concept_key("Mechanism", name)
            local_map[local_id] = key
            sample_id = str(mechanism.get("sample_id") or "")
            sample_key = local_map.get(sample_id)
            evidence = _evidence(mechanism.get("evidence"), document_id, source_name, chunk_id)
            _insert_node(
                connection,
                node_key=key,
                document_id=None,
                local_id=local_id,
                entity_type="Mechanism",
                name=name,
                material_state=mechanism.get("material_state"),
                attributes={"category": mechanism.get("category")},
                evidence=evidence,
                source_document_id=document_id,
                source_name=source_name,
            )
            phase = phase_anchor(sample_id, mechanism.get("material_state"))
            process = process_anchor(sample_id, mechanism.get("material_state"))
            mechanism_source = (
                phase["key"] if phase else process["key"] if process else sample_key
            )
            if mechanism_source:
                add_edge(
                    mechanism_source,
                    "ASSOCIATED_WITH_MECHANISM",
                    key,
                    sample_key=sample_key,
                    material_state=mechanism.get("material_state"),
                    assertion_level=mechanism.get("assertion_level"),
                    evidence=evidence,
                )

        for index, model in enumerate(_as_list(payload.get("machine_learning_models")), 1):
            if not isinstance(model, dict):
                continue
            local_id = str(model.get("id") or f"ml_model_{index}")
            name = _safe_name(model.get("name"), f"Machine learning model {index}")
            key = _concept_key("MachineLearningModel", name)
            local_map[local_id] = key
            sample_key = local_map.get(str(model.get("sample_id") or ""))
            evidence = _evidence(model.get("evidence"), document_id, source_name, chunk_id)
            attributes = {
                field: model.get(field)
                for field in ("task", "inputs", "target", "dataset", "validation", "metrics")
                if model.get(field) not in (None, "", [], {})
            }
            _insert_node(
                connection,
                node_key=key,
                document_id=None,
                local_id=local_id,
                entity_type="MachineLearningModel",
                name=name,
                attributes=attributes,
                evidence=evidence,
                source_document_id=document_id,
                source_name=source_name,
            )
            if sample_key:
                add_edge(sample_key, "USES_MODEL", key, sample_key=sample_key, attributes=attributes, evidence=evidence)
            observation_key = local_map.get(str(model.get("property_observation_id") or ""))
            if observation_key:
                add_edge(key, "PREDICTS", observation_key, sample_key=sample_key, attributes=attributes, evidence=evidence)

        for index, relation in enumerate(_as_list(payload.get("relations")), 1):
            if not isinstance(relation, dict):
                continue
            source_id = str(relation.get("source_id") or "")
            target_id = str(relation.get("target_id") or "")
            if not source_id or not target_id:
                continue
            if source_id in filtered_property_ids or target_id in filtered_property_ids:
                continue
            source_key = local_map.get(source_id)
            target_key = local_map.get(target_id)
            for local_id, resolved in ((source_id, source_key), (target_id, target_key)):
                if resolved:
                    continue
                unknown_key = _local_key(document_id, f"unresolved_{local_id}")
                _insert_node(
                    connection,
                    node_key=unknown_key,
                    document_id=document_id,
                    local_id=local_id,
                    entity_type="UnresolvedEntity",
                    name=local_id,
                    evidence=[],
                    source_document_id=document_id,
                    source_name=source_name,
                )
                local_map[local_id] = unknown_key
            source_key = local_map[source_id]
            target_key = local_map[target_id]
            sample_key = local_map.get(str(relation.get("sample_id") or ""))
            evidence = _evidence(relation.get("evidence"), document_id, source_name, chunk_id)
            predicate, original_predicate = _normalize_predicate(relation.get("predicate"))
            relation_attributes = {
                "conditions": _as_dict(relation.get("conditions")),
                "claim_id": relation.get("id"),
            }
            if original_predicate:
                relation_attributes["original_predicate"] = original_predicate
            add_edge(
                source_key,
                predicate,
                target_key,
                sample_key=sample_key,
                material_state=relation.get("material_state"),
                polarity=relation.get("polarity"),
                assertion_level=relation.get("assertion_level"),
                attributes=relation_attributes,
                evidence=evidence,
            )

        # Remove shared concepts that became orphaned after a forced replacement.
        orphans = connection.execute(
            """
            SELECT n.node_key FROM nodes n
            LEFT JOIN edges es ON es.source_key=n.node_key
            LEFT JOIN edges et ON et.target_key=n.node_key
            LEFT JOIN node_sources ns ON ns.node_key=n.node_key
            WHERE n.document_id IS NULL AND es.edge_key IS NULL
              AND et.edge_key IS NULL AND ns.node_key IS NULL
            """
        ).fetchall()
        for row in orphans:
            connection.execute("DELETE FROM node_fts WHERE node_key=?", (row[0],))
            connection.execute("DELETE FROM nodes WHERE node_key=?", (row[0],))

        node_count = connection.execute(
            """
            SELECT COUNT(DISTINCT node_key) FROM (
                SELECT node_key FROM node_sources WHERE document_id=?
                UNION SELECT node_key FROM nodes WHERE document_id=?
            )
            """,
            (document_id, document_id),
        ).fetchone()[0]
        edge_count = connection.execute("SELECT COUNT(*) FROM edges WHERE document_id=?", (document_id,)).fetchone()[0]
        connection.execute(
            """
            INSERT OR REPLACE INTO graph_papers(
                document_id, name, document_type, status, themes, graph_path, source_chunks,
                node_count, edge_count, prompt_tokens, completion_tokens, error, updated_at
            ) VALUES (?, ?, ?, 'complete', ?, ?, ?, ?, ?, ?, ?, NULL, ?)
            """,
            (
                document_id,
                source_name,
                str(document.get("document_type") or "literature"),
                _json(themes),
                graph_path,
                source_chunks,
                node_count,
                edge_count,
                int(usage.get("prompt_tokens", 0) or 0),
                int(usage.get("completion_tokens", 0) or 0),
                _now(),
            ),
        )
        return {"nodes": int(node_count), "edges": int(edge_count)}


def record_graph_failure(document: dict, error: str, themes: list[str] | None = None) -> None:
    with _LOCK, closing(_connect()) as connection, connection:
        connection.execute(
            """
            INSERT INTO graph_papers(
                document_id, name, document_type, status, themes, error, updated_at
            )
            VALUES (?, ?, ?, 'failed', ?, ?, ?)
            ON CONFLICT(document_id) DO UPDATE SET
                document_type=excluded.document_type, status='failed',
                themes=excluded.themes, error=excluded.error,
                updated_at=excluded.updated_at
            """,
            (
                document["id"],
                document["name"],
                str(document.get("document_type") or "literature"),
                _json(themes or []),
                error[:4000],
                _now(),
            ),
        )


def graph_stats() -> dict[str, int]:
    with closing(_connect()) as connection, connection:
        return {
            "papers": connection.execute("SELECT COUNT(*) FROM graph_papers WHERE status='complete'").fetchone()[0],
            "failed": connection.execute("SELECT COUNT(*) FROM graph_papers WHERE status='failed'").fetchone()[0],
            "nodes": connection.execute("SELECT COUNT(*) FROM nodes").fetchone()[0],
            "edges": connection.execute("SELECT COUNT(*) FROM edges").fetchone()[0],
            "observations": connection.execute("SELECT COUNT(*) FROM nodes WHERE type='Property'").fetchone()[0],
            "post_treatments": connection.execute(
                "SELECT COUNT(*) FROM nodes WHERE type='PostTreatment'"
            ).fetchone()[0],
            "fabrication_processes": connection.execute(
                "SELECT COUNT(*) FROM nodes WHERE type='FabricationProcess'"
            ).fetchone()[0],
        }


def parsed_corpus_stats() -> dict[str, int]:
    """Summarize only papers that have a completed GraphRAG extraction."""
    with closing(_connect()) as connection:
        papers = connection.execute(
            """
            SELECT gp.document_id, gp.name, gp.name AS title, gp.document_type
            FROM graph_papers gp
            WHERE gp.status='complete'
            ORDER BY gp.document_id
            """
        ).fetchall()
        relations = int(
            connection.execute(
                "SELECT COUNT(*) FROM (SELECT 1 FROM edges GROUP BY source_key, predicate, target_key)"
            ).fetchone()[0]
        )
        alloys = int(
            connection.execute("SELECT COUNT(*) FROM nodes WHERE type='Composition'").fetchone()[0]
        )

    document_ids = [str(row["document_id"]) for row in papers]
    sampled_text: dict[str, str] = {}
    searchable_chunks = 0
    if document_ids and LITERATURE_DB_PATH.exists():
        with closing(sqlite3.connect(LITERATURE_DB_PATH)) as literature:
            placeholders = ",".join("?" for _ in document_ids)
            searchable_chunks = int(
                literature.execute(
                    f"""
                    SELECT COUNT(*) FROM chunks
                    WHERE document_id IN ({placeholders}) AND kind='original_text'
                    """,
                    document_ids,
                ).fetchone()[0]
            )
            for document_id in document_ids:
                rows = literature.execute(
                    """
                    SELECT text FROM chunks
                    WHERE document_id=? AND kind='original_text'
                    ORDER BY id LIMIT 8
                    """,
                    (document_id,),
                ).fetchall()
                sampled_text[document_id] = "".join(str(row[0] or "") for row in rows)[:50000]

    patent_pattern = re.compile(
        r"(?i)\bpatent\b|专利|(?:^|[\s_(.\-])(?:CN|US|EP|WO|JP|KR)[-_ ]?\d{6,}[A-Z]?\d?(?:[\s_).\-]|$)"
    )
    chinese_papers = 0
    english_papers = 0
    patents = 0
    for row in papers:
        identity = f"{row['name']} {row['title']}"
        if str(row["document_type"] or "").casefold() == "patent" or patent_pattern.search(identity):
            patents += 1
            continue
        text = sampled_text.get(str(row["document_id"]), "")
        cjk_count = len(re.findall(r"[\u3400-\u9fff]", text))
        latin_count = len(re.findall(r"[A-Za-z]", text))
        is_chinese = cjk_count >= 40 and cjk_count / max(cjk_count + latin_count, 1) >= 0.08
        if is_chinese:
            chinese_papers += 1
        else:
            english_papers += 1

    return {
        "papers": len(papers),
        "chinese_papers": chinese_papers,
        "english_papers": english_papers,
        "patents": patents,
        "chunks": searchable_chunks,
        "relations": relations,
        "alloys": alloys,
    }


def _decode_row(row: sqlite3.Row) -> dict:
    value = dict(row)
    for key in ("attributes_json", "evidence_json"):
        if key in value:
            try:
                value[key.removesuffix("_json")] = json.loads(value.pop(key) or ("[]" if key.startswith("evidence") else "{}"))
            except json.JSONDecodeError:
                value[key.removesuffix("_json")] = [] if key.startswith("evidence") else {}
    return value


def _aggregate_graph_edges(edges: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Collapse visually identical cross-paper claims while retaining all evidence."""
    grouped: dict[tuple[str, str, str], dict[str, Any]] = {}
    assertion_rank = {
        "experimentally_observed": 0,
        "directly_reported": 1,
        "author_interpretation": 2,
        "author_hypothesis": 3,
    }
    for edge in edges:
        marker = (
            str(edge.get("source_key") or ""),
            str(edge.get("predicate") or ""),
            str(edge.get("target_key") or ""),
        )
        if marker not in grouped:
            grouped[marker] = dict(edge)
            grouped[marker]["evidence"] = []
            grouped[marker]["document_ids"] = []
        merged = grouped[marker]
        document_id = str(edge.get("document_id") or "")
        if document_id and document_id not in merged["document_ids"]:
            merged["document_ids"].append(document_id)
        existing_assertion = str(merged.get("assertion_level") or "")
        candidate_assertion = str(edge.get("assertion_level") or "")
        if assertion_rank.get(candidate_assertion, 99) < assertion_rank.get(existing_assertion, 99):
            merged["assertion_level"] = candidate_assertion
        seen_evidence = {
            (
                str(item.get("document_id") or ""),
                str(item.get("page") or ""),
                str(item.get("quote") or ""),
            )
            for item in merged["evidence"]
            if isinstance(item, dict)
        }
        for item in _as_list(edge.get("evidence")):
            if not isinstance(item, dict):
                continue
            evidence_marker = (
                str(item.get("document_id") or ""),
                str(item.get("page") or ""),
                str(item.get("quote") or ""),
            )
            if evidence_marker not in seen_evidence:
                merged["evidence"].append(item)
                seen_evidence.add(evidence_marker)
    output = []
    for marker, edge in grouped.items():
        edge["edge_key"] = "aggregate:" + hashlib.sha1("|".join(marker).encode("utf-8")).hexdigest()
        attributes = _as_dict(edge.get("attributes"))
        edge["attributes"] = {**attributes, "supporting_documents": len(edge["document_ids"])}
        output.append(edge)
    return output


def _graph_request_limits(max_nodes: Any, hops: Any, total_nodes: int) -> tuple[int, int]:
    """Normalize user-defined graph limits against the actual database size."""
    try:
        requested_nodes = max(10, int(float(max_nodes)))
    except (TypeError, ValueError, OverflowError):
        requested_nodes = 60
    try:
        requested_hops = max(1, int(float(hops)))
    except (TypeError, ValueError, OverflowError):
        requested_hops = 1
    if total_nodes <= 0:
        return 0, requested_hops
    return min(requested_nodes, total_nodes), min(requested_hops, max(1, total_nodes - 1))


def search_subgraph(query: str = "", max_nodes: int = 60, hops: int = 1) -> dict[str, Any]:
    """Return a bounded evidence subgraph around lexical seed nodes."""
    with closing(_connect()) as connection, connection:
        total_nodes = int(connection.execute("SELECT COUNT(*) FROM nodes").fetchone()[0])
        max_nodes, hops = _graph_request_limits(max_nodes, hops, total_nodes)
        if max_nodes == 0:
            return {"nodes": [], "edges": [], "seed_keys": []}
        if query.strip():
            tokens = list(dict.fromkeys(_search_tokens(_expand_query(query)).split()))[:60]
            if not tokens:
                seed_rows = []
            else:
                expression = " OR ".join('"' + token.replace('"', '""') + '"' for token in tokens)
                seed_rows = connection.execute(
                    """
                    SELECT n.* FROM node_fts f
                    JOIN nodes n ON n.node_key=f.node_key
                    WHERE node_fts MATCH ?
                    ORDER BY bm25(node_fts) LIMIT ?
                    """,
                    (expression, min(30, max(5, max_nodes // 2))),
                ).fetchall()
        else:
            ranked_rows = connection.execute(
                """
                SELECT n.*, COUNT(e.edge_key) degree FROM nodes n
                JOIN edges e ON e.source_key=n.node_key OR e.target_key=n.node_key
                WHERE n.type NOT IN ('UnresolvedEntity', 'MaterialState', 'TestCondition')
                GROUP BY n.node_key ORDER BY degree DESC, n.name COLLATE NOCASE
                """
            ).fetchall()
            # A global overview must not be made only of high-degree hubs.
            # First preserve entity-type coverage, then add extra scientific
            # identity nodes and finally fill with the strongest hubs.
            seed_target = min(max_nodes, max(30, min(72, max_nodes // 4)))
            by_type: dict[str, list[sqlite3.Row]] = {}
            for row in ranked_rows:
                by_type.setdefault(str(row["type"]), []).append(row)
            identity_types = ("Alloy", "Composition", "Element", "Phase")
            type_order = list(identity_types) + sorted(set(by_type) - set(identity_types))
            seed_rows = []
            seeded_keys: set[str] = set()

            def add_seed(row: sqlite3.Row) -> None:
                if row["node_key"] not in seeded_keys and len(seed_rows) < seed_target:
                    seed_rows.append(row)
                    seeded_keys.add(row["node_key"])

            # At least one representative of every available type.
            for entity_type in type_order:
                if by_type.get(entity_type):
                    add_seed(by_type[entity_type][0])
            # Preserve scientific type coverage in a global overview. Earlier
            # versions over-weighted identity hubs, so even a 300-node view
            # could contain only one PostTreatment and a few Properties despite
            # thousands being present in the database.
            overview_quotas = {
                "Alloy": 4,
                "Composition": 4,
                "Element": 4,
                "Phase": 4,
                "PostTreatment": max(4, min(12, max_nodes // 25)),
                "Property": max(4, min(16, max_nodes // 20)),
                "FabricationProcess": max(3, min(10, max_nodes // 30)),
                "Sample": max(3, min(8, max_nodes // 40)),
                "Mechanism": 3,
                "Microstructure": 2,
                "Defect": 2,
                "MachineLearningModel": 2,
            }
            for rank in range(1, max(overview_quotas.values())):
                for entity_type in type_order:
                    if rank >= overview_quotas.get(entity_type, 1):
                        continue
                    candidates = by_type.get(entity_type, [])
                    if len(candidates) > rank:
                        add_seed(candidates[rank])
            for row in ranked_rows:
                add_seed(row)
                if len(seed_rows) >= seed_target:
                    break

        seed_keys = {row["node_key"] for row in seed_rows}
        selected = set(seed_keys)
        selected_edges: dict[str, sqlite3.Row] = {}

        def include_edge(row: sqlite3.Row) -> bool:
            additions = {
                key
                for key in (row["source_key"], row["target_key"])
                if key not in selected
            }
            if len(selected) + len(additions) > max_nodes:
                return False
            selected.update(additions)
            selected_edges[row["edge_key"]] = row
            return True

        # Every seed must bring at least one real relation into the bounded
        # graph. This prevents type-balanced sampling from creating floating
        # dots whose neighbours were lost at the node cap.
        seed_priority = {
            "PostTreatment": 0,
            "FabricationProcess": 1,
            "Property": 2,
            "MachineLearningModel": 3,
        }
        seed_types = {str(row["node_key"]): str(row["type"]) for row in seed_rows}
        ordered_seed_keys = sorted(
            seed_keys,
            key=lambda key: (seed_priority.get(seed_types.get(key, ""), 4), key),
        )
        for seed_key in ordered_seed_keys:
            incident = connection.execute(
                """
                SELECT * FROM edges
                WHERE source_key=? OR target_key=?
                ORDER BY CASE predicate
                    WHEN 'HAS_COMPOSITION' THEN 0
                    WHEN 'FABRICATED_BY' THEN 1
                    WHEN 'FOLLOWED_BY' THEN 2
                    WHEN 'PRODUCES' THEN 3
                    WHEN 'HAS_SAMPLE' THEN 4
                    WHEN 'CONTAINS_ELEMENT' THEN 5
                    WHEN 'CONTAINS_PHASE' THEN 6
                    WHEN 'HAS_PROPERTY_OBSERVATION' THEN 7
                    ELSE 8 END,
                    CASE assertion_level
                    WHEN 'experimentally_observed' THEN 0
                    WHEN 'directly_reported' THEN 1
                    WHEN 'author_interpretation' THEN 2 ELSE 3 END
                """,
                (seed_key, seed_key),
            ).fetchall()
            for row in incident:
                if include_edge(row):
                    break

        # Preserve one complete directed material route for every material or
        # process seed: Alloy -> Composition -> Process -> ... -> Sample.
        # A process is therefore never shown as if its physical sample were
        # absent merely because the overview is node-limited.
        route_predicates = {"HAS_COMPOSITION", "FABRICATED_BY", "FOLLOWED_BY", "PRODUCES", "HAS_SAMPLE"}
        route_rows = connection.execute(
            """
            SELECT * FROM edges
            WHERE predicate IN ('HAS_COMPOSITION','FABRICATED_BY','FOLLOWED_BY','PRODUCES','HAS_SAMPLE')
            ORDER BY CASE predicate
                WHEN 'HAS_COMPOSITION' THEN 0
                WHEN 'FABRICATED_BY' THEN 1
                WHEN 'FOLLOWED_BY' THEN 2
                WHEN 'PRODUCES' THEN 3 ELSE 4 END,
                edge_key
            """
        ).fetchall()
        outgoing_routes: dict[str, list[sqlite3.Row]] = {}
        for row in route_rows:
            outgoing_routes.setdefault(str(row["source_key"]), []).append(row)
        node_types = {
            str(row["node_key"]): str(row["type"])
            for row in connection.execute("SELECT node_key, type FROM nodes")
        }

        def shortest_sample_route(root: str) -> list[sqlite3.Row]:
            queue: list[tuple[str, list[sqlite3.Row]]] = [(root, [])]
            visited = {root}
            while queue:
                current, path = queue.pop(0)
                if current != root and node_types.get(current) == "Sample":
                    return path
                for edge in outgoing_routes.get(current, []):
                    target = str(edge["target_key"])
                    if target in visited or edge["predicate"] not in route_predicates:
                        continue
                    visited.add(target)
                    queue.append((target, [*path, edge]))
            return []

        route_root_types = {"Alloy", "Composition", "Element", "FabricationProcess", "PostTreatment"}
        for seed_key in sorted(
            seed_keys,
            key=lambda key: (seed_priority.get(node_types.get(key, ""), 4), key),
        ):
            if node_types.get(seed_key) not in route_root_types:
                continue
            route = shortest_sample_route(seed_key)
            additions = {
                key
                for edge in route
                for key in (edge["source_key"], edge["target_key"])
                if key not in selected
            }
            if len(selected) + len(additions) <= max_nodes:
                for edge in route:
                    include_edge(edge)

        frontier = set(selected)
        for _ in range(hops):
            if not frontier or len(selected) >= max_nodes:
                break
            placeholders = ",".join("?" for _ in frontier)
            rows = connection.execute(
                f"""
                SELECT * FROM edges
                WHERE source_key IN ({placeholders}) OR target_key IN ({placeholders})
                ORDER BY CASE assertion_level
                    WHEN 'experimentally_observed' THEN 0
                    WHEN 'directly_reported' THEN 1
                    WHEN 'author_interpretation' THEN 2 ELSE 3 END,
                    predicate
                LIMIT ?
                """,
                (*frontier, *frontier, max_nodes * 5),
            ).fetchall()
            next_frontier: set[str] = set()
            for row in rows:
                other_keys = (row["source_key"], row["target_key"])
                if not any(key in selected for key in other_keys):
                    continue
                additions = [key for key in other_keys if key not in selected]
                if additions and len(selected) + len(additions) > max_nodes:
                    continue
                selected.update(additions)
                next_frontier.update(additions)
                selected_edges[row["edge_key"]] = row
            frontier = next_frontier

        if not selected:
            return {"nodes": [], "edges": [], "seed_keys": []}
        placeholders = ",".join("?" for _ in selected)
        # Include edges among already selected nodes even if a cap skipped them.
        edge_rows = connection.execute(
            f"""
            SELECT * FROM edges WHERE source_key IN ({placeholders})
            AND target_key IN ({placeholders}) LIMIT ?
            """,
            (*selected, *selected, max_nodes * 6),
        ).fetchall()
        for row in edge_rows:
            selected_edges[row["edge_key"]] = row

        # An execution node without its downstream Sample is visually
        # misleading. Remove only cap-truncated process nodes; the complete
        # process remains searchable and will reappear whenever its route fits.
        selected_route_outgoing: dict[str, list[str]] = {}
        for row in selected_edges.values():
            if row["predicate"] in route_predicates:
                selected_route_outgoing.setdefault(str(row["source_key"]), []).append(
                    str(row["target_key"])
                )

        def reaches_selected_sample(root: str) -> bool:
            pending = [root]
            visited = {root}
            while pending:
                current = pending.pop()
                for target in selected_route_outgoing.get(current, []):
                    if target not in selected or target in visited:
                        continue
                    if node_types.get(target) == "Sample":
                        return True
                    visited.add(target)
                    pending.append(target)
            return False

        incomplete_processes = {
            key
            for key in selected
            if node_types.get(key) in {"FabricationProcess", "PostTreatment"}
            and not reaches_selected_sample(key)
        }
        selected.difference_update(incomplete_processes)
        selected_edges = {
            edge_key: row
            for edge_key, row in selected_edges.items()
            if row["source_key"] in selected and row["target_key"] in selected
        }
        connected = {
            key
            for row in selected_edges.values()
            for key in (row["source_key"], row["target_key"])
            if key in selected
        }
        selected.intersection_update(connected)
        if not selected:
            return {"nodes": [], "edges": [], "seed_keys": []}
        placeholders = ",".join("?" for _ in selected)
        node_rows = connection.execute(
            f"SELECT * FROM nodes WHERE node_key IN ({placeholders})", tuple(selected)
        ).fetchall()
        return {
            "nodes": [_decode_row(row) for row in node_rows],
            "edges": _aggregate_graph_edges(
                [_decode_row(row) for row in selected_edges.values()]
            ),
            # Preserve the lexical/FTS seeds separately from their expanded
            # neighbours so the UI can show what the graph search matched.
            "seed_keys": sorted(seed_keys.intersection(selected)),
        }


def graph_evidence(
    query: str,
    limit: int | None = None,
    max_nodes: int = 160,
    hops: int = 2,
) -> list[dict[str, Any]]:
    """Return query-centred graph evidence ranked by topology and provenance.

    ``limit=None`` intentionally means that no arbitrary top-k is applied.
    The answer pipeline can then use one shared context budget for graph and
    source-text evidence instead of silently discarding graph relations first.
    """
    graph = search_subgraph(query, max_nodes=max_nodes, hops=hops)
    node_names = {
        str(node.get("node_key") or ""): str(node.get("name") or "")
        for node in graph["nodes"]
    }
    query_tokens = [
        token
        for token in dict.fromkeys(_search_tokens(query).split())
        if token not in {
            "a", "an", "and", "are", "does", "for", "how", "in", "is",
            "of", "on", "or", "the", "to", "what", "which", "with",
        }
    ]
    adjacency: dict[str, set[str]] = {}
    for edge in graph["edges"]:
        source_key = str(edge.get("source_key") or "")
        target_key = str(edge.get("target_key") or "")
        if source_key and target_key:
            adjacency.setdefault(source_key, set()).add(target_key)
            adjacency.setdefault(target_key, set()).add(source_key)

    distances: dict[str, int] = {}
    frontier = [str(key) for key in graph.get("seed_keys", [])]
    for key in frontier:
        distances[key] = 0
    while frontier:
        current = frontier.pop(0)
        for neighbour in adjacency.get(current, set()):
            if neighbour in distances:
                continue
            distances[neighbour] = distances[current] + 1
            frontier.append(neighbour)

    lowered_query = str(query or "").casefold()
    property_intent = any(
        token in lowered_query
        for token in (
            "strength", "ductility", "elongation", "hardness", "creep",
            "oxidation", "property", "performance", "强度", "塑性", "硬度",
            "蠕变", "氧化", "性能",
        )
    )
    mechanism_intent = any(
        token in lowered_query
        for token in ("mechanism", "strengthening", "机理", "机制", "强化")
    )
    candidates: dict[tuple[str, str, str], dict[str, Any]] = {}
    for edge in graph["edges"]:
        relation = str(edge.get("predicate") or "")
        edge_distance = min(
            distances.get(str(edge.get("source_key") or ""), hops + 2),
            distances.get(str(edge.get("target_key") or ""), hops + 2),
        )
        topology_score = max(0.0, 12.0 - 5.0 * edge_distance)
        assertion_level = str(edge.get("assertion_level") or "")
        quality_score = {
            "experimentally_observed": 5.0,
            "directly_reported": 3.0,
            "author_interpretation": 1.0,
        }.get(assertion_level, 0.0)
        intent_score = 0.0
        if property_intent and relation in {
            "HAS_PROPERTY_OBSERVATION", "AFFECTS_PROPERTY", "IMPROVES",
            "INCREASES", "DECREASES", "DEGRADES", "CAUSES_TRADEOFF",
        }:
            intent_score += 6.0
        if mechanism_intent and relation in {
            "EXPLAINED_BY", "HAS_MECHANISM", "AFFECTS_MECHANISM",
            "STRENGTHENS_BY", "ASSOCIATED_WITH_MECHANISM",
            "ACTIVATES_MECHANISM",
        }:
            intent_score += 6.0
        for evidence in _as_list(edge.get("evidence")):
            quote = str(evidence.get("quote") or "").strip()
            source = str(evidence.get("source") or "Unknown source")
            if not quote:
                continue
            marker = (source, str(evidence.get("page") or ""), quote)
            context = " ".join(
                (
                    quote,
                    relation.replace("_", " "),
                    node_names.get(str(edge.get("source_key") or ""), ""),
                    node_names.get(str(edge.get("target_key") or ""), ""),
                )
            ).casefold()
            matched_tokens = sum(1 for token in query_tokens if token.casefold() in context)
            coverage = matched_tokens / len(query_tokens) if query_tokens else 0.0
            evidence_score = min(
                100.0,
                42.0
                + 38.0 * coverage
                + topology_score
                + quality_score
                + intent_score
                + (3.0 if re.search(r"\d", quote) else 0.0),
            )
            item = {
                "document_id": evidence.get("document_id"),
                "source": source,
                "page": evidence.get("page"),
                "kind": "graph_evidence",
                "relation": relation,
                "text": f"[Graph relation: {relation}] {quote}",
                "score": round(evidence_score, 2),
                "relevance": round(evidence_score, 2),
                "graph_distance": edge_distance,
                "assertion_level": assertion_level,
            }
            previous = candidates.get(marker)
            if previous is None or evidence_score > float(previous.get("relevance", 0.0)):
                candidates[marker] = item
    output = sorted(
        candidates.values(),
        key=lambda item: (
            float(item.get("relevance", 0.0)),
            -int(item.get("graph_distance", hops + 2)),
        ),
        reverse=True,
    )
    return output if limit is None else output[: max(0, int(limit))]


def active_graph_document_ids() -> list[str]:
    """Return document IDs in the currently active GraphRAG corpus."""
    with closing(_connect()) as connection:
        return [
            str(row["document_id"])
            for row in connection.execute(
                "SELECT DISTINCT document_id FROM graph_papers "
                "WHERE status='complete' ORDER BY document_id"
            ).fetchall()
        ]


def _usable_bibliographic_value(value: Any) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip().strip("*_")
    lowered = text.casefold()
    missing_markers = (
        "not explicitly stated",
        "not provided",
        "not available",
        "unknown",
        "n/a",
        "none",
        "null",
    )
    return "" if not text or any(marker in lowered for marker in missing_markers) else text


def _parse_structured_paper_metadata(text: str) -> dict[str, Any]:
    """Parse the Paper Metadata block already produced during RAG ingestion."""
    content = str(text or "")
    heading = re.search(r"(?im)^#\s+Paper Metadata\s*$", content)
    if heading:
        start = heading.end()
        next_heading = re.search(r"(?m)^#\s+", content[start:])
        content = content[start : start + next_heading.start()] if next_heading else content[start:]
    else:
        content = content[:8000]

    fields: dict[str, str] = {}
    pattern = re.compile(
        r"(?im)^\s*[-*]\s+\*{0,2}\s*(Title|Authors?|Journal|Year|DOI)"
        r"\s*:?\s*\*{0,2}\s*:?\s*(.+?)\s*$"
    )
    for match in pattern.finditer(content):
        key = match.group(1).casefold()
        key = "authors" if key.startswith("author") else key
        value = _usable_bibliographic_value(match.group(2))
        if value and key not in fields:
            fields[key] = value

    if fields.get("authors"):
        fields["authors"] = [
            author.strip()
            for author in re.split(r"\s*(?:,|;|；|、)\s*", fields["authors"])
            if author.strip()
        ]
    if fields.get("year"):
        year_match = re.search(r"\b(?:18|19|20)\d{2}\b", fields["year"])
        if year_match:
            fields["year"] = year_match.group(0)
    if fields.get("doi"):
        fields["doi"] = re.sub(
            r"^https?://(?:dx\.)?doi\.org/",
            "",
            fields["doi"],
            flags=re.IGNORECASE,
        ).rstrip(". ")
    return fields


def _structured_citation_entries() -> list[dict[str, Any]]:
    """Load bibliographic fields for the original structured-RAG corpus."""
    if not LITERATURE_DB_PATH.exists() or not STRUCTURED_DIR.exists():
        return []
    try:
        with closing(sqlite3.connect(LITERATURE_DB_PATH)) as connection:
            connection.row_factory = sqlite3.Row
            rows = connection.execute(
                "SELECT id, name, markdown_path FROM documents WHERE structured=1"
            ).fetchall()
    except sqlite3.Error:
        return []

    entries: list[dict[str, Any]] = []
    for row in rows:
        markdown_name = Path(str(row["markdown_path"]).replace("\\", "/")).name
        structured_path = STRUCTURED_DIR / markdown_name
        if not structured_path.exists():
            continue
        try:
            metadata = _parse_structured_paper_metadata(
                structured_path.read_text(encoding="utf-8", errors="replace")
            )
        except OSError:
            continue
        entries.append(
            {
                "document_id": str(row["id"]),
                "source": str(row["name"] or ""),
                "title": metadata.get("title"),
                "authors": metadata.get("authors"),
                "journal": metadata.get("journal"),
                "year": metadata.get("year"),
                "doi": metadata.get("doi"),
            }
        )
    return entries


def citation_metadata_index(
    document_ids: list[str] | tuple[str, ...] | set[str] | None = None,
) -> dict[str, dict[str, dict[str, Any]]]:
    """Return bibliography metadata extracted by the active GraphRAG pipeline.

    Legacy structured-RAG cards are deliberately not read here. This keeps
    citations, retrieval, and graph extraction on the same newly extracted
    500-paper corpus.
    """
    by_document_id: dict[str, dict[str, Any]] = {}
    by_source: dict[str, dict[str, Any]] = {}

    requested_ids = list(dict.fromkeys(str(value) for value in document_ids or [] if str(value)))
    with closing(_connect()) as connection:
        if document_ids is not None and not requested_ids:
            rows = []
        elif requested_ids:
            placeholders = ",".join("?" for _ in requested_ids)
            rows = connection.execute(
                f"""
                SELECT gp.document_id, gp.name AS source_name, gp.graph_path
                FROM graph_papers gp
                WHERE gp.status='complete' AND gp.document_id IN ({placeholders})
                """,
                requested_ids,
            ).fetchall()
        else:
            rows = connection.execute(
                """
                SELECT gp.document_id, gp.name AS source_name, gp.graph_path
                FROM graph_papers gp
                WHERE gp.status='complete'
                """
            ).fetchall()
    for row in rows:
        metadata = {}
        graph_path = Path(str(row["graph_path"] or ""))
        if not graph_path.is_absolute():
            graph_path = BASE_DIR / graph_path
        if graph_path.exists():
            try:
                metadata = _as_dict(json.loads(graph_path.read_text(encoding="utf-8", errors="replace")).get("paper_metadata"))
            except (OSError, TypeError, json.JSONDecodeError):
                metadata = {}
        graph_entry = {
            "document_id": str(row["document_id"]),
            "source": str(row["source_name"] or ""),
            "title": metadata.get("title"),
            "authors": metadata.get("authors"),
            "journal": metadata.get("journal"),
            "year": metadata.get("year"),
            "doi": metadata.get("doi"),
        }
        entry = dict(by_document_id.get(graph_entry["document_id"], {}))
        entry.update(
            {
                key: value
                for key, value in graph_entry.items()
                if key in {"document_id", "source"} or _usable_bibliographic_value(value)
            }
        )
        by_document_id[entry["document_id"]] = entry
        for source in (entry["source"], metadata.get("file_name")):
            if source:
                by_source[str(source).casefold()] = entry
    return {"by_document_id": by_document_id, "by_source": by_source}


NODE_COLORS = {
    "Alloy": "#00B8D9",
    "Composition": "#7C3AED",
    "Element": "#22C55E",
    "Sample": "#2563EB",
    "FabricationProcess": "#F59E0B",
    "PostTreatment": "#F97316",
    "Phase": "#D946EF",
    "Microstructure": "#38BDF8",
    "Defect": "#EF4444",
    "Mechanism": "#84CC16",
    "Property": "#EC4899",
    "MachineLearningModel": "#6366F1",
    "UnresolvedEntity": "#64748B",
}

NODE_SHAPES = {entity_type: "dot" for entity_type in NODE_COLORS}

NODE_TYPE_LABELS = {
    "Alloy": "Alloy",
    "Composition": "Composition",
    "Element": "Element",
    "Sample": "Sample",
    "FabricationProcess": "Fabrication Process",
    "PostTreatment": "Post Treatment",
    "Phase": "Phase",
    "Microstructure": "Microstructure",
    "Defect": "Defect",
    "Mechanism": "Mechanism",
    "Property": "Property",
    "MachineLearningModel": "Machine Learning Model",
    "UnresolvedEntity": "Unresolved Entity",
}

ASSERTION_STYLES = {
    "experimentally_observed": ("Experimentally Observed", "rgba(177, 184, 198, 0.52)", 1.35),
    "directly_reported": ("Directly Reported", "rgba(145, 153, 169, 0.38)", 1.05),
    "author_interpretation": ("Author Interpretation", "rgba(117, 124, 139, 0.28)", 0.85),
    "inferred": ("Inferred", "rgba(93, 99, 112, 0.20)", 0.7),
}

NODE_NAME_TRANSLATIONS = {
    "yield strength": "Yield strength",
    "ultimate tensile strength": "Ultimate tensile strength",
    "tensile strength": "Tensile strength",
    "compressive strength": "Compressive strength",
    "elongation": "Elongation",
    "plastic fracture strain": "Plastic fracture strain",
    "fracture toughness": "Fracture toughness",
    "relative density": "Relative density",
    "elastic modulus": "Elastic modulus",
    "hardness": "Hardness",
    "creep rate": "Creep rate",
    "creep stress exponent n": "Creep stress exponent n",
    "dbtt": "Ductile-to-brittle transition temperature (DBTT)",
    "cof": "Coefficient of friction (COF)",
    "dislocation climb": "Dislocation climb",
    "dislocation strengthening": "Dislocation strengthening",
    "solid solution strengthening": "Solid-solution strengthening",
    "solid-solution strengthening": "Solid-solution strengthening",
    "precipitation strengthening": "Precipitation strengthening",
    "dispersion strengthening": "Dispersion strengthening",
    "carbide dispersion strengthening": "Carbide dispersion strengthening",
    "grain boundary strengthening": "Grain-boundary strengthening",
    "hall-petch grain boundary strengthening": "Hall–Petch grain-boundary strengthening",
    "hall-petch strengthening": "Hall–Petch strengthening",
    "grain refinement": "Grain refinement",
    "grain refinement strengthening": "Grain-refinement strengthening",
    "second phase strengthening": "Second-phase strengthening",
    "second-phase strengthening": "Second-phase strengthening",
    "vacuum arc melting": "Vacuum arc melting",
    "arc melting": "Arc melting",
    "annealing": "Annealing",
    "homogenization heat treatment": "Homogenization heat treatment",
    "hot rolling": "Hot rolling",
    "cold rolling": "Cold rolling",
    "ball milling": "Ball milling",
    "mechanical alloying": "Mechanical alloying",
    "mechanical alloying (ma)": "Mechanical alloying (MA)",
    "spark plasma sintering": "Spark plasma sintering (SPS)",
    "spark plasma sintering (sps)": "Spark plasma sintering (SPS)",
    "cold isostatic pressing": "Cold isostatic pressing",
    "gas atomization": "Gas atomization",
    "solution treatment": "Solution treatment",
    "isothermal oxidation": "Isothermal oxidation",
    "oxidation test": "Oxidation test",
    "neutron irradiation": "Neutron irradiation",
    "laser powder bed fusion (lpbf)": "Laser powder bed fusion (LPBF)",
    "gtaw rotary waam additive manufacturing": "GTAW rotary-arc WAAM",
    "columnar grains": "Columnar grains",
    "columnar grain": "Columnar grain",
    "equiaxed grains": "Equiaxed grains",
    "equiaxed grain": "Equiaxed grain",
    "average grain size": "Average grain size",
    "grain size": "Grain size",
    "dendritic microstructure": "Dendritic microstructure",
    "dendritic structure": "Dendritic structure",
    "cellular subgrain structure": "Cellular subgrain structure",
    "low angle grain boundaries (lagbs)": "Low-angle grain boundaries (LAGBs)",
    "lagbs": "Low-angle grain boundaries (LAGBs)",
    "dislocation tangles": "Dislocation tangles",
    "dislocations": "Dislocations",
    "subgrains": "Subgrains",
    "second phase particles": "Second-phase particles",
    "bcc matrix": "BCC matrix",
    "bcc phase": "BCC phase",
    "bcc solid solution phase": "BCC solid-solution phase",
    "fcc solid solution phase": "FCC solid-solution phase",
    "laves phase": "Laves phase",
    "zro2 dispersoid": "ZrO₂ dispersoid",
}

PREDICATE_LABELS = {
    "INSTANCE_OF": "Is instance of",
    "CONTAINS_ELEMENT": "Contains element",
    "HAS_PROPERTY_OBSERVATION": "Has property data",
    "UNDERGOES_PROCESS": "Undergoes process",
    "FABRICATED_BY": "Fabricated by",
    "PRODUCES": "Produces",
    "FOLLOWED_BY": "Followed by",
    "OBSERVED_AFTER_PROCESS": "Observed after process",
    "ASSOCIATED_WITH_MECHANISM": "Associated with mechanism",
    "HAS_COMPOSITION": "Has composition",
    "HAS_SAMPLE": "Has sample",
    "HAS_DEFECT": "Has defect",
    "USES_MODEL": "Uses model",
    "PREDICTS": "Predicts",
    "CONTAINS_PHASE": "Contains phase",
    "HAS_MICROSTRUCTURE": "Has microstructure",
    "ACTIVATES_MECHANISM": "Activates mechanism",
    "IMPROVES": "Improves",
    "COMPARED_WITH": "Compared with",
    "INCREASES": "Increases",
    "CAUSES_TRADEOFF": "Causes trade-off",
    "PROMOTES": "Promotes",
    "DECREASES": "Decreases",
    "SUPPRESSES": "Suppresses",
    "DEGRADES": "Degrades",
    "CORRELATES_WITH": "Correlates with",
    "REFINES": "Refines",
    "FORMS": "Forms",
    "TRANSFORMS_TO": "Transforms to",
    "LOCATED_AT": "Located at",
}


ELEMENT_SYMBOLS = {
    symbol.casefold(): symbol
    for symbol in (
        "Ag Al Ar As Au B Ba Be Bi Br C Ca Cd Ce Cl Co Cr Cs Cu Dy Er Eu F Fe "
        "Gd Ge H He Hf Hg Ho I In Ir K Kr La Li Lu Mg Mn Mo N Na Nb Nd Ne Ni "
        "O Os P Pa Pb Pd Pm Po Pr Pt Ra Rb Re Rh Ru S Sb Sc Se Si Sm Sn Sr Ta "
        "Tb Tc Te Th Ti Tl Tm U V W Xe Y Yb Zn Zr"
    ).split()
}

ALLOY_ACRONYMS = {
    "ebm": "EBM",
    "hea": "HEA",
    "lpbf": "LPBF",
    "ma": "MA",
    "mpea": "MPEA",
    "ods": "ODS",
    "rhea": "RHEA",
    "slm": "SLM",
    "sps": "SPS",
    "tzm": "TZM",
    "vim": "VIM",
    "waam": "WAAM",
}
NON_FORMULA_TOKENS = {
    "alloy",
    "as",
    "at",
    "base",
    "based",
    "doped",
    "free",
    "matrix",
    "part",
    "powder",
    "pure",
    "reinforced",
    "sample",
    "sintered",
    "specimen",
    "vol",
    "wt",
}

# Core labels identify the material itself. Process, condition, property and
# mechanism nodes remain visible and inspectable, but their text appears only
# in All-label mode, on search, or while focusing a neighborhood.
CORE_LABEL_QUOTAS = {
    "Alloy": 8,
    "Composition": 10,
    "Element": 10,
    "Phase": 8,
}
CORE_LABEL_PRIORITY = {name: len(CORE_LABEL_QUOTAS) - index for index, name in enumerate(CORE_LABEL_QUOTAS)}


def _format_alloy_canonical(value: Any) -> str:
    """Restore chemical-symbol casing in lowercased canonical alloy names."""
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if not text:
        return ""

    def format_token(match: re.Match[str]) -> str:
        token = match.group(0)
        lowered = token.casefold()
        if lowered in ALLOY_ACRONYMS:
            return ALLOY_ACRONYMS[lowered]
        if lowered in NON_FORMULA_TOKENS:
            return lowered
        output: list[str] = []
        index = 0
        while index < len(token):
            if token[index].isdigit() or token[index] == ".":
                output.append(token[index])
                index += 1
                continue
            symbol = None
            for width in (2, 1):
                candidate = token[index : index + width].casefold()
                if candidate in ELEMENT_SYMBOLS:
                    symbol = ELEMENT_SYMBOLS[candidate]
                    break
            if symbol is None:
                # Preserve known author designations instead of inventing a
                # chemical parsing for arbitrary letters.
                return token.upper() if any(char.isdigit() for char in token) else token
            output.append(symbol)
            index += len(symbol)
        return "".join(output)

    return re.sub(r"[A-Za-z][A-Za-z0-9.]*", format_token, text)


def _compact_name(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value or "").casefold())


def _contains_cjk(value: Any) -> bool:
    return bool(re.search(r"[\u3400-\u9fff]", str(value or "")))


def _looks_like_sample_reference(value: Any) -> bool:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return bool(
        "#" in text
        or re.fullmatch(r"(?i)(?:sample|specimen|alloy|build|part)\s*[-#]?[a-z0-9]+(?:\s*,\s*.+)?", text)
        or re.fullmatch(r"[A-Za-z]{1,7}\d{1,3}(?:[-_/][A-Za-z0-9*]+)*", text)
    )


def _looks_like_state_description(value: Any) -> bool:
    return bool(
        re.search(
            r"(?i)\b(?:annealed|aged|as-built|as-cast|as-deposited|deformed|"
            r"formed layer|heat-treated|irradiated|milled|oxidized|rolled|"
            r"sintered|solution-treated)\b|°\s*c|℃",
            str(value or ""),
        )
    )


def _alloy_sample_display_name(
    original: str,
    canonical_name: Any,
    alloy_system_name: Any,
    material_state: Any = None,
) -> str:
    """Show a scientific composition identity without author sample codes."""
    canonical = _format_alloy_canonical(canonical_name)
    system = re.sub(r"\s+", " ", str(alloy_system_name or "")).strip()
    if canonical and not _is_opaque_sample_name(canonical) and not _contains_cjk(canonical):
        return canonical
    cleaned_original = _format_alloy_canonical(original)
    if (
        cleaned_original
        and not _is_opaque_sample_name(cleaned_original)
        and not _looks_like_state_description(cleaned_original)
        and not _contains_cjk(cleaned_original)
    ):
        return cleaned_original
    if system and not _contains_cjk(system):
        return system
    return "Unresolved composition"

    # Legacy alias formatting is intentionally unreachable. It is retained
    # below only so older saved data can still be inspected during migration.
    state = re.sub(r"\s+", " ", str(material_state or "")).strip()

    # Non-English source designations remain available in Original designation
    # and evidence, but the canvas follows the application's English-only rule.
    if _contains_cjk(original):
        identity = canonical if canonical and not _contains_cjk(canonical) else system
        if not identity or _contains_cjk(identity):
            identity = "Unresolved alloy sample"
        descriptor = state if state and not _contains_cjk(state) else ""
        if re.search(r"(?:铸?锭)", original) and descriptor.casefold() == "as-cast":
            descriptor = "as-cast ingot"
        return f"{identity} · {descriptor}" if descriptor else identity

    original_key = _compact_name(original)
    canonical_key = _compact_name(canonical)
    if canonical and canonical_key and canonical_key != original_key and canonical_key not in original_key:
        if _looks_like_state_description(original):
            return f"{canonical} · {original}"
        return f"{original} · {canonical}"

    if _looks_like_sample_reference(original) and system:
        system_key = _compact_name(system)
        if system_key and system_key not in original_key:
            return f"{original} · {system}"
    return original


def _display_node_name(
    name: Any,
    entity_type: str | None = None,
    attributes: dict[str, Any] | None = None,
    canonical_name: Any = None,
    alloy_system_name: Any = None,
    material_state: Any = None,
) -> str:
    """Return a concise, type-aware label while retaining the original in tooltips."""
    original = re.sub(r"\s+", " ", str(name or "")).strip()
    if not original:
        return "Unnamed node"
    lowered = original.casefold()

    if entity_type == "Element" and lowered in ELEMENT_SYMBOLS:
        return ELEMENT_SYMBOLS[lowered]

    if entity_type == "Composition":
        concise = re.sub(
            r"\s+(?:formed\s+layer|alloy\s+sample|sample|specimen)$",
            "",
            original,
            flags=re.IGNORECASE,
        ).strip()
        if concise:
            original = concise
            lowered = original.casefold()
        return _alloy_sample_display_name(
            original,
            canonical_name,
            alloy_system_name,
            material_state,
        )
    if entity_type == "Sample":
        identity = _alloy_sample_display_name(
            original,
            canonical_name,
            alloy_system_name,
            material_state,
        )
        identity = re.sub(r"\s+(?:sample|specimen)$", "", identity, flags=re.I).strip()
        attributes = attributes or {}
        state = _clean_sample_qualifier(
            attributes.get("display_state") or attributes.get("source_material_state") or material_state
        )
        process = _clean_sample_qualifier(attributes.get("display_process"))
        if _contains_cjk(state):
            state = ""
        if _contains_cjk(process):
            process = ""
        variant_count = int(attributes.get("display_variant_count") or 0)
        variant_index = int(attributes.get("display_variant_index") or 0)
        qualifiers: list[str] = []
        # Put an unavoidable neutral specimen number first so truncation never
        # hides the distinction. It is not an author code or invented alloy ID.
        if variant_count > 1 and variant_index > 0:
            qualifiers.append(f"specimen {variant_index}")
        if state:
            qualifiers.append(state)
        if process:
            qualifiers.append(process)
        if identity and qualifiers:
            return " · ".join((identity, *qualifiers))
        return f"{identity} sample" if identity else "Material sample"

    if entity_type in {"FabricationProcess", "PostTreatment"}:
        base_name = NODE_NAME_TRANSLATIONS.get(lowered, original)
        parameters = _as_dict(_as_dict(attributes).get("parameters"))
        details: list[str] = []
        temperature = parameters.get("temperature_c")
        if temperature not in (None, ""):
            details.append(f"{_format_composition_number(temperature)} °C")
        duration = parameters.get("time")
        if duration not in (None, ""):
            details.append(_clean_sample_qualifier(duration))
        pressure = parameters.get("pressure")
        if pressure not in (None, ""):
            details.append(_clean_sample_qualifier(pressure))
        laser_power = parameters.get("laser_power_w")
        if laser_power not in (None, ""):
            details.append(f"{_format_composition_number(laser_power)} W")
        scan_speed = parameters.get("scan_speed")
        if scan_speed not in (None, ""):
            details.append(_clean_sample_qualifier(scan_speed))
        deformation = parameters.get("deformation")
        if deformation not in (None, "") and not details:
            details.append(_clean_sample_qualifier(deformation))
        return " · ".join((base_name, *details[:3]))

    if lowered in NODE_NAME_TRANSLATIONS:
        return NODE_NAME_TRANSLATIONS[lowered]
    for phrase in sorted(NODE_NAME_TRANSLATIONS, key=len, reverse=True):
        if lowered.startswith(phrase + ":"):
            suffix = original[len(phrase) + 1 :].strip()
            return f"{NODE_NAME_TRANSLATIONS[phrase]}: {suffix}"
    if entity_type == "Phase":
        phase_name = re.sub(
            r"^(bcc|fcc|hcp)(\d*)",
            lambda match: match.group(1).upper() + match.group(2),
            original,
            flags=re.IGNORECASE,
        )
        phase_name = re.sub(r"\s+phase$", " phase", phase_name, flags=re.IGNORECASE)
        return phase_name
    return original


def _sample_alloy_system_names(
    nodes: dict[str, dict[str, Any]],
    edges: list[dict[str, Any]],
) -> dict[str, str]:
    """Resolve Alloy context through Alloy -> Composition -> Sample paths."""
    systems: dict[str, str] = {}
    for edge in edges:
        if edge.get("predicate") != "HAS_COMPOSITION":
            continue
        source_key = str(edge.get("source_key") or "")
        target_key = str(edge.get("target_key") or "")
        source = nodes.get(source_key)
        target = nodes.get(target_key)
        if not source or not target:
            continue
        if source.get("type") == "Alloy" and target.get("type") == "Composition":
            systems[target_key] = str(source.get("name") or "").strip()
    # Older local graphs may have Composition -> HAS_SAMPLE.  Newer graphs
    # intentionally use Composition -> Fabrication -> ... -> PRODUCES ->
    # Sample, so resolve the Alloy context by walking that route backwards.
    incoming: dict[str, list[dict[str, Any]]] = {}
    for edge in edges:
        incoming.setdefault(str(edge.get("target_key") or ""), []).append(edge)

    for sample_key, sample in nodes.items():
        if sample.get("type") != "Sample":
            continue
        frontier = [sample_key]
        visited: set[str] = set()
        while frontier and sample_key not in systems:
            current = frontier.pop()
            if current in visited:
                continue
            visited.add(current)
            for edge in incoming.get(current, []):
                predicate = str(edge.get("predicate") or "")
                source_key = str(edge.get("source_key") or "")
                source = nodes.get(source_key)
                if not source:
                    continue
                if source.get("type") == "Composition":
                    systems[sample_key] = systems.get(source_key, "")
                    break
                if predicate in {"HAS_SAMPLE", "PRODUCES", "FOLLOWED_BY", "FABRICATED_BY"}:
                    frontier.append(source_key)
    return systems


def _graph_display_names(
    nodes: dict[str, dict[str, Any]],
    edges: list[dict[str, Any]],
) -> tuple[dict[str, str], dict[str, str]]:
    """Build one consistent display label per node for canvas, edges and details."""
    sample_systems = _sample_alloy_system_names(nodes, edges)
    display_names = {
        key: _display_node_name(
            node.get("name"),
            node.get("type"),
            _as_dict(node.get("attributes")),
            node.get("canonical_name"),
            sample_systems.get(key),
            node.get("material_state"),
        )
        for key, node in nodes.items()
    }
    return display_names, sample_systems


def _short_graph_label(label: str, limit: int = 30) -> str:
    """Keep canvas labels compact; the detail card always shows the full label."""
    clean = re.sub(r"\s+", " ", str(label or "")).strip()
    if len(clean) <= limit:
        return clean
    return clean[: limit - 1].rstrip() + "…"


def _is_core_label_candidate(node: dict[str, Any]) -> bool:
    """Reject generated IDs and sentence-like legacy names from the core view."""
    raw = re.sub(r"\s+", " ", str(node.get("name") or "")).strip()
    if not raw or raw.startswith(("local:", "concept:")):
        return False
    entity_type = str(node.get("type") or "")
    displayed = _display_node_name(
        raw,
        entity_type,
        _as_dict(node.get("attributes")),
        node.get("canonical_name"),
    )
    if entity_type == "Sample" and raw.casefold() in {
        "powder",
        "virgin powder",
        "recycled powder",
        "as-cast sample",
        "as-built sample",
    }:
        return False
    if entity_type == "Property" and not re.search(r"\d", raw):
        return False
    if entity_type == "Mechanism" and re.search(
        r"\b(?:causes?|decreases?|degrades?|enhances?|improves?|increases?|"
        r"inhibits?|leads?|promotes?|reduces?|refines?|retards?|suppresses?)\b",
        raw,
        flags=re.IGNORECASE,
    ):
        return False
    if entity_type in {
        "Mechanism",
        "FabricationProcess",
        "PostTreatment",
        "Phase",
        "Microstructure",
        "Defect",
        "MachineLearningModel",
    }:
        # A scientific entity label should be a noun phrase, not an extracted
        # conclusion. Long legacy phrases remain searchable and visible in the
        # details card or in "all labels" mode.
        if len(displayed) > 52 or len(displayed.split()) > 8:
            return False
    return True


def _select_core_labels(
    nodes: dict[str, dict[str, Any]],
    degrees: dict[str, int],
    matched_keys: set[str],
) -> set[str]:
    """Choose readable labels with coverage across scientific entity types."""
    budget = max(12, min(30, round(len(nodes) * 0.42)))
    selected = {
        key for key in matched_keys if nodes.get(key, {}).get("type") in CORE_LABEL_QUOTAS
    }
    eligible = [
        key
        for key, node in nodes.items()
        if node.get("type") in CORE_LABEL_QUOTAS
        and _is_core_label_candidate(node)
    ]
    ranked = sorted(
        eligible,
        key=lambda key: (
            -CORE_LABEL_PRIORITY.get(nodes[key].get("type", ""), 0),
            -degrees.get(key, 0),
            str(nodes[key].get("name") or "").casefold(),
        ),
    )

    # First guarantee one representative label for every semantic type present.
    for entity_type in CORE_LABEL_QUOTAS:
        candidate = next((key for key in ranked if nodes[key].get("type") == entity_type), None)
        if candidate:
            selected.add(candidate)

    # Then fill each type up to its quota, followed by the best remaining nodes.
    for entity_type, quota in CORE_LABEL_QUOTAS.items():
        candidates = [key for key in ranked if nodes[key].get("type") == entity_type]
        already_selected = sum(1 for key in candidates if key in selected)
        for key in candidates:
            if len(selected) >= budget or already_selected >= quota:
                break
            if key not in selected:
                selected.add(key)
                already_selected += 1
        if len(selected) >= budget:
            break
    if len(selected) < budget:
        selected.update(key for key in ranked if key not in selected and len(selected) < budget)
    return selected


def _display_predicate(predicate: Any) -> str:
    value = str(predicate or "").strip()
    return PREDICATE_LABELS.get(value, value.replace("_", " ").title())


def _query_matches_node(query: str, node: dict[str, Any]) -> bool:
    """Return whether a node should receive the search-result halo."""
    if not query.strip():
        return False
    haystack = " ".join(
        (
            str(node.get("name") or ""),
            str(node.get("canonical_name") or ""),
            json.dumps(_as_dict(node.get("attributes")), ensure_ascii=False),
        )
    ).casefold()
    raw_query = query.strip().casefold()
    if raw_query in haystack:
        return True
    tokens = re.findall(r"[a-z0-9]+(?:[-_.][a-z0-9]+)*|[\u4e00-\u9fff]{2,}", raw_query)
    meaningful = [token for token in tokens if len(token) >= 2]
    return bool(meaningful) and all(token in haystack for token in meaningful)


def make_graph_figure(query: str = "", max_nodes: int = 60, hops: int = 1):
    """Create an Obsidian-inspired interactive Plotly network and edge table."""
    import networkx as nx
    import plotly.graph_objects as go

    subgraph = search_subgraph(query, max_nodes=max_nodes, hops=hops)
    nodes = {node["node_key"]: node for node in subgraph["nodes"]}
    edges = [edge for edge in subgraph["edges"] if edge["source_key"] in nodes and edge["target_key"] in nodes]
    if not nodes:
        figure = go.Figure()
        figure.add_annotation(
            text="No matching graph nodes were found",
            showarrow=False,
            font={"size": 18, "color": "#C8CBD4"},
        )
        figure.update_layout(
            height=720,
            paper_bgcolor="#111318",
            plot_bgcolor="#111318",
            margin={"l": 0, "r": 0, "t": 0, "b": 0},
            xaxis={"visible": False},
            yaxis={"visible": False},
        )
        return figure, [], "No matching nodes were found. Try another composition, phase, process, or property."

    display_names, sample_systems = _graph_display_names(nodes, edges)

    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    for edge in edges:
        source_key = edge["source_key"]
        target_key = edge["target_key"]
        if graph.has_edge(source_key, target_key):
            graph[source_key][target_key]["weight"] += 1
        else:
            graph.add_edge(source_key, target_key, weight=1)

    # A stable spring layout keeps the graph recognizable between refreshes.
    spacing = max(0.75, 4.4 / max(len(nodes), 1) ** 0.5)
    positions = nx.spring_layout(
        graph,
        seed=42,
        k=spacing,
        iterations=180,
        weight="weight",
        scale=1.15,
    )
    degrees = dict(graph.degree())
    matched_keys = {key for key, node in nodes.items() if _query_matches_node(query, node)}
    labelled_keys = _select_core_labels(nodes, degrees, matched_keys)

    figure = go.Figure()
    midpoint_x: list[float] = []
    midpoint_y: list[float] = []
    midpoint_hover: list[str] = []
    edge_table: list[list[str]] = []
    styled_edges: dict[str, tuple[list[float | None], list[float | None]]] = {}
    for edge in edges:
        x0, y0 = positions[edge["source_key"]]
        x1, y1 = positions[edge["target_key"]]
        assertion = edge.get("assertion_level") or "inferred"
        edge_x, edge_y = styled_edges.setdefault(assertion, ([], []))
        edge_x.extend((x0, x1, None))
        edge_y.extend((y0, y1, None))
        source_name = display_names[edge["source_key"]]
        target_name = display_names[edge["target_key"]]
        evidence = _as_list(edge.get("evidence"))
        quote = str(evidence[0].get("quote") or "")[:240] if evidence else ""
        assertion_label = ASSERTION_STYLES.get(assertion, (assertion, "", 0))[0]
        midpoint_x.append((x0 + x1) / 2)
        midpoint_y.append((y0 + y1) / 2)
        midpoint_hover.append(
            f"<b>{source_name}</b> → <b>{target_name}</b>"
            f"<br><span style='color:#A9AFBD'>{edge['predicate']} · {assertion_label}</span>"
            + (f"<br><br>{quote}" if quote else "")
        )
        edge_table.append([source_name, edge["predicate"], target_name, edge.get("assertion_level") or "", quote])

    assertion_order = list(ASSERTION_STYLES) + sorted(set(styled_edges) - set(ASSERTION_STYLES))
    for assertion in assertion_order:
        if assertion not in styled_edges:
            continue
        edge_x, edge_y = styled_edges[assertion]
        assertion_label, color, width = ASSERTION_STYLES.get(
            assertion, (assertion, "rgba(117, 124, 139, 0.25)", 0.8)
        )
        figure.add_trace(
            go.Scatter(
                x=edge_x,
                y=edge_y,
                mode="lines",
                line={"width": width, "color": color},
                hoverinfo="skip",
                name=assertion_label,
                legendgroup="evidence",
                showlegend=False,
            )
        )
    figure.add_trace(
        go.Scatter(
            x=midpoint_x,
            y=midpoint_y,
            mode="markers",
            marker={"size": 11, "color": "rgba(0,0,0,0)"},
            hovertext=midpoint_hover,
            hoverinfo="text",
            showlegend=False,
        )
    )

    types = sorted({node["type"] for node in nodes.values()})
    for entity_type in types:
        keys = [key for key, node in nodes.items() if node["type"] == entity_type]
        x_values = [positions[key][0] for key in keys]
        y_values = [positions[key][1] for key in keys]
        labels = [display_names[key] for key in keys]
        hover: list[str] = []
        for key in keys:
            node = nodes[key]
            attributes = _as_dict(node.get("attributes"))
            details = "<br>".join(
                f"{field}: {str(value)[:160]}" for field, value in list(attributes.items())[:8] if value not in (None, "", [], {})
            )
            evidence = _as_list(node.get("evidence"))
            quote = str(evidence[0].get("quote") or "")[:260] if evidence else ""
            hover.append(
                f"<b>{display_names[key]}</b>"
                f"<br><span style='color:#A9AFBD'>Type: {NODE_TYPE_LABELS.get(entity_type, entity_type)}"
                f" · Connections: {degrees.get(key, 0)}</span>"
                + (
                    f"<br>Source designation: {attributes.get('source_designation')}"
                    if entity_type == "Sample" and attributes.get("source_designation")
                    else ""
                )
                + (
                    f"<br>Canonical identity: {_format_alloy_canonical(node.get('canonical_name'))}"
                    if entity_type in {"Composition", "Sample"} and node.get("canonical_name")
                    else ""
                )
                + (
                    f"<br>Alloy system: {sample_systems[key]}"
                    if entity_type in {"Composition", "Sample"} and sample_systems.get(key)
                    else ""
                )
                + (f"<br>State: {node['material_state']}" if node.get("material_state") else "")
                + (f"<br>{details}" if details else "")
                + (f"<br><br>Evidence: {quote}" if quote else "")
            )
        node_sizes = [
            min(31, 9 + 3.2 * degrees.get(key, 0) ** 0.5) + (3 if key in matched_keys else 0)
            for key in keys
        ]
        figure.add_trace(
            go.Scatter(
                x=x_values,
                y=y_values,
                mode="markers+text",
                text=[
                    (label if len(label) <= 22 else label[:20] + "…") if key in labelled_keys else ""
                    for key, label in zip(keys, labels)
                ],
                textposition="top center",
                textfont={"size": 10, "color": "#D9DCE5"},
                name=NODE_TYPE_LABELS.get(entity_type, entity_type),
                customdata=keys,
                hovertext=hover,
                hoverinfo="text",
                marker={
                    "size": node_sizes,
                    "color": NODE_COLORS.get(entity_type, "#9B9B9B"),
                    "line": {
                        "width": [3.2 if key in matched_keys else 0.8 for key in keys],
                        "color": ["#F4F0FF" if key in matched_keys else "#292D36" for key in keys],
                    },
                    "opacity": 0.94,
                },
                selected={"marker": {"opacity": 1.0}},
                unselected={"marker": {"opacity": 0.18}, "textfont": {"color": "rgba(217,220,229,0.25)"}},
            )
        )

    figure.update_layout(
        height=760,
        paper_bgcolor="#111318",
        plot_bgcolor="#111318",
        font={"family": "Inter, Segoe UI, Microsoft YaHei, sans-serif", "color": "#C8CBD4"},
        title={
            "text": f"<b>{query or 'Global Knowledge Graph'}</b><br><sup>{len(nodes)} nodes · {len(edges)} relations</sup>",
            "x": 0.025,
            "y": 0.975,
            "font": {"size": 17, "color": "#E7E9EF"},
        },
        hovermode="closest",
        clickmode="event+select",
        dragmode="pan",
        margin={"l": 8, "r": 8, "t": 68, "b": 40},
        legend={
            "orientation": "h",
            "yanchor": "top",
            "y": -0.015,
            "x": 0.01,
            "font": {"size": 10, "color": "#A9AFBD"},
            "bgcolor": "rgba(0,0,0,0)",
            "itemsizing": "constant",
        },
        hoverlabel={
            "bgcolor": "#20232B",
            "bordercolor": "#4B5060",
            "font": {"color": "#F1F2F6", "size": 12},
            "align": "left",
        },
        xaxis={"visible": False, "fixedrange": False},
        yaxis={"visible": False, "fixedrange": False, "scaleanchor": "x", "scaleratio": 1},
        uirevision=f"obsidian:{query}:{max_nodes}:{hops}",
        selectionrevision=f"obsidian:{query}:{max_nodes}:{hops}",
    )
    status = (
        f"Showing {len(nodes)} nodes and {len(edges)} relations. Node size represents connection count. "
        "Only core nodes are labeled to reduce overlap. Hover to inspect evidence, drag to pan, "
        "and use the mouse wheel or toolbar to zoom."
    )
    return figure, edge_table, status


def make_graph_html(query: str = "", max_nodes: int = 60, hops: int = 1):
    """Create a self-contained 2D/3D interactive graph in an iframe."""
    import networkx as nx
    from pyvis.network import Network

    subgraph = search_subgraph(query, max_nodes=max_nodes, hops=hops)
    nodes = {node["node_key"]: node for node in subgraph["nodes"]}
    edges = [
        edge
        for edge in subgraph["edges"]
        if edge["source_key"] in nodes and edge["target_key"] in nodes
    ]
    if not nodes:
        empty = """
        <div style="height:740px;display:grid;place-items:center;background:#111318;color:#c8cbd4;
                    font:16px 'Segoe UI','Microsoft YaHei',sans-serif;border-radius:14px">
          No matching graph nodes were found
        </div>
        """
        return empty, [], [], "No matching nodes were found. Try another composition, phase, process, or property."

    display_names, sample_systems = _graph_display_names(nodes, edges)

    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    for edge in edges:
        graph.add_edge(edge["source_key"], edge["target_key"])
    degrees = dict(graph.degree())
    seed_keys = {
        str(key)
        for key in _as_list(subgraph.get("seed_keys"))
        if str(key) in nodes
    }
    lexical_matches = {key for key, node in nodes.items() if _query_matches_node(query, node)}
    matched_keys = (seed_keys | lexical_matches) if query.strip() else set()
    labelled_keys = _select_core_labels(nodes, degrees, matched_keys)
    three_nodes: list[dict[str, Any]] = []
    query_active = bool(query.strip())
    muted_node_color = "#555B66"
    muted_node_border = "#3D424C"
    muted_font_color = "#858B97"

    matched_node_rows = [
        [
            display_names[key],
            NODE_TYPE_LABELS.get(nodes[key]["type"], nodes[key]["type"]),
            degrees.get(key, 0),
            sample_systems.get(key, ""),
            str(nodes[key].get("material_state") or ""),
        ]
        for key in matched_keys
    ]
    matched_node_rows.sort(
        key=lambda row: (-int(row[2]), str(row[1]).casefold(), str(row[0]).casefold())
    )

    network = Network(
        height="100%",
        width="100%",
        directed=True,
        bgcolor="#111318",
        font_color="#D9DCE5",
        cdn_resources="in_line",
    )

    present_types = sorted(
        {node["type"] for node in nodes.values()},
        key=lambda entity_type: NODE_TYPE_LABELS.get(entity_type, entity_type),
    )
    group_options = {
        entity_type: {
            "shape": NODE_SHAPES.get(entity_type, "dot"),
            "color": {
                "background": NODE_COLORS.get(entity_type, "#8B91A0"),
                "border": "#2B2F39",
                "highlight": {
                    "background": NODE_COLORS.get(entity_type, "#8B91A0"),
                    "border": "#F4F0FF",
                },
                "hover": {
                    "background": NODE_COLORS.get(entity_type, "#8B91A0"),
                    "border": "#D8D0FF",
                },
            }
        }
        for entity_type in present_types
    }

    def safe_text(value: Any, limit: int = 500) -> str:
        text = str(value or "")[:limit]
        return text.replace("<", "‹").replace(">", "›")

    for key, node in nodes.items():
        attributes = _as_dict(node.get("attributes"))
        evidence = _as_list(node.get("evidence"))
        detail_rows = [
            f"<div><b>Type</b><span>{html_lib.escape(NODE_TYPE_LABELS.get(node['type'], node['type']))}</span></div>",
            f"<div><b>Connections</b><span>{degrees.get(key, 0)}</span></div>",
        ]
        if node.get("material_state"):
            detail_rows.append(
                f"<div><b>Material state</b><span>{html_lib.escape(str(node['material_state']))}</span></div>"
            )
        for field, value in list(attributes.items())[:8]:
            if value not in (None, "", [], {}):
                detail_rows.append(
                    f"<div><b>{html_lib.escape(str(field))}</b>"
                    f"<span>{html_lib.escape(str(value)[:240])}</span></div>"
                )
        if evidence:
            quote = str(evidence[0].get("quote") or "")[:420]
            if quote:
                detail_rows.append(
                    f"<div class='evidence'><b>Source evidence</b><span>{html_lib.escape(quote)}</span></div>"
                )
        original_name = safe_text(node["name"], 180)
        full_name = safe_text(display_names[key], 180)
        short_name = safe_text(_short_graph_label(full_name), 80)
        if node.get("type") == "Sample":
            source_designation = attributes.get("source_designation")
            if source_designation:
                detail_rows.insert(
                    1,
                    f"<div><b>Source designation</b><span>{html_lib.escape(str(source_designation))}</span></div>",
                )
        if node.get("type") in {"Composition", "Sample"}:
            canonical_identity = _format_alloy_canonical(node.get("canonical_name"))
            if canonical_identity and _compact_name(canonical_identity) != _compact_name(node.get("name")):
                detail_rows.insert(
                    2,
                    f"<div><b>Canonical identity</b><span>{html_lib.escape(canonical_identity)}</span></div>",
                )
            if sample_systems.get(key):
                detail_rows.insert(
                    3,
                    f"<div><b>Alloy system</b><span>{html_lib.escape(sample_systems[key])}</span></div>",
                )
        search_text = " ".join(
            (
                full_name,
                original_name,
                str(node.get("canonical_name") or ""),
                sample_systems.get(key, ""),
                node["type"],
                NODE_TYPE_LABELS.get(node["type"], node["type"]),
                json.dumps(attributes, ensure_ascii=False),
            )
        )
        matched = key in matched_keys
        base_color = NODE_COLORS.get(node["type"], "#8B91A0")
        muted = query_active and not matched
        display_color = muted_node_color if muted else base_color
        display_border = muted_node_border if muted else ("#F4F0FF" if matched else "#2B2F39")
        display_font = muted_font_color if muted else "#D9DCE5"
        network.add_node(
            key,
            # A single space is intentional: vis-network falls back to the technical
            # node ID when label is an empty string, exposing local:/concept: keys.
            label=short_name if key in labelled_keys else " ",
            title=f"{full_name} — {NODE_TYPE_LABELS.get(node['type'], node['type'])}",
            detailHtml=f"<div class='kg-tooltip'><h3>{html_lib.escape(full_name)}</h3>{''.join(detail_rows)}</div>",
            group=node["type"],
            shape=NODE_SHAPES.get(node["type"], "dot"),
            size=min(34, 9 + 3.4 * degrees.get(key, 0) ** 0.5) + (3 if matched else 0),
            borderWidth=3.5 if matched else 1,
            borderWidthSelected=4,
            color={
                "background": display_color,
                "border": display_border,
                "highlight": {"background": display_color, "border": "#FFFFFF"},
                "hover": {"background": display_color, "border": "#D8D0FF"},
            },
            font={"color": display_font, "size": 13, "face": "Segoe UI, Microsoft YaHei"},
            fullLabel=full_name,
            shortLabel=short_name,
            coreLabel=short_name if key in labelled_keys else " ",
            searchText=safe_text(search_text.casefold(), 1800),
            baseColor=display_color,
            baseFontColor=display_font,
            originalColor=base_color,
            topSearchMatched=matched,
            topSearchMuted=muted,
            nodeType=node["type"],
        )
        three_nodes.append(
            {
                "id": key,
                "label": short_name if key in labelled_keys else "",
                "fullLabel": full_name,
                "detailHtml": f"<div class='kg-tooltip'><h3>{html_lib.escape(full_name)}</h3>{''.join(detail_rows)}</div>",
                "searchText": safe_text(search_text.casefold(), 1800),
                "nodeType": node["type"],
                "color": display_color,
                "originalColor": base_color,
                "topSearchMatched": matched,
                "topSearchMuted": muted,
                "size": min(17, 5 + 1.7 * degrees.get(key, 0) ** 0.5) + (1.8 if matched else 0),
                "degree": degrees.get(key, 0),
            }
        )

    edge_table: list[list[str]] = []
    edge_colors = {
        "experimentally_observed": "rgba(190,198,214,0.62)",
        "directly_reported": "rgba(155,164,183,0.46)",
        "author_interpretation": "rgba(122,130,148,0.34)",
        "inferred": "rgba(96,103,119,0.24)",
    }
    edge_widths = {
        "experimentally_observed": 1.7,
        "directly_reported": 1.3,
        "author_interpretation": 1.0,
        "inferred": 0.8,
    }
    for edge in edges:
        source_node = nodes[edge["source_key"]]
        target_node = nodes[edge["target_key"]]
        source_name = display_names[edge["source_key"]]
        target_name = display_names[edge["target_key"]]
        predicate_label = _display_predicate(edge["predicate"])
        assertion = edge.get("assertion_level") or "inferred"
        evidence = _as_list(edge.get("evidence"))
        quote = str(evidence[0].get("quote") or "")[:420] if evidence else ""
        assertion_label = ASSERTION_STYLES.get(assertion, (assertion, "", 0))[0]
        edge_title = (
            f"<div class='kg-tooltip'><h3>{html_lib.escape(str(source_name))} → "
            f"{html_lib.escape(str(target_name))}</h3>"
            f"<div><b>Relation</b><span>{html_lib.escape(predicate_label)}</span></div>"
            f"<div><b>Evidence level</b><span>{html_lib.escape(assertion_label)}</span></div>"
            + (
                f"<div class='evidence'><b>Source evidence</b><span>{html_lib.escape(quote)}</span></div>"
                if quote
                else ""
            )
            + "</div>"
        )
        base_edge_color = edge_colors.get(assertion, "rgba(122,130,148,0.30)")
        network.add_edge(
            edge["source_key"],
            edge["target_key"],
            id=edge["edge_key"],
            title=f"{source_name} → {target_name} — {predicate_label}",
            detailHtml=edge_title,
            width=edge_widths.get(assertion, 1.0),
            color={
                "color": base_edge_color,
                "highlight": "rgba(197,181,255,0.95)",
                "hover": "rgba(197,181,255,0.78)",
                "inherit": False,
            },
            arrows={"to": {"enabled": True, "scaleFactor": 0.38}},
            smooth={"enabled": True, "type": "dynamic", "roundness": 0.12},
            baseColor=base_edge_color,
            predicate=safe_text(predicate_label, 180),
        )
        edge_table.append([source_name, predicate_label, target_name, assertion_label, quote[:240]])

    three_data = {
        "nodes": three_nodes,
        "links": [
            {
                "source": edge["source_key"],
                "target": edge["target_key"],
                "color": edge_colors.get(edge.get("assertion_level") or "inferred", "rgba(122,130,148,0.30)"),
            }
            for edge in edges
        ],
    }
    # Avoid accidental script termination if an evidence quote contains a
    # literal HTML closing tag.  The graph itself remains entirely local.
    three_data_json = json.dumps(three_data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    options = {
        "autoResize": True,
        "layout": {"improvedLayout": True, "randomSeed": 42},
        "groups": group_options,
        "interaction": {
            "dragNodes": True,
            "dragView": True,
            "hover": True,
            "hoverConnectedEdges": True,
            "keyboard": {"enabled": True, "bindToWindow": False},
            "multiselect": True,
            "navigationButtons": False,
            "selectConnectedEdges": True,
            "tooltipDelay": 140,
            "zoomView": True,
            "hideEdgesOnDrag": True,
        },
        "nodes": {
            "shape": "dot",
            "chosen": True,
            "shadow": {"enabled": True, "color": "rgba(0,0,0,0.35)", "size": 8, "x": 0, "y": 3},
            "scaling": {"label": {"enabled": False, "min": 11, "max": 16, "drawThreshold": 2}},
        },
        "edges": {
            "chosen": True,
            "selectionWidth": 2.4,
            "hoverWidth": 1.5,
        },
        "physics": {
            "enabled": True,
            "solver": "forceAtlas2Based",
            "forceAtlas2Based": {
                "gravitationalConstant": -88,
                "centralGravity": 0.009,
                "springLength": 165,
                "springConstant": 0.055,
                "damping": 0.64,
                "avoidOverlap": 1.0,
            },
            "maxVelocity": 36,
            "minVelocity": 0.3,
            "stabilization": {"enabled": True, "iterations": 560, "updateInterval": 25, "fit": True},
        },
    }
    network.set_options(json.dumps(options, ensure_ascii=False))
    document = network.generate_html(notebook=False)
    force_graph_bundle_path = BASE_DIR / "node_modules" / "3d-force-graph" / "dist" / "3d-force-graph.min.js"
    try:
        force_graph_bundle = force_graph_bundle_path.read_text(encoding="utf-8")
    except OSError:
        force_graph_bundle = ""
    document = document.replace("</head>", f"<script>{force_graph_bundle}</script></head>")

    legend_buttons = "".join(
        f"<button class='kg-legend-item' data-group='{html_lib.escape(entity_type, quote=True)}'>"
        f"<i style='background:{NODE_COLORS.get(entity_type, '#8B91A0')}'></i>"
        f"{html_lib.escape(NODE_TYPE_LABELS.get(entity_type, entity_type))}</button>"
        for entity_type in present_types
    )
    custom_ui = """
    <style>
      html, body { width:100%; height:100%; margin:0; overflow:hidden; background:#111318; }
      body > .card { position:absolute !important; inset:0 !important; width:100% !important;
                     height:100% !important; margin:0 !important; padding:0 !important;
                     border:0 !important; border-radius:0 !important; background:#111318 !important; }
      #mynetwork { position:absolute !important; inset:0 !important; float:none !important;
                   width:100% !important; height:100% !important; margin:0 !important;
                   padding:0 !important; border:0 !important; background:#111318; }
      #kg-3d { position:absolute; inset:0; display:none; background:#111318; }
      #kg-3d > div, #kg-3d canvas { width:100% !important; height:100% !important; }
      #kg-3d-labels { position:absolute; z-index:8; inset:0; display:none; overflow:hidden;
                      pointer-events:none; }
      .kg-3d-label { position:absolute; max-width:180px; padding:2px 5px; transform:translate(-50%,-145%);
                     overflow:hidden; color:#e8eaf0; background:rgba(17,19,24,.72);
                     border:1px solid rgba(119,128,149,.32); border-radius:5px;
                     font:600 10px/1.25 'Segoe UI','Microsoft YaHei',sans-serif;
                     text-overflow:ellipsis; white-space:nowrap; text-shadow:0 1px 2px #000; }
      #kg-3d-labels.all-labels .kg-3d-label { width:max-content; max-width:min(360px,42vw);
                     overflow:visible; overflow-wrap:anywhere; text-overflow:clip; white-space:normal; }
      #kg-3d-hint { position:absolute; z-index:20; right:14px; bottom:14px; display:none; padding:7px 10px;
                     border:1px solid #343945; border-radius:8px; color:#aeb4c2; background:rgba(25,28,35,.88);
                     font:11px 'Segoe UI','Microsoft YaHei',sans-serif; pointer-events:none; }
      #kg-toolbar { position:absolute; z-index:20; top:12px; left:12px; right:12px; display:flex;
                    flex-wrap:wrap; gap:8px; align-items:center; pointer-events:none; }
      #kg-toolbar > * { pointer-events:auto; }
      #kg-search { width:min(310px,38vw); height:36px; box-sizing:border-box; padding:0 13px;
                   color:#e7e9ef; background:rgba(31,34,42,.94); border:1px solid #3b404d;
                   border-radius:9px; outline:none; font:13px 'Segoe UI','Microsoft YaHei',sans-serif; }
      #kg-search:focus { border-color:#8b7cf6; box-shadow:0 0 0 2px rgba(139,124,246,.18); }
      .kg-btn { height:36px; padding:0 12px; color:#cdd1db; background:rgba(31,34,42,.94);
                border:1px solid #3b404d; border-radius:9px; cursor:pointer; font:12px 'Segoe UI','Microsoft YaHei',sans-serif; }
      .kg-btn:hover, .kg-btn.active { color:#fff; border-color:#8b7cf6; background:#353047; }
      .kg-zoom { width:36px; padding:0; font-size:18px; line-height:34px; }
      #kg-match-count { color:#9ea4b2; font:12px 'Segoe UI','Microsoft YaHei',sans-serif; }
      #kg-loading { position:absolute; z-index:19; inset:0; display:grid; place-items:center; color:#aeb3c0;
                    background:rgba(17,19,24,.76); font:13px 'Segoe UI','Microsoft YaHei',sans-serif;
                    pointer-events:none; transition:opacity .3s; }
      #kg-legend { position:absolute; z-index:20; left:14px; bottom:12px; display:flex; flex-wrap:wrap;
                   gap:5px; max-width:calc(100% - 28px); }
      .kg-legend-item { display:flex; align-items:center; gap:6px; padding:5px 8px; color:#b9beca;
                        background:rgba(25,28,35,.86); border:1px solid #343945; border-radius:999px;
                        cursor:pointer; font:11px 'Segoe UI','Microsoft YaHei',sans-serif; }
      .kg-legend-item i { width:8px; height:8px; border-radius:50%; box-shadow:0 0 6px currentColor; }
      .kg-legend-item.off { opacity:.34; text-decoration:line-through; }
      #kg-details { position:absolute; z-index:30; top:58px; right:14px; width:min(370px,42vw); max-height:70%;
                    overflow:auto; display:none; padding:14px 16px; color:#d8dbe3; background:rgba(27,30,38,.96);
                    border:1px solid #424856; border-radius:12px; box-shadow:0 14px 40px rgba(0,0,0,.36);
                    font:12px/1.5 'Segoe UI','Microsoft YaHei',sans-serif; }
      #kg-details.open { display:block; }
      #kg-details-close { position:absolute; right:9px; top:7px; color:#9ca2b0; background:none; border:0;
                          cursor:pointer; font-size:18px; }
      .kg-tooltip h3 { margin:0 22px 10px 0; color:#f0f1f5; font-size:14px; }
      .kg-tooltip > div { display:grid; grid-template-columns:88px 1fr; gap:10px; margin:5px 0; }
      .kg-tooltip b { color:#9fa5b3; font-weight:600; }
      .kg-tooltip span { color:#dde0e7; overflow-wrap:anywhere; }
      .kg-tooltip .evidence { display:block; margin-top:12px; padding-top:10px; border-top:1px solid #3a3f4b; }
      .kg-tooltip .evidence b, .kg-tooltip .evidence span { display:block; }
      .kg-tooltip .evidence span { margin-top:5px; color:#bfc4cf; }
      #kg-3d-reheat { display:none; }
      body.kg-3d-active #kg-physics, body.kg-3d-active .kg-zoom { display:none; }
      body.kg-3d-active #kg-3d-reheat { display:inline-block; }
      body.kg-3d-active #kg-3d-hint { display:block; }
      body.kg-3d-active #kg-3d-labels { display:block; }
      @media (max-width:860px) { #kg-physics { display:none; } #kg-details { width:calc(100% - 60px); } }
    </style>
    <div id="kg-toolbar">
      <input id="kg-search" placeholder="Find nodes in this graph…" autocomplete="off">
      <button id="kg-dimension" class="kg-btn" title="Switch between 2D and 3D">View: 2D</button>
      <button id="kg-fit" class="kg-btn">Fit View</button>
      <button id="kg-3d-reheat" class="kg-btn" title="Re-run the 3D spring simulation">Reheat 3D</button>
      <button id="kg-labels" class="kg-btn active" title="Change node-label density">Labels: Core</button>
      <button id="kg-physics" class="kg-btn active">Physics: On</button>
      <button id="kg-zoom-out" class="kg-btn kg-zoom" title="Zoom out">−</button>
      <button id="kg-zoom-in" class="kg-btn kg-zoom" title="Zoom in">＋</button>
      <button id="kg-reset" class="kg-btn">Reset</button>
      <span id="kg-match-count"></span>
    </div>
    <div id="kg-loading">Computing physics layout…</div>
    <div id="kg-3d"></div>
    <div id="kg-3d-labels"></div>
    <div id="kg-3d-hint">3D physics · drag background to orbit · drag a node to move it · scroll to zoom</div>
    <div id="kg-legend">__LEGEND__</div>
    <aside id="kg-details"><button id="kg-details-close" title="Close">×</button><div id="kg-details-content"></div></aside>
    <script>
      (() => {
        const graph3dData = __THREE_DATA__;
        const hiddenGroups = new Set();
        let physicsOn = true;
        let labelMode = 'core';
        let labelFontSize = 13;
        let fontSyncTimer = null;
        let viewDimension = '2d';
        let graph3d = null;
        const details = document.getElementById('kg-details');
        const detailsContent = document.getElementById('kg-details-content');
        const searchInput = document.getElementById('kg-search');
        const matchCount = document.getElementById('kg-match-count');
        const graph3dContainer = document.getElementById('kg-3d');
        const graph3dLabels = document.getElementById('kg-3d-labels');
        const graph3dLabelElements = new Map();

        function groupHidden(node) { return hiddenGroups.has(node.nodeType); }
        function readableFont(color) {
          return {color:color, size:labelFontSize, face:'Segoe UI, Microsoft YaHei'};
        }
        function syncLabelFont() {
          // vis-network scales text with the canvas. Compensate so labels stay
          // close to 12 screen pixels in both overview and focused views.
          labelFontSize = Math.max(6, Math.min(38, 12 / Math.max(network.getScale(), .08)));
          nodes.update(nodes.get().map(n => ({id:n.id,
            font:readableFont(n.font && n.font.color ? n.font.color : '#D9DCE5')})));
        }
        function scheduleFontSync() {
          if (fontSyncTimer) clearTimeout(fontSyncTimer);
          fontSyncTimer = setTimeout(syncLabelFont, 80);
        }
        function labelFor(node, emphasize=false) {
          if (emphasize) return node.shortLabel || node.fullLabel || ' ';
          if (labelMode === 'all') return node.fullLabel || node.shortLabel || ' ';
          if (labelMode === 'off') return ' ';
          return node.coreLabel || ' ';
        }
        function baseNodeUpdate(node) {
          return { id:node.id, hidden:groupHidden(node), opacity:1,
                   label:labelFor(node),
                   font:readableFont(node.baseFontColor || '#D9DCE5'), color:{background:node.baseColor,
                   border:node.color && node.color.border ? node.color.border : '#2B2F39'} };
        }
        function restoreView(fit=false) {
          nodes.update(nodes.get().map(baseNodeUpdate));
          const nodeMap = new Map(nodes.get().map(n => [n.id, n]));
          edges.update(edges.get().map(e => ({ id:e.id,
            hidden:groupHidden(nodeMap.get(e.from)) || groupHidden(nodeMap.get(e.to)),
            color:{color:e.baseColor, highlight:'rgba(197,181,255,.95)', hover:'rgba(197,181,255,.78)', inherit:false}
          })));
          network.unselectAll();
          if (fit) network.fit({animation:{duration:450,easingFunction:'easeInOutQuad'}});
          if (viewDimension === '3d') render3D();
        }
        function highlight(ids, selectedId=null) {
          const active = new Set(ids);
          nodes.update(nodes.get().map(n => ({id:n.id, hidden:groupHidden(n),
            label:labelFor(n, active.has(n.id)),
            opacity:active.has(n.id) ? 1 : .10,
            font:readableFont(active.has(n.id) ? '#F1F2F6' : 'rgba(217,220,229,.12)')})));
          const nodeMap = new Map(nodes.get().map(n => [n.id, n]));
          edges.update(edges.get().map(e => {
            const direct = selectedId ? (e.from === selectedId || e.to === selectedId) :
                           (active.has(e.from) && active.has(e.to));
            return {id:e.id, hidden:groupHidden(nodeMap.get(e.from)) || groupHidden(nodeMap.get(e.to)),
                    color:{color:direct ? 'rgba(197,181,255,.78)' : 'rgba(80,85,98,.045)',
                           highlight:'rgba(214,204,255,1)', hover:'rgba(197,181,255,.9)', inherit:false}};
          }));
        }
        function showDetails(html) { detailsContent.innerHTML = html || ''; details.classList.add('open'); }
        function closeDetails() { details.classList.remove('open'); }
        function focusNode(id) {
          const related = [id].concat(network.getConnectedNodes(id));
          highlight(related, id);
          network.selectNodes([id]);
          network.focus(id, {scale:1.15, animation:{duration:420,easingFunction:'easeInOutQuad'}});
          const node = nodes.get(id);
          showDetails(node.detailHtml);
        }
        function multiplyMatrixVector(matrix, vector) {
          const e = matrix.elements;
          return [
            e[0]*vector[0] + e[4]*vector[1] + e[8]*vector[2] + e[12]*vector[3],
            e[1]*vector[0] + e[5]*vector[1] + e[9]*vector[2] + e[13]*vector[3],
            e[2]*vector[0] + e[6]*vector[1] + e[10]*vector[2] + e[14]*vector[3],
            e[3]*vector[0] + e[7]*vector[1] + e[11]*vector[2] + e[15]*vector[3],
          ];
        }
        function update3DLabels() {
          graph3dLabels.classList.toggle('all-labels', labelMode === 'all');
          if (viewDimension !== '3d' || !graph3d || labelMode === 'off') {
            graph3dLabelElements.forEach(element => { element.style.display = 'none'; });
            return;
          }
          const camera = graph3d.camera();
          camera.updateMatrixWorld(true);
          const bounds = graph3dContainer.getBoundingClientRect();
          const term = searchInput.value.trim().toLocaleLowerCase();
          const visibleLabels = new Set();
          graph3dData.nodes.forEach(node => {
            const showCore = Boolean(node.label);
            const showSearch = Boolean(term && node.matched);
            const shouldShow = !node.hidden && (labelMode === 'all' || node.matched !== false)
              && (labelMode === 'all' || showCore || showSearch)
              && Number.isFinite(node.x) && Number.isFinite(node.y) && Number.isFinite(node.z);
            if (!shouldShow) return;
            let element = graph3dLabelElements.get(node.id);
            if (!element) {
              element = document.createElement('span');
              element.className = 'kg-3d-label';
              element.textContent = node.fullLabel;
              graph3dLabels.appendChild(element);
              graph3dLabelElements.set(node.id, element);
            }
            element.style.color = node.topSearchMuted ? '#858b97' : '#e8eaf0';
            const view = multiplyMatrixVector(camera.matrixWorldInverse, [node.x,node.y,node.z,1]);
            const clip = multiplyMatrixVector(camera.projectionMatrix, view);
            if (clip[3] <= 0) { element.style.display='none'; return; }
            const ndcX = clip[0] / clip[3];
            const ndcY = clip[1] / clip[3];
            const ndcZ = clip[2] / clip[3];
            if (Math.abs(ndcX) > 1.08 || Math.abs(ndcY) > 1.08 || ndcZ < -1 || ndcZ > 1) {
              element.style.display='none'; return;
            }
            element.style.display = 'block';
            element.style.left = ((ndcX + 1) * .5 * bounds.width) + 'px';
            element.style.top = ((1 - ndcY) * .5 * bounds.height) + 'px';
            visibleLabels.add(node.id);
          });
          graph3dLabelElements.forEach((element, id) => {
            if (!visibleLabels.has(id)) element.style.display = 'none';
          });
        }
        function animate3DLabels() {
          update3DLabels();
          requestAnimationFrame(animate3DLabels);
        }
        function degreeAwareRadial3DForce() {
          let simulationNodes = [];
          let maximumDegree = 1;
          function force(alpha) {
            simulationNodes.forEach((node, index) => {
              const degree = Math.max(0, Number(node.degree || 0));
              const centrality = degree > 0
                ? Math.log1p(degree) / Math.log1p(maximumDegree)
                : 0;
              // Hubs occupy the central volume, ordinary connected nodes form
              // the middle layers, and true isolates stay in a compact outer layer.
              const targetRadius = degree === 0 ? 215 : 32 + (1 - centrality) * 145;
              let x = node.x || 0, y = node.y || 0, z = node.z || 0;
              let radius = Math.hypot(x, y, z);
              if (radius < 1) {
                const angle = index * Math.PI * (3 - Math.sqrt(5));
                const vertical = ((index % 7) - 3) / 3;
                x = Math.cos(angle); y = vertical; z = Math.sin(angle);
                radius = Math.hypot(x, y, z);
              }
              const strength = degree === 0 ? .18 : .10 + .08 * centrality;
              const displacement = (radius - targetRadius) * strength * alpha;
              node.vx = (node.vx || 0) - (x / radius) * displacement;
              node.vy = (node.vy || 0) - (y / radius) * displacement;
              node.vz = (node.vz || 0) - (z / radius) * displacement;

              if (radius <= 300) return;
              const boundaryPull = ((radius - 300) / Math.max(radius, 1)) * .26 * alpha;
              node.vx -= x * boundaryPull;
              node.vy -= y * boundaryPull;
              node.vz -= z * boundaryPull;
            });
          }
          force.initialize = nodes3d => {
            simulationNodes = nodes3d || [];
            maximumDegree = Math.max(
              1,
              ...simulationNodes.map(node => Math.max(0, Number(node.degree || 0))),
            );
          };
          return force;
        }
        function render3D() {
          if (!window.ForceGraph3D) {
            graph3dContainer.innerHTML = '<div style="height:100%;display:grid;place-items:center;color:#c8cbd4;font:14px Segoe UI,sans-serif">3D rendering could not be initialized.</div>';
            return;
          }
          const term = searchInput.value.trim().toLocaleLowerCase();
          graph3dData.nodes.forEach(node => {
            node.hidden = hiddenGroups.has(node.nodeType);
            node.matched = !term || (node.searchText || '').includes(term);
          });
          const nodeById = new Map(graph3dData.nodes.map(node => [node.id, node]));
          graph3dData.links.forEach(link => {
            const sourceId = typeof link.source === 'object' ? link.source.id : link.source;
            const targetId = typeof link.target === 'object' ? link.target.id : link.target;
            link.hidden = !nodeById.get(sourceId) || !nodeById.get(targetId)
              || nodeById.get(sourceId).hidden || nodeById.get(targetId).hidden;
          });
          if (!graph3d) {
            graph3d = new ForceGraph3D(graph3dContainer, {controlType:'orbit'})
              .backgroundColor('#111318')
              .showNavInfo(false)
              .graphData(graph3dData)
              .nodeId('id')
              .nodeLabel(node => '<b>' + node.fullLabel + '</b><br><span style="color:#aeb4c2">' + node.nodeType + '</span>')
              .nodeVal(node => node.size)
              .nodeColor(node => node.matched ? node.color : 'rgba(77,83,96,.18)')
              .nodeOpacity(.96)
              .nodeResolution(14)
              .linkColor(link => link.color)
              .linkOpacity(.48)
              .linkWidth(0.6)
              .linkDirectionalArrowLength(2.4)
              .linkDirectionalArrowRelPos(.94)
              .linkDirectionalArrowColor(link => link.color)
              .linkDirectionalParticles(1)
              .linkDirectionalParticleWidth(.7)
              .linkDirectionalParticleSpeed(.004)
              .linkDirectionalParticleColor(link => link.color)
              .d3VelocityDecay(.24)
              .warmupTicks(30)
              .cooldownTime(18000)
              .onNodeClick(node => {
                showDetails(node.detailHtml);
                const distance = 115;
                const length = Math.hypot(node.x || 0, node.y || 0, node.z || 0) || 1;
                const ratio = 1 + distance / length;
                graph3d.cameraPosition(
                  {x:(node.x || 0) * ratio, y:(node.y || 0) * ratio, z:(node.z || 0) * ratio},
                  node,
                  700,
                );
              })
              .onNodeDragEnd(node => {
                node.fx = undefined; node.fy = undefined; node.fz = undefined;
                graph3d.d3ReheatSimulation();
              });
            graph3d.d3Force('charge').strength(node => Number(node.degree || 0) === 0 ? -38 : -140);
            graph3d.d3Force('link').distance(92).strength(.72);
            graph3d.d3Force('degree-radial', degreeAwareRadial3DForce());
            setTimeout(() => graph3d.zoomToFit(650, 78), 450);
          }
          graph3d
            .nodeVisibility(node => !node.hidden)
            .linkVisibility(link => !link.hidden)
            .nodeColor(node => node.matched ? node.color : 'rgba(77,83,96,.18)')
            .refresh();
          if (term) {
            const matches = graph3dData.nodes.filter(node => !node.hidden && node.matched);
            matchCount.textContent = matches.length ? matches.length + ' matches' : 'No matches';
          }
        }
        function switchDimension() {
          viewDimension = viewDimension === '2d' ? '3d' : '2d';
          const is3d = viewDimension === '3d';
          document.body.classList.toggle('kg-3d-active', is3d);
          document.getElementById('mynetwork').style.display = is3d ? 'none' : 'block';
          graph3dContainer.style.display = is3d ? 'block' : 'none';
          document.getElementById('kg-dimension').textContent = 'View: ' + (is3d ? '3D' : '2D');
          document.getElementById('kg-dimension').classList.toggle('active', is3d);
          if (is3d) { render3D(); graph3d && graph3d.resumeAnimation(); }
          else if (graph3d) { graph3d.pauseAnimation(); }
        }
        function searchGraph() {
          const term = searchInput.value.trim().toLocaleLowerCase();
          if (viewDimension === '3d') {
            matchCount.textContent = ''; render3D(); return;
          }
          if (!term) { matchCount.textContent=''; restoreView(false); return; }
          const matches = nodes.get().filter(n => (n.searchText || n.fullLabel || '').toLocaleLowerCase().includes(term));
          matchCount.textContent = matches.length ? matches.length + ' matches' : 'No matches';
          highlight(matches.map(n => n.id));
          if (matches.length) network.fit({nodes:matches.map(n => n.id), animation:{duration:350}});
        }
        function zoomBy(factor) {
          const next = Math.max(.08, Math.min(4, network.getScale() * factor));
          network.moveTo({scale:next, animation:{duration:180,easingFunction:'easeInOutQuad'}});
        }

        network.on('click', params => {
          if (params.nodes.length) { focusNode(params.nodes[0]); return; }
          if (params.edges.length) { const edge=edges.get(params.edges[0]); showDetails(edge.detailHtml); return; }
          closeDetails(); restoreView(false);
        });
        network.on('doubleClick', params => {
          if (params.nodes.length) network.focus(params.nodes[0], {scale:1.55, animation:{duration:500}});
        });
        network.on('zoom', scheduleFontSync);
        let loadingHidden = false;
        function hideLoading() {
          if (loadingHidden) return;
          loadingHidden = true;
          const loading=document.getElementById('kg-loading');
          if (loading) { loading.style.opacity='0'; setTimeout(() => loading.remove(), 350); }
          network.fit({animation:{duration:500}});
          setTimeout(syncLabelFont, 560);
        }
        network.on('stabilizationIterationsDone', hideLoading);
        network.on('stabilized', hideLoading);
        // The inline network can finish stabilizing before the custom listener is registered.
        // Always reveal the canvas even when that early event was missed.
        setTimeout(hideLoading, 1800);
        searchInput.addEventListener('input', searchGraph);
        searchInput.addEventListener('keydown', event => {
          if (event.key === 'Enter') { const term=searchInput.value.trim().toLocaleLowerCase();
            const first=nodes.get().find(n => (n.searchText || '').toLocaleLowerCase().includes(term));
            if (first) focusNode(first.id); }
          if (event.key === 'Escape') { searchInput.value=''; matchCount.textContent=''; closeDetails(); restoreView(true); }
        });
        document.getElementById('kg-dimension').addEventListener('click', switchDimension);
        document.getElementById('kg-fit').addEventListener('click', () => {
          if (viewDimension === '3d') { render3D(); graph3d && graph3d.zoomToFit(500, 78); }
          else { network.fit({animation:{duration:450}}); }
        });
        document.getElementById('kg-3d-reheat').addEventListener('click', () => {
          if (graph3d) { graph3d.d3ReheatSimulation(); }
        });
        document.getElementById('kg-zoom-out').addEventListener('click', () => zoomBy(.82));
        document.getElementById('kg-zoom-in').addEventListener('click', () => zoomBy(1.22));
        document.getElementById('kg-labels').addEventListener('click', event => {
          labelMode = labelMode === 'core' ? 'all' : (labelMode === 'all' ? 'off' : 'core');
          const names = {core:'Core', all:'All', off:'Hidden'};
          event.currentTarget.textContent = 'Labels: ' + names[labelMode];
          event.currentTarget.classList.toggle('active', labelMode !== 'off');
          restoreView(false);
        });
        document.getElementById('kg-reset').addEventListener('click', () => {
          searchInput.value=''; matchCount.textContent=''; hiddenGroups.clear(); closeDetails(); labelMode='core';
          const labelsButton=document.getElementById('kg-labels');
          labelsButton.textContent='Labels: Core'; labelsButton.classList.add('active');
          document.querySelectorAll('.kg-legend-item').forEach(b => b.classList.remove('off')); restoreView(true);
        });
        document.getElementById('kg-physics').addEventListener('click', event => {
          physicsOn=!physicsOn; network.setOptions({physics:{enabled:physicsOn}});
          event.currentTarget.textContent='Physics: ' + (physicsOn ? 'On' : 'Off');
          event.currentTarget.classList.toggle('active', physicsOn);
        });
        document.getElementById('kg-details-close').addEventListener('click', closeDetails);
        document.querySelectorAll('.kg-legend-item').forEach(button => button.addEventListener('click', () => {
          const group=button.dataset.group;
          if (hiddenGroups.has(group)) hiddenGroups.delete(group); else hiddenGroups.add(group);
          button.classList.toggle('off', hiddenGroups.has(group)); restoreView(false);
        }));
        animate3DLabels();
      })();
    </script>
    """.replace("__LEGEND__", legend_buttons).replace("__THREE_DATA__", three_data_json)
    document = document.replace("</body>", custom_ui + "</body>")
    iframe = (
        '<iframe class="kg-network-frame" sandbox="allow-scripts" '
        'style="width:100%;height:780px;border:0;border-radius:14px;background:#111318" '
        f'srcdoc="{html_lib.escape(document, quote=True)}"></iframe>'
    )
    status = (
        f"Showing {len(nodes)} nodes and {len(edges)} relations, including {len(matched_node_rows)} directly matched nodes. "
        "Matched nodes have a white border and are listed separately above the graph. Drag nodes to rearrange the graph; "
        "click a node to focus on one-hop neighbors, double-click to zoom in, or click empty space to reset. "
        "The graph supports a 2D/3D switch, search, Core/All/Hidden label modes, entity-type filters, "
        "physics controls, button or wheel zooming, and panning. In 3D, high-degree hubs gravitate toward the "
        "center while low-degree nodes occupy outer layers; drag to orbit and scroll to zoom."
    )
    return iframe, matched_node_rows, edge_table, status
