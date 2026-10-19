from __future__ import annotations

import os
import socket
import sys
import threading
import time
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def find_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def monitor_public_status(initial_status: tuple[int, int], stop_event: threading.Event) -> None:
    from account_store import public_account_stats

    previous = initial_status
    while not stop_event.wait(10):
        stats = public_account_stats()
        current = (stats["online"], stats["registered"])
        if current != previous:
            print(
                f"[PUBLIC STATUS] online={current[0]} registered={current[1]}",
                flush=True,
            )
            previous = current


def main() -> None:
    port = find_free_port()
    os.environ["RAG_PUBLIC_MODE"] = "True"
    os.environ["RAG_PUBLIC_READONLY"] = "True"
    # The tunnel is created below around the complete FastAPI application so
    # that the custom registration/login page is included as well.
    os.environ["GRADIO_SHARE"] = "False"
    os.environ["GRADIO_SERVER_PORT"] = str(port)
    os.chdir(ROOT)
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))

    import app as rag_application
    import uvicorn
    from gradio import networking
    from public_auth_app import create_public_application
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
    status_stop_event = threading.Event()
    threading.Thread(
        target=monitor_public_status,
        args=(initial_status, status_stop_event),
        name="public-status-monitor",
        daemon=True,
    ).start()

    rag_application.demo.queue(default_concurrency_limit=4)
    web_app = create_public_application(rag_application.demo)
    config = uvicorn.Config(
        web_app,
        host="127.0.0.1",
        port=port,
        log_level="warning",
        access_log=False,
        proxy_headers=True,
        forwarded_allow_ips="127.0.0.1",
    )
    server = uvicorn.Server(config)
    server_thread = threading.Thread(target=server.run, daemon=True)
    server_thread.start()

    health_url = f"http://127.0.0.1:{port}/health"
    for _ in range(100):
        try:
            with urllib.request.urlopen(health_url, timeout=1) as response:
                if response.status == 200:
                    break
        except Exception:
            time.sleep(0.1)
    else:
        server.should_exit = True
        raise RuntimeError("The local public application did not start in time.")

    print(f"Local port: {port}", flush=True)
    print(f"Local registration page: http://127.0.0.1:{port}", flush=True)
    print("Starting Gradio tunnel for the complete registration application...", flush=True)
    try:
        public_url = networking.setup_tunnel(
            local_host="127.0.0.1",
            local_port=port,
            share_token=rag_application.demo.share_token,
            share_server_address=None,
            share_server_tls_certificate=None,
        )
        print(f"* Running on public URL: {public_url}", flush=True)
        print("Press Ctrl+C to stop the public application.", flush=True)
        while server_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        status_stop_event.set()
        server.should_exit = True
        server_thread.join(timeout=5)


if __name__ == "__main__":
    main()
