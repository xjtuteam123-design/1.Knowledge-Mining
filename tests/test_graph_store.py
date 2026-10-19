import json
import tempfile
import unittest
import sqlite3
from contextlib import closing
from pathlib import Path

import graph_store


class GraphStoreTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        root = Path(self.temporary.name)
        graph_store.GRAPH_DIR = root
        graph_store.GRAPH_RAW_DIR = root / "raw"
        graph_store.GRAPH_PAPERS_DIR = root / "papers"
        graph_store.GRAPH_FAILED_DIR = root / "failed"
        graph_store.GRAPH_DB_PATH = root / "graph.db"
        graph_store.GRAPH_REPORTS_DIR = root / "reports"
        graph_store.LITERATURE_DB_PATH = root / "literature.db"

    def tearDown(self):
        self.temporary.cleanup()

    def test_user_defined_graph_limits_are_not_fixed_to_150_nodes_or_2_hops(self):
        self.assertEqual(graph_store._graph_request_limits(240, 4, 386), (240, 4))
        self.assertEqual(graph_store._graph_request_limits(9999, 9999, 386), (386, 385))
        self.assertEqual(graph_store._graph_request_limits(5, 0, 386), (10, 1))

    def test_import_search_and_visualize(self):
        document = {"id": "doc-1", "name": "example.pdf"}
        evidence = [{"page": 3, "quote": "Zr and C formed fine ZrC precipitates."}]
        payload = {
            "chunk_id": "doc-1:part:001",
            "paper_metadata": {"title": "Example refractory alloy"},
            "alloy_systems": [
                {"id": "alloy_system_1", "name": "Nb-W alloy", "evidence": evidence}
            ],
            "samples": [
                {
                    "id": "sample_1",
                    "original_name": "Nb-10W-1Zr-0.1C",
                    "canonical_name": "Nb-10W-1Zr-0.1C",
                    "alloy_system_id": "alloy_system_1",
                    "material_state": "annealed",
                    "composition": [
                        {"element": "Zr", "value": 1, "unit": "wt.%", "evidence": evidence},
                        {"element": "C", "value": 0.1, "unit": "wt.%", "evidence": evidence},
                    ],
                    "evidence": evidence,
                }
            ],
            "process_steps": [
                {
                    "id": "process_1",
                    "sample_id": "sample_1",
                    "sequence": 1,
                    "method": "arc melting",
                    "parameters": {},
                    "input_state": None,
                    "output_state": "as-cast",
                    "evidence": evidence,
                },
                {
                    "id": "process_2",
                    "sample_id": "sample_1",
                    "sequence": 2,
                    "method": "annealing",
                    "parameters": {"temperature_c": 1200, "time": "1 h"},
                    "input_state": "as-cast",
                    "output_state": "annealed",
                    "evidence": evidence,
                }
            ],
            "phases_and_microstructures": [
                {
                    "id": "phase_1",
                    "type": "Phase",
                    "name": "ZrC",
                    "sample_id": "sample_1",
                    "material_state": "annealed",
                    "attributes": {"size": "20 nm"},
                    "evidence": evidence,
                },
                {
                    "id": "defect_1",
                    "type": "Defect",
                    "name": "pore",
                    "sample_id": "sample_1",
                    "material_state": "annealed",
                    "attributes": {"size": "2 μm"},
                    "evidence": evidence,
                },
            ],
            "property_observations": [
                {
                    "id": "observation_1",
                    "sample_id": "sample_1",
                    "material_state": "annealed",
                    "property": "yield strength",
                    "value": 500,
                    "unit": "MPa",
                    "conditions": {"temperature_c": 1000},
                    "evidence": evidence,
                },
                {
                    "id": "observation_without_value",
                    "sample_id": "sample_1",
                    "material_state": "annealed",
                    "property": "ductility",
                    "value": None,
                    "unit": None,
                    "conditions": {},
                    "evidence": evidence,
                },
            ],
            "mechanisms": [
                {
                    "id": "mechanism_1",
                    "name": "precipitation strengthening",
                    "sample_id": "sample_1",
                    "assertion_level": "author_interpretation",
                    "evidence": evidence,
                }
            ],
            "machine_learning_models": [
                {
                    "id": "ml_model_1",
                    "name": "random forest",
                    "sample_id": "sample_1",
                    "property_observation_id": "observation_1",
                    "task": "yield-strength prediction",
                    "metrics": {"r2": 0.92},
                    "evidence": evidence,
                }
            ],
            "relations": [
                {
                    "id": "claim_1",
                    "source_id": "phase_1",
                    "predicate": "ACTIVATES_MECHANISM",
                    "target_id": "mechanism_1",
                    "sample_id": "sample_1",
                    "assertion_level": "author_interpretation",
                    "evidence": evidence,
                },
                {
                    "id": "claim_filtered_property",
                    "source_id": "sample_1",
                    "predicate": "HAS_PROPERTY_OBSERVATION",
                    "target_id": "observation_without_value",
                    "sample_id": "sample_1",
                    "assertion_level": "directly_reported",
                    "evidence": evidence,
                },
            ],
            "unresolved_terms": [],
            "conflicts": [],
        }
        counts = graph_store.replace_paper_graph(
            document, payload, "data/graph/paper_graphs/doc-1.json", 1
        )
        self.assertGreaterEqual(counts["nodes"], 9)
        self.assertGreaterEqual(counts["edges"], 10)
        self.assertEqual(graph_store.graph_stats()["papers"], 1)
        with closing(sqlite3.connect(graph_store.GRAPH_DB_PATH)) as graph_connection:
            predicates = {
                row[0] for row in graph_connection.execute("SELECT predicate FROM edges")
            }
        self.assertIn("FABRICATED_BY", predicates)
        self.assertIn("FOLLOWED_BY", predicates)
        self.assertIn("PRODUCES", predicates)
        self.assertNotIn("RESULTS_IN_STATE", predicates)
        self.assertNotIn("HAS_MATERIAL_STATE", predicates)
        self.assertNotIn("TESTED_UNDER", predicates)
        self.assertIn("OBSERVED_AFTER_PROCESS", predicates)
        self.assertIn("HAS_COMPOSITION", predicates)
        self.assertNotIn("HAS_SAMPLE", predicates)
        self.assertIn("ASSOCIATED_WITH_MECHANISM", predicates)
        self.assertIn("USES_MODEL", predicates)
        self.assertIn("PREDICTS", predicates)
        with closing(sqlite3.connect(graph_store.GRAPH_DB_PATH)) as graph_connection:
            node_types = {
                row[0] for row in graph_connection.execute("SELECT DISTINCT type FROM nodes")
            }
        self.assertIn("Alloy", node_types)
        self.assertIn("Composition", node_types)
        self.assertIn("Sample", node_types)
        self.assertIn("PostTreatment", node_types)
        self.assertNotIn("MaterialState", node_types)
        self.assertNotIn("TestCondition", node_types)
        self.assertIn("Defect", node_types)
        self.assertIn("Mechanism", node_types)
        self.assertIn("MachineLearningModel", node_types)
        self.assertIn("Property", node_types)
        self.assertNotIn("PropertyType", node_types)
        self.assertNotIn("UnresolvedEntity", node_types)
        with closing(sqlite3.connect(graph_store.GRAPH_DB_PATH)) as graph_connection:
            self.assertEqual(
                graph_connection.execute("SELECT COUNT(*) FROM nodes WHERE type='Property'").fetchone()[0],
                1,
            )
            property_link = graph_connection.execute(
                """
                SELECT source.type, target.attributes_json
                FROM edges edge
                JOIN nodes source ON source.node_key=edge.source_key
                JOIN nodes target ON target.node_key=edge.target_key
                WHERE edge.predicate='HAS_PROPERTY_OBSERVATION'
                """
            ).fetchone()
            self.assertIn(property_link[0], {"Sample", "FabricationProcess", "PostTreatment"})
            self.assertEqual(json.loads(property_link[1])["conditions"]["temperature_c"], 1000)
        with closing(sqlite3.connect(graph_store.LITERATURE_DB_PATH)) as literature, literature:
            literature.execute(
                "CREATE TABLE chunks (id INTEGER PRIMARY KEY, document_id TEXT, kind TEXT, text TEXT)"
            )
            literature.executemany(
                "INSERT INTO chunks(document_id, kind, text) VALUES (?, ?, ?)",
                [
                    ("doc-1", "original_text", "铌锆合金高温力学性能与组织演变。" * 12),
                    ("doc-1", "structured_analysis", "English structured knowledge."),
                ],
            )
        corpus_stats = graph_store.parsed_corpus_stats()
        self.assertEqual(corpus_stats["chinese_papers"], 1)
        self.assertEqual(corpus_stats["english_papers"], 0)
        self.assertEqual(corpus_stats["patents"], 0)
        # Legacy structured-analysis chunks remain archived but are excluded
        # from the active GraphRAG corpus and its UI statistics.
        self.assertEqual(corpus_stats["chunks"], 1)
        self.assertEqual(corpus_stats["alloys"], 1)
        self.assertGreater(corpus_stats["relations"], 0)
        result = graph_store.search_subgraph("ZrC precipitation strengthening", 40, 2)
        self.assertTrue(result["nodes"])
        self.assertTrue(result["edges"])
        overview_types = {
            node["type"] for node in graph_store.search_subgraph("", 60, 1)["nodes"]
        }
        for entity_type in ("Alloy", "Composition", "Element", "Phase"):
            self.assertIn(entity_type, overview_types)
        self.assertNotIn("MaterialState", overview_types)
        overview = graph_store.search_subgraph("", 60, 1)
        overview_nodes = {node["node_key"]: node for node in overview["nodes"]}
        degree = {key: 0 for key in overview_nodes}
        route_outgoing = {}
        for edge in overview["edges"]:
            degree[edge["source_key"]] += 1
            degree[edge["target_key"]] += 1
            if edge["predicate"] in {
                "HAS_COMPOSITION", "FABRICATED_BY", "FOLLOWED_BY", "PRODUCES", "HAS_SAMPLE"
            }:
                route_outgoing.setdefault(edge["source_key"], []).append(edge["target_key"])
        self.assertTrue(all(value > 0 for value in degree.values()))
        for key, node in overview_nodes.items():
            if node["type"] not in {"FabricationProcess", "PostTreatment"}:
                continue
            pending, visited, found_sample = [key], {key}, False
            while pending:
                current = pending.pop()
                for target in route_outgoing.get(current, []):
                    if overview_nodes[target]["type"] == "Sample":
                        found_sample = True
                    elif target not in visited:
                        visited.add(target)
                        pending.append(target)
            self.assertTrue(found_sample, node["name"])
        evidence_rows = graph_store.graph_evidence("ZrC", 5)
        self.assertTrue(any("ZrC" in row["text"] for row in evidence_rows))
        figure, rows, status = graph_store.make_graph_figure("ZrC", 40, 2)
        self.assertTrue(figure.data)
        self.assertTrue(rows)
        self.assertIn("nodes", status)
        graph_html, matched_rows, html_rows, html_status = graph_store.make_graph_html("ZrC", 40, 2)
        self.assertTrue(graph_html.startswith("<iframe"))
        self.assertIn("vis-network", graph_html)
        self.assertIn("dragNodes", graph_html)
        self.assertIn("kg-search", graph_html)
        self.assertIn("kg-labels", graph_html)
        self.assertIn("kg-dimension", graph_html)
        self.assertIn("ForceGraph3D", graph_html)
        self.assertIn("d3ReheatSimulation", graph_html)
        self.assertIn("kg-3d-reheat", graph_html)
        self.assertIn("kg-3d-labels", graph_html)
        self.assertIn("update3DLabels", graph_html)
        self.assertIn("degreeAwareRadial3DForce", graph_html)
        self.assertIn("degree-radial", graph_html)
        self.assertIn("Math.log1p(degree)", graph_html)
        self.assertIn("return node.fullLabel || node.shortLabel", graph_html)
        self.assertIn("all-labels", graph_html)
        self.assertIn("kg-zoom-in", graph_html)
        self.assertIn("coreLabel", graph_html)
        self.assertIn("topSearchMuted", graph_html)
        self.assertIn("#555B66", graph_html)
        self.assertIn('&quot;navigationButtons&quot;: false', graph_html)
        self.assertNotIn('&quot;title&quot;: &quot;&lt;div class=', graph_html)
        self.assertNotIn('&quot;shape&quot;: &quot;diamond&quot;', graph_html)
        self.assertTrue(matched_rows)
        self.assertTrue(any("ZrC" in str(row[0]) for row in matched_rows))
        self.assertEqual(len(html_rows), len(rows))
        self.assertIn("Drag nodes", html_status)
        self.assertEqual(graph_store._display_node_name("yield strength"), "Yield strength")
        self.assertEqual(graph_store._display_node_name("creep stress exponent n: 105"), "Creep stress exponent n: 105")
        self.assertEqual(
            graph_store._display_node_name("NbMoTaNiCr formed layer", "Composition"),
            "NbMoTaNiCr",
        )
        self.assertEqual(graph_store._display_node_name("NB", "Element"), "Nb")
        self.assertEqual(graph_store._display_predicate("ACTIVATES_MECHANISM"), "Activates mechanism")

    def test_sample_aliases_are_not_displayed_on_the_graph(self):
        self.assertEqual(
            graph_store._display_node_name(
                "8#", "Composition", {}, "tial-5nb-7mo", "TiAl-Nb-Mo alloy"
            ),
            "TiAl-5Nb-7Mo",
        )
        self.assertEqual(
            graph_store._display_node_name(
                "Sample 1#", "Composition", {}, "1#", "W-based alloy"
            ),
            "W-based alloy",
        )
        self.assertEqual(
            graph_store._display_node_name(
                "1200 °C annealed sample",
                "Composition",
                {},
                "nb-10w-1zr",
                "Nb-W-Zr alloy",
            ),
            "Nb-10W-1Zr",
        )
        self.assertEqual(
            graph_store._display_node_name(
                "Nb1Zr锭",
                "Composition",
                {},
                "nb1zr",
                "Nb-Zr alloy",
                "as-cast",
            ),
            "Nb1Zr",
        )
        self.assertEqual(
            graph_store._display_node_name(
                "原工艺成品",
                "Composition",
                {},
                "原工艺成品",
                "Nb-Zr alloy",
                "finished product (original process)",
            ),
            "Nb-Zr alloy",
        )

    def test_sample_system_context_is_resolved_from_material_path(self):
        nodes = {
            "composition": {
                "name": "TiAl-5Nb-5Mo",
                "canonical_name": "tial-5nb-5mo",
                "type": "Composition",
                "attributes": {},
            },
            "sample": {
                "name": "TiAl-5Nb-5Mo sample",
                "canonical_name": "tial-5nb-5mo",
                "type": "Sample",
                "attributes": {},
            },
            "system": {
                "name": "TiAl-Nb-Mo alloy",
                "canonical_name": "tial-nb-mo alloy",
                "type": "Alloy",
                "attributes": {},
            },
        }
        edges = [
            {"source_key": "system", "predicate": "HAS_COMPOSITION", "target_key": "composition"},
            {"source_key": "composition", "predicate": "HAS_SAMPLE", "target_key": "sample"},
        ]
        display_names, systems = graph_store._graph_display_names(nodes, edges)
        self.assertEqual(display_names["sample"], "TiAl-5Nb-5Mo sample")
        self.assertEqual(systems["sample"], "TiAl-Nb-Mo alloy")
        self.assertEqual(
            graph_store._display_node_name(
                "Mo sample",
                "Sample",
                {
                    "display_state": "deformed (¦Å=20%)",
                    "display_variant_count": 2,
                    "display_variant_index": 2,
                },
                "Mo",
            ),
            "Mo · specimen 2 · deformed (ε=20%)",
        )

    def test_core_labels_cover_scientific_entity_types(self):
        nodes = {
            "alloy": {"name": "Nb-W alloy", "type": "Alloy"},
            "composition": {"name": "Nb-10W", "type": "Composition"},
            "sample": {"name": "Nb-10W sample", "type": "Sample"},
            "element": {"name": "W", "type": "Element"},
            "phase": {"name": "ZrC", "type": "Phase"},
            "process": {"name": "arc melting", "type": "FabricationProcess"},
            "treatment": {"name": "annealing", "type": "PostTreatment"},
            "mechanism": {"name": "precipitation strengthening", "type": "Mechanism"},
            "property": {"name": "yield strength: 500 MPa", "type": "Property"},
        }
        selected = graph_store._select_core_labels(
            nodes,
            {key: 1 for key in nodes},
            set(),
        )
        self.assertEqual(selected, {"alloy", "composition", "element", "phase"})

    def test_identical_processes_merge_and_conditions_are_displayed(self):
        attributes = {
            "sequence": 2,
            "parameters": {"temperature_c": 600, "time": "1 h", "pressure": None},
            "input_state": "as-forged",
            "output_state": "annealed",
        }
        first = graph_store._process_key("PostTreatment", "annealing", attributes)
        second = graph_store._process_key("PostTreatment", "Annealing", dict(attributes))
        changed = graph_store._process_key(
            "PostTreatment",
            "annealing",
            {**attributes, "parameters": {"temperature_c": 700, "time": "1 h"}},
        )
        self.assertEqual(first, second)
        self.assertNotEqual(first, changed)
        self.assertEqual(
            graph_store._display_node_name("annealing", "PostTreatment", attributes),
            "Annealing · 600 °C · 1 h",
        )

    def test_property_filter_keeps_only_material_or_model_performance(self):
        self.assertEqual(
            graph_store._property_kind(
                {"id": "p1", "property": "yield strength", "value": 500}, set()
            ),
            "material",
        )
        self.assertEqual(
            graph_store._property_kind(
                {"id": "p2", "property": "relative density", "value": 98.5}, set()
            ),
            "material",
        )
        self.assertIsNone(
            graph_store._property_kind(
                {"id": "p3", "property": "grain size", "value": 12}, set()
            )
        )
        self.assertIsNone(
            graph_store._property_kind(
                {"id": "p4", "property": "tensile strain rate", "value": "1e-3"}, set()
            )
        )
        self.assertEqual(
            graph_store._property_kind(
                {"id": "metric_1", "property": "R2", "value": 0.95}, {"metric_1"}
            ),
            "model",
        )
        self.assertIsNone(
            graph_store._property_kind(
                {"id": "orphan_metric", "property": "R2", "value": 0.95}, set()
            )
        )

    def test_same_composition_merges_across_papers_without_author_aliases(self):
        def payload(alias):
            return {
                "chunk_id": "paper",
                "paper_metadata": {"title": f"Study of {alias}"},
                "alloy_systems": [
                    {"id": "system_1", "name": "Nb-Zr alloy", "evidence": []}
                ],
                "samples": [
                    {
                        "id": "sample_1",
                        "original_name": alias,
                        "canonical_name": "Nb-1Zr",
                        "alloy_system_id": "system_1",
                        "material_state": "annealed",
                        "composition": [
                            {"element": "Nb", "unit": "wt.%", "role": "balance"},
                            {"element": "Zr", "value": 1, "unit": "wt.%", "role": "nominal"},
                        ],
                        "evidence": [],
                    }
                ],
                "process_steps": [],
                "phases_and_microstructures": [],
                "property_observations": [],
                "mechanisms": [],
                "relations": [],
                "unresolved_terms": [],
                "conflicts": [],
            }

        graph_store.replace_paper_graph(
            {"id": "doc-1", "name": "one.pdf"}, payload("7#"), "one.json", 1
        )
        graph_store.replace_paper_graph(
            {"id": "doc-2", "name": "two.pdf"}, payload("Sample B"), "two.json", 1
        )
        with closing(sqlite3.connect(graph_store.GRAPH_DB_PATH)) as connection:
            compositions = connection.execute(
                "SELECT node_key, name FROM nodes WHERE type='Composition'"
            ).fetchall()
            sources = connection.execute(
                "SELECT COUNT(*) FROM node_sources WHERE node_key=?",
                (compositions[0][0],),
            ).fetchone()[0]
        self.assertEqual(compositions, [(compositions[0][0], "Nb-1Zr")])
        self.assertEqual(sources, 2)
        self.assertEqual(
            graph_store._display_node_name("7#", "Composition", {}, "Nb-1Zr", "Nb-Zr alloy"),
            "Nb-1Zr",
        )

    def test_pure_single_element_uses_element_instead_of_composition(self):
        payload = {
            "chunk_id": "paper",
            "paper_metadata": {"title": "Pure molybdenum study"},
            "alloy_systems": [{"id": "system_1", "name": "pure molybdenum"}],
            "samples": [
                {
                    "id": "sample_1",
                    "original_name": "pure Mo",
                    "canonical_name": "pure Mo",
                    "alloy_system_id": "system_1",
                    "composition": [
                        {"element": "Mo", "value": 99.99, "unit": "wt.%", "role": "pure"}
                    ],
                }
            ],
            "process_steps": [],
            "phases_and_microstructures": [],
            "property_observations": [],
            "mechanisms": [],
            "machine_learning_models": [],
            "relations": [],
            "unresolved_terms": [],
            "conflicts": [],
        }
        graph_store.replace_paper_graph(
            {"id": "doc-pure", "name": "pure-mo.pdf"}, payload, "pure-mo.json", 1
        )
        with closing(sqlite3.connect(graph_store.GRAPH_DB_PATH)) as connection:
            types = {
                row[0]: row[1]
                for row in connection.execute("SELECT type, COUNT(*) FROM nodes GROUP BY type")
            }
            paths = connection.execute(
                "SELECT predicate FROM edges WHERE predicate IN ('CONTAINS_ELEMENT','HAS_SAMPLE')"
            ).fetchall()
        self.assertNotIn("Composition", types)
        self.assertNotIn("Alloy", types)
        self.assertEqual(types.get("Element"), 1)
        self.assertEqual(types.get("Sample"), 1)
        self.assertIn(("HAS_SAMPLE",), paths)

    def test_compound_additives_are_decomposed_into_chemical_elements(self):
        self.assertEqual(graph_store._component_element_symbols("B4C"), ["B", "C"])
        self.assertEqual(graph_store._component_element_symbols("La2O3"), ["La", "O"])
        self.assertEqual(graph_store._component_element_symbols("ZrO₂"), ["Zr", "O"])
        self.assertEqual(graph_store._component_element_symbols("Nb"), ["Nb"])
        self.assertEqual(graph_store._component_element_symbols("unknown additive"), [])

    def test_structured_paper_metadata_is_parsed_for_citations(self):
        metadata = graph_store._parse_structured_paper_metadata(
            """# Paper Metadata
- **Title:** Example refractory alloy
- **Authors**: A. Researcher, B. Scientist
- **Journal:** Journal of Refractory Materials
- **Year:** 2024 (available online 2023)
- **DOI:** https://doi.org/10.1000/example.123
- **Material Category:** Nb alloy

# Alloy System and Research Object
Other content.
"""
        )
        self.assertEqual(metadata["title"], "Example refractory alloy")
        self.assertEqual(metadata["authors"], ["A. Researcher", "B. Scientist"])
        self.assertEqual(metadata["journal"], "Journal of Refractory Materials")
        self.assertEqual(metadata["year"], "2024")
        self.assertEqual(metadata["doi"], "10.1000/example.123")


if __name__ == "__main__":
    unittest.main()
