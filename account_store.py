"""Small, local account store for the public Gradio entry point.

Public visitors use separate registration and sign-in actions. Passwords are
salted and hashed; plaintext passwords and browser session tokens are never
written to disk.
"""

from __future__ import annotations

import hashlib
import hmac
import os
import re
import secrets
import sqlite3
import threading
import time
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AUTH_DB_PATH = Path(
    os.getenv("RAG_AUTH_DB", str(ROOT / "data" / "auth" / "accounts.db"))
).resolve()
PASSWORD_ITERATIONS = 310_000
USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_.-]{3,32}$")
_DB_LOCK = threading.RLock()


def _now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def _connect() -> sqlite3.Connection:
    AUTH_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(AUTH_DB_PATH, timeout=30)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA journal_mode=WAL")
    connection.execute("PRAGMA foreign_keys=ON")
    return connection


@contextmanager
def _database():
    """Commit or roll back a transaction and always release the file handle."""
    connection = _connect()
    try:
        with connection:
            yield connection
    finally:
        connection.close()


def initialize_account_store() -> None:
    with _DB_LOCK, _database() as connection:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY COLLATE NOCASE,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                iterations INTEGER NOT NULL,
                created_at TEXT NOT NULL,
                registration_ip TEXT,
                last_seen_at TEXT,
                last_seen_ip TEXT,
                access_count INTEGER NOT NULL DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS registration_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                ip_address TEXT NOT NULL,
                user_agent TEXT,
                registered_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS online_sessions (
                session_hash TEXT PRIMARY KEY,
                username TEXT NOT NULL COLLATE NOCASE,
                ip_address TEXT NOT NULL,
                last_seen_epoch REAL NOT NULL
            );

            CREATE INDEX IF NOT EXISTS idx_online_sessions_last_seen
            ON online_sessions(last_seen_epoch);

            CREATE TABLE IF NOT EXISTS web_sessions (
                token_hash TEXT PRIMARY KEY,
                username TEXT NOT NULL COLLATE NOCASE,
                created_at TEXT NOT NULL,
                expires_epoch REAL NOT NULL,
                last_seen_epoch REAL NOT NULL
            );

            CREATE INDEX IF NOT EXISTS idx_web_sessions_expires
            ON web_sessions(expires_epoch);
            """
        )


def _password_digest(password: str, salt: bytes, iterations: int) -> bytes:
    return hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, iterations
    )


def _account_limit() -> int:
    try:
        return max(0, int(os.getenv("RAG_MAX_PUBLIC_ACCOUNTS", "200")))
    except ValueError:
        return 200


def _credentials_are_valid(username: str, password: str) -> bool:
    return bool(
        USERNAME_PATTERN.fullmatch((username or "").strip())
        and 8 <= len(password or "") <= 256
    )


def register_account(username: str, password: str) -> tuple[bool, str]:
    """Create a new account and return a user-facing result message."""
    username = (username or "").strip()
    if not USERNAME_PATTERN.fullmatch(username):
        return False, "Username must be 3–32 letters, numbers, dots, underscores, or hyphens."
    if not 8 <= len(password or "") <= 256:
        return False, "Password must contain at least 8 characters."

    initialize_account_store()
    with _DB_LOCK, _database() as connection:
        connection.execute("BEGIN IMMEDIATE")
        row = connection.execute(
            "SELECT 1 FROM users WHERE username = ?",
            (username,),
        ).fetchone()
        if row is not None:
            return False, "This username already exists. Please sign in instead."

        limit = _account_limit()
        if limit and connection.execute("SELECT COUNT(*) FROM users").fetchone()[0] >= limit:
            return False, "Public registration has reached its account limit."

        salt = secrets.token_bytes(16)
        digest = _password_digest(password, salt, PASSWORD_ITERATIONS)
        connection.execute(
            """
            INSERT INTO users
                (username, password_hash, salt, iterations, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (username, digest.hex(), salt.hex(), PASSWORD_ITERATIONS, _now()),
        )
        return True, "Account created successfully."


def authenticate_account(username: str, password: str) -> bool:
    """Validate the password for an existing account."""
    username = (username or "").strip()
    if not _credentials_are_valid(username, password):
        return False
    initialize_account_store()
    with _DB_LOCK, _database() as connection:
        row = connection.execute(
            "SELECT password_hash, salt, iterations FROM users WHERE username = ?",
            (username,),
        ).fetchone()
    if row is None:
        return False
    actual = _password_digest(
        password, bytes.fromhex(row["salt"]), int(row["iterations"])
    )
    return hmac.compare_digest(actual.hex(), row["password_hash"])


def authenticate_or_register(username: str, password: str) -> bool:
    """Backward-compatible combined authentication used by legacy launchers."""
    username = (username or "").strip()
    if not _credentials_are_valid(username, password):
        return False
    initialize_account_store()
    with _DB_LOCK, _database() as connection:
        exists = connection.execute(
            "SELECT 1 FROM users WHERE username = ?", (username,)
        ).fetchone() is not None
    if exists:
        return authenticate_account(username, password)
    created, _ = register_account(username, password)
    return created


def _session_token_hash(token: str) -> str:
    return hashlib.sha256((token or "").encode("utf-8")).hexdigest()


def create_web_session(username: str, lifetime_seconds: int = 7 * 24 * 60 * 60) -> str:
    """Create a revocable browser session and return its un-hashed token."""
    initialize_account_store()
    token = secrets.token_urlsafe(32)
    now_epoch = time.time()
    expires_epoch = now_epoch + max(300, int(lifetime_seconds))
    with _DB_LOCK, _database() as connection:
        connection.execute("DELETE FROM web_sessions WHERE expires_epoch <= ?", (now_epoch,))
        row = connection.execute(
            "SELECT username FROM users WHERE username = ?", ((username or "").strip(),)
        ).fetchone()
        if row is None:
            raise ValueError("Cannot create a session for an unknown account.")
        connection.execute(
            """
            INSERT INTO web_sessions
                (token_hash, username, created_at, expires_epoch, last_seen_epoch)
            VALUES (?, ?, ?, ?, ?)
            """,
            (_session_token_hash(token), row["username"], _now(), expires_epoch, now_epoch),
        )
    return token


