"""Start the RAG UI with self-registration through an SSH HTTPS tunnel."""

from __future__ import annotations

import os
import socket
import sys
import threading
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def find_available_port(preferred_port: int, attempts: int = 20) -> int:
    """Return the preferred localhost port or the next available one."""
    preferred_port = int(preferred_port)
    for port in range(preferred_port, preferred_port + max(1, attempts)):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
            try:
                probe.bind(("127.0.0.1", port))
            except OSError:
                continue
            return port
    raise RuntimeError(
        f"No available localhost port was found from {preferred_port} "
        f"through {preferred_port + max(1, attempts) - 1}."
    )


def monitor_public_status(initial_status: tuple[int, int]) -> None:
    from account_store import public_account_stats

    previous = initial_status
    while True:
        time.sleep(10)
        stats = public_account_stats()
        current = (stats["online"], stats["registered"])
        if current != previous:
            print(
                f"[PUBLIC STATUS] online={current[0]} registered={current[1]}",
                flush=True,
            )
            previous = current


def main() -> None:
    os.environ["RAG_PUBLIC_MODE"] = "True"
    os.environ["RAG_PUBLIC_READONLY"] = "True"
    # Use the account-free SSH tunnel instead of Gradio's FRP share service.
    # This path is independent of any optional local HTTP proxy configuration.
    os.environ["GRADIO_SHARE"] = "False"
    os.chdir(ROOT)
    sys.path.insert(0, str(ROOT))

    from localhost_run_tunnel import start_public_tunnel

    requested_port = int(os.getenv("GRADIO_SERVER_PORT", "7860"))
    server_port = find_available_port(requested_port)
    if server_port != requested_port:
        print(
            f"[PORT] {requested_port} is already in use; using {server_port} instead.",
            flush=True,
        )
    os.environ["GRADIO_SERVER_PORT"] = str(server_port)
    # Keep a reference for the lifetime of the app; the tunnel also registers
    # its own shutdown handler so the SSH child process is cleaned up on exit.
    public_tunnel = start_public_tunnel(server_port)
    print(f"[LOCAL URL] http://127.0.0.1:{server_port}", flush=True)

    from account_store import (
        AUTH_DB_PATH,
        clear_online_sessions,
        list_registered_accounts,
        public_account_stats,
    )

    clear_online_sessions()
    accounts = list_registered_accounts()
    print("Public self-registration is enabled.")
    print(f"Account database: {AUTH_DB_PATH}")
    print(f"Existing registered accounts: {len(accounts)}")
    for account in accounts:
        print(
            f"  {account['username']} | registration IP: "
            f"{account['registration_ip'] or 'pending first page load'}"
        )
    print("New registrations and their IP addresses will appear below.")
    status = public_account_stats()
    initial_status = (status["online"], status["registered"])
    print(
        f"[PUBLIC STATUS] online={initial_status[0]} "
        f"registered={initial_status[1]}",
        flush=True,
    )
    threading.Thread(
        target=monitor_public_status,
        args=(initial_status,),
        name="public-status-monitor",
        daemon=True,
    ).start()
    try:
        import app as rag_application
        from public_auth_app import run_public_server

        run_public_server(rag_application.demo, server_port)
    finally:
        public_tunnel.stop()


if __name__ == "__main__":
    main()
