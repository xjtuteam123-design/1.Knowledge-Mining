"""Print public accounts and the IP addresses recorded at registration."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from account_store import AUTH_DB_PATH, list_registered_accounts  # noqa: E402


def main() -> None:
    accounts = list_registered_accounts()
    print(f"Account database: {AUTH_DB_PATH}")
    if not accounts:
        print("No public accounts have registered yet.")
        return

    print(f"Registered accounts: {len(accounts)}")
    for account in accounts:
        print(
            "  {username} | registration IP: {registration_ip} | "
            "created: {created_at} | last IP: {last_seen_ip} | visits: {access_count}".format(
                **account
            )
        )


if __name__ == "__main__":
    main()

