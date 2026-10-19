import unittest

import app


class LoadingMessageTest(unittest.TestCase):
    def test_none_metadata_is_safe(self):
        self.assertFalse(
            app.is_loading_message(
                {"role": "assistant", "content": "A completed answer", "metadata": None}
            )
        )

    def test_html_marker_survives_missing_metadata(self):
        self.assertTrue(
            app.is_loading_message(
                {"role": "assistant", "content": app.LOADING_DOTS_HTML, "metadata": None}
            )
        )

    def test_metadata_marker_is_recognized(self):
        self.assertTrue(
            app.is_loading_message(
                {
                    "role": "assistant",
                    "content": "normalized content",
                    "metadata": {"id": app.LOADING_MESSAGE_ID},
                }
            )
        )


if __name__ == "__main__":
    unittest.main()
