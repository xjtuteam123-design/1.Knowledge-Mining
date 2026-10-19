import tempfile
import unittest
from contextlib import closing
from pathlib import Path

import rag_store


class RagStoreTokenizationTest(unittest.TestCase):
    def test_chinese_query_does_not_expand_to_single_characters(self):
        self.assertEqual(rag_store._search_tokens("你好").split(), ["你好"])
        self.assertEqual(
            rag_store._search_tokens("铌合金").split(),
            ["铌合金", "铌合", "合金"],
        )

    def test_relevance_rewards_query_coverage(self):
        terms = rag_store._query_relevance_terms("Nb alloy yield strength")
        complete = rag_store._lexical_relevance(
            "The Nb alloy had a yield strength of 620 MPa.",
            terms,
            "Nb alloy yield strength",
        )
        partial = rag_store._lexical_relevance(
            "The Nb alloy was annealed.",
            terms,
            "Nb alloy yield strength",
        )
        unrelated = rag_store._lexical_relevance(
            "The specimen was polished before microscopy.",
            terms,
            "Nb alloy yield strength",
        )
        self.assertGreater(complete, partial)
        self.assertGreater(partial, unrelated)
        self.assertEqual(unrelated, 0.0)

    def test_element_symbols_are_kept_as_relevance_terms(self):
        self.assertEqual(rag_store._query_relevance_terms("W and C"), ["w", "c"])


class RetrievalHistoryTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        root = Path(self.temporary.name)
        self.original_paths = {
            name: getattr(rag_store, name)
            for name in (
                "DATA_DIR", "MARKDOWN_DIR", "STRUCTURED_DIR", "UPLOAD_DIR",
                "INDEX_DIR", "REPORTS_DIR", "DB_PATH",
            )
        }
        rag_store.DATA_DIR = root / "data"
        rag_store.MARKDOWN_DIR = root / "data" / "markdown"
        rag_store.STRUCTURED_DIR = root / "data" / "structured"
        rag_store.UPLOAD_DIR = root / "data" / "uploads"
        rag_store.INDEX_DIR = root / "data" / "index"
        rag_store.REPORTS_DIR = root / "reports"
        rag_store.DB_PATH = rag_store.INDEX_DIR / "literature.db"

    def tearDown(self):
        for name, value in self.original_paths.items():
            setattr(rag_store, name, value)
        self.temporary.cleanup()

    def _seed_document(self):
        with closing(rag_store._connect()) as connection, connection:
            connection.execute(
                """
                INSERT INTO documents(
                    id, name, source_path, file_sha256, text_sha256,
                    markdown_path, pages, chunk_count, structured, created_at
                ) VALUES ('doc-1', 'paper.pdf', 'paper.pdf', 'file-1', 'text-1',
                          'paper.md', 1, 2, 0, 'now')
                """
            )
            rag_store._insert_chunk(
                connection, "doc-1", "paper.pdf", 1, "original_text",
                "Nb alloy yield strength reached 620 MPa after annealing.",
            )
            rag_store._insert_chunk(
                connection, "doc-1", "paper.pdf", 1, "original_text",
                "Nb alloy yield strength reached 710 MPa after forging.",
            )

    def test_indexed_recall_has_no_fixed_top_k_and_history_is_recorded(self):
        self._seed_document()
        results = rag_store.search_global("Nb alloy yield strength", ["doc-1"])
        self.assertEqual(len(results), 2)
        rag_store.record_retrieval_feedback(
            "Nb alloy yield strength", "Standard Q&A", results, {"doc-1"}
        )
        priors = rag_store.historical_chunk_priors(
            "yield strength of Nb alloy", ["doc-1"]
        )
        self.assertEqual(set(priors), {result["chunk_id"] for result in results})
        stats = rag_store.chunk_history_stats(set(priors))
        self.assertTrue(all(item["question_count"] == 1 for item in stats.values()))
        self.assertTrue(all(item["citation_rate"] == 1.0 for item in stats.values()))


if __name__ == "__main__":
    unittest.main()
