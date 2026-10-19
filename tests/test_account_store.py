from __future__ import annotations

import os
import sqlite3
import tempfile
import unittest
from contextlib import closing
from pathlib import Path
from unittest.mock import patch

import account_store


class AccountStoreTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.database = Path(self.temporary_directory.name) / "accounts.db"
        self.path_patch = patch.object(account_store, "AUTH_DB_PATH", self.database)
        self.limit_patch = patch.dict(os.environ, {"RAG_MAX_PUBLIC_ACCOUNTS": "200"})
        self.path_patch.start()
        self.limit_patch.start()

    def tearDown(self):
        self.limit_patch.stop()
        self.path_patch.stop()
        self.temporary_directory.cleanup()

    def test_first_login_registers_and_later_login_authenticates(self):
        self.assertTrue(
            account_store.authenticate_or_register("alloy_user", "safe-pass-123")
        )
        self.assertTrue(
            account_store.authenticate_or_register("alloy_user", "safe-pass-123")
        )
        self.assertFalse(
            account_store.authenticate_or_register("alloy_user", "wrong-pass")
        )

        with closing(sqlite3.connect(self.database)) as connection:
            password_hash, salt = connection.execute(
                "SELECT password_hash, salt FROM users WHERE username = ?",
                ("alloy_user",),
            ).fetchone()
        self.assertNotEqual(password_hash, "safe-pass-123")
        self.assertTrue(salt)

    def test_registration_ip_is_recorded_only_once(self):
        self.assertTrue(
            account_store.authenticate_or_register("researcher", "safe-pass-123")
        )
        self.assertTrue(
            account_store.record_authenticated_access(
                "researcher", "203.0.113.10", "test browser"
            )
        )
        self.assertFalse(
            account_store.record_authenticated_access(
                "researcher", "203.0.113.11", "test browser"
            )
        )

        account = account_store.list_registered_accounts()[0]
        self.assertEqual(account["registration_ip"], "203.0.113.10")
        self.assertEqual(account["last_seen_ip"], "203.0.113.11")
        self.assertEqual(account["access_count"], 2)

    def test_separate_registration_login_and_session(self):
        created, message = account_store.register_account(
            "graph_user", "safe-pass-123"
        )
        self.assertTrue(created, message)
        duplicate, _ = account_store.register_account(
            "graph_user", "different-pass-123"
        )
        self.assertFalse(duplicate)
        self.assertTrue(
            account_store.authenticate_account("graph_user", "safe-pass-123")
        )
        self.assertFalse(
            account_store.authenticate_account("graph_user", "wrong-pass-123")
        )

        token = account_store.create_web_session("graph_user")
        self.assertEqual(account_store.web_session_username(token), "graph_user")
        self.assertIsNone(account_store.web_session_username("not-a-real-token"))
        account_store.delete_web_session(token)
        self.assertIsNone(account_store.web_session_username(token))

    def test_username_password_rules_and_account_limit(self):
        with patch.dict(os.environ, {"RAG_MAX_PUBLIC_ACCOUNTS": "1"}):
            self.assertFalse(account_store.authenticate_or_register("x", "safe-pass-123"))
            self.assertFalse(account_store.authenticate_or_register("valid_user", "short"))
            self.assertTrue(
                account_store.authenticate_or_register("first_user", "safe-pass-123")
            )
            self.assertFalse(
                account_store.authenticate_or_register("second_user", "safe-pass-123")
            )
            self.assertTrue(
                account_store.authenticate_or_register("FIRST_USER", "safe-pass-123")
            )

    def test_online_count_uses_unique_accounts_and_expires(self):
        self.assertTrue(
            account_store.authenticate_or_register("first_user", "safe-pass-123")
        )
        self.assertTrue(
            account_store.authenticate_or_register("second_user", "safe-pass-123")
        )
        with patch.object(account_store.time, "time", return_value=1_000):
            account_store.record_authenticated_access(
                "first_user", "203.0.113.1", session_hash="tab-one"
            )
            account_store.record_online_presence(
                "first_user", "203.0.113.1", "tab-two"
            )
            account_store.record_authenticated_access(
                "second_user", "203.0.113.2", session_hash="tab-three"
            )
            self.assertEqual(
                account_store.public_account_stats(),
                {"online": 2, "registered": 2},
            )

        with patch.object(account_store.time, "time", return_value=1_100):
            self.assertEqual(
                account_store.public_account_stats(),
                {"online": 0, "registered": 2},
            )

        account_store.clear_online_sessions()
        self.assertEqual(
            account_store.public_account_stats(),
            {"online": 0, "registered": 2},
        )


if __name__ == "__main__":
    unittest.main()