def web_session_username(token: str | None) -> str | None:
    """Return the authenticated username for a live browser session token."""
    if not token:
        return None
    initialize_account_store()
    now_epoch = time.time()
    token_hash = _session_token_hash(token)
    with _DB_LOCK, _database() as connection:
        row = connection.execute(
            """
            SELECT username FROM web_sessions
            WHERE token_hash = ? AND expires_epoch > ?
            """,
            (token_hash, now_epoch),
        ).fetchone()
        if row is None:
            return None
        return str(row["username"])


def delete_web_session(token: str | None) -> None:
    """Revoke one browser session token."""
    if not token:
        return
    initialize_account_store()
    with _DB_LOCK, _database() as connection:
        connection.execute(
            "DELETE FROM web_sessions WHERE token_hash = ?",
            (_session_token_hash(token),),
        )


def record_authenticated_access(
    username: str | None,
    ip_address: str | None,
    user_agent: str | None = None,
    session_hash: str | None = None,
) -> bool:
    """Record an authenticated visit and print a new registration with its IP.

    Returns True only when this visit supplies the account's registration IP for
    the first time.
    """
    username = (username or "").strip()
    ip_address = (ip_address or "unknown").strip() or "unknown"
    if not username:
        return False

    initialize_account_store()
    timestamp = _now()
    newly_recorded = False
    canonical_username = username
    with _DB_LOCK, _database() as connection:
        connection.execute("BEGIN IMMEDIATE")
        row = connection.execute(
            "SELECT username, registration_ip FROM users WHERE username = ?", (username,)
        ).fetchone()
        if row is None:
            return False
        canonical_username = row["username"]
        if not row["registration_ip"]:
            newly_recorded = True
            connection.execute(
                """
                UPDATE users
                SET registration_ip = ?, last_seen_at = ?, last_seen_ip = ?,
                    access_count = access_count + 1
                WHERE username = ?
                """,
                (ip_address, timestamp, ip_address, canonical_username),
            )
            connection.execute(
                """
                INSERT INTO registration_events
                    (username, ip_address, user_agent, registered_at)
                VALUES (?, ?, ?, ?)
                """,
                (canonical_username, ip_address, (user_agent or "")[:1000], timestamp),
            )
        else:
            connection.execute(
                """
                UPDATE users
                SET last_seen_at = ?, last_seen_ip = ?, access_count = access_count + 1
                WHERE username = ?
                """,
                (timestamp, ip_address, canonical_username),
            )
        if session_hash:
            connection.execute(
                """
                INSERT INTO online_sessions
                    (session_hash, username, ip_address, last_seen_epoch)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(session_hash) DO UPDATE SET
                    username = excluded.username,
                    ip_address = excluded.ip_address,
                    last_seen_epoch = excluded.last_seen_epoch
                """,
                (session_hash[:256], canonical_username, ip_address, time.time()),
            )

    if newly_recorded:
        print(
            f"[ACCOUNT REGISTERED] user={canonical_username} "
            f"ip={ip_address} time={timestamp}",
            flush=True,
        )
    return newly_recorded


def record_online_presence(
    username: str | None, ip_address: str | None, session_hash: str | None
) -> None:
    """Refresh one browser session without counting it as another page visit."""
    username = (username or "").strip()
    session_hash = (session_hash or "").strip()
    ip_address = (ip_address or "unknown").strip() or "unknown"
    if not username or not session_hash:
        return

    initialize_account_store()
    with _DB_LOCK, _database() as connection:
        row = connection.execute(
            "SELECT username FROM users WHERE username = ?", (username,)
        ).fetchone()
        if row is None:
            return
        connection.execute(
            """
            INSERT INTO online_sessions
                (session_hash, username, ip_address, last_seen_epoch)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(session_hash) DO UPDATE SET
                username = excluded.username,
                ip_address = excluded.ip_address,
                last_seen_epoch = excluded.last_seen_epoch
            """,
            (session_hash[:256], row["username"], ip_address, time.time()),
        )


def public_account_stats(online_window_seconds: int = 75) -> dict[str, int]:
    """Return registered and recently active unique-account counts."""
    initialize_account_store()
    cutoff = time.time() - max(10, int(online_window_seconds))
    with _DB_LOCK, _database() as connection:
        connection.execute(
            "DELETE FROM online_sessions WHERE last_seen_epoch < ?", (cutoff,)
        )
        registered = int(connection.execute("SELECT COUNT(*) FROM users").fetchone()[0])
        online = int(
            connection.execute(
                "SELECT COUNT(DISTINCT username) FROM online_sessions"
            ).fetchone()[0]
        )
    return {"online": online, "registered": registered}


def clear_online_sessions() -> None:
    """Discard presence rows left behind by a previous server process."""
    initialize_account_store()
    with _DB_LOCK, _database() as connection:
        connection.execute("DELETE FROM online_sessions")


def list_registered_accounts() -> list[dict[str, object]]:
    initialize_account_store()
    with _DB_LOCK, _database() as connection:
        rows = connection.execute(
            """
            SELECT username, registration_ip, created_at, last_seen_at,
                   last_seen_ip, access_count
            FROM users
            ORDER BY created_at DESC
            """
        ).fetchall()
    return [dict(row) for row in rows]
