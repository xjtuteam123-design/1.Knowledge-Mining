"""Account-free HTTPS tunnel for the public RAG launcher.

localhost.run is reached with Windows OpenSSH. The command uses a self-contained
SSH configuration so unrelated per-user SSH host settings cannot change it.
"""

from __future__ import annotations

import atexit
import os
import re
import shutil
import subprocess
import threading
from pathlib import Path


PUBLIC_URL_PATTERN = re.compile(r"https://[a-zA-Z0-9-]+\.lhr\.life")
ANSI_PATTERN = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")


class LocalhostRunTunnel:
    def __init__(self, local_port: int) -> None:
        self.local_port = int(local_port)
        self.process: subprocess.Popen[str] | None = None
        self._stop_event = threading.Event()
        self._thread = threading.Thread(
            target=self._supervise,
            name="localhost-run-public-tunnel",
            daemon=True,
        )
        self._last_url = ""

    @staticmethod
    def executable() -> str:
        configured = os.getenv("RAG_SSH_EXE", "").strip()
        candidate = configured or shutil.which("ssh")
        if not candidate or not Path(candidate).exists():
            raise RuntimeError(
                "Windows OpenSSH was not found. Install 'OpenSSH Client' from "
                "Windows Optional Features, or set RAG_SSH_EXE."
            )
        return candidate

    def command(self) -> list[str]:
        return [
            self.executable(),
            "-F",
            "NUL" if os.name == "nt" else "/dev/null",
            "-p",
            "22",
            "-T",
            "-o",
            "StrictHostKeyChecking=accept-new",
            "-o",
            "BatchMode=yes",
            "-o",
            "ServerAliveInterval=30",
            "-o",
            "ServerAliveCountMax=3",
            "-o",
            "ExitOnForwardFailure=yes",
            "-R",
            f"80:127.0.0.1:{self.local_port}",
            "nokey@localhost.run",
            "--",
            "--output",
            "json",
        ]

    def start(self) -> None:
        self.executable()
        self._thread.start()
        atexit.register(self.stop)

    def _supervise(self) -> None:
        retry_seconds = 5
        while not self._stop_event.is_set():
            print(
                "[PUBLIC TUNNEL] Connecting to localhost.run over TCP 22...",
                flush=True,
            )
            creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
            try:
                self.process = subprocess.Popen(
                    self.command(),
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    bufsize=1,
                    creationflags=creation_flags,
                )
                assert self.process.stdout is not None
                for raw_line in self.process.stdout:
                    line = ANSI_PATTERN.sub("", raw_line).strip()
                    match = PUBLIC_URL_PATTERN.search(line)
                    if match:
                        url = match.group(0)
                        if url != self._last_url:
                            self._last_url = url
                            print(f"[PUBLIC URL] {url}", flush=True)
                    elif line and "if you get a permission denied error" not in line.lower() and (
                        "error" in line.lower()
                        or "failed" in line.lower()
                        or "denied" in line.lower()
                    ):
                        print(f"[PUBLIC TUNNEL] {line}", flush=True)
                return_code = self.process.wait()
            except Exception as exc:
                return_code = -1
                print(f"[PUBLIC TUNNEL] {type(exc).__name__}: {exc}", flush=True)
            finally:
                self.process = None

            if self._stop_event.is_set():
                return
            print(
                f"[PUBLIC TUNNEL] Disconnected (code {return_code}); "
                f"retrying in {retry_seconds} seconds...",
                flush=True,
            )
            self._stop_event.wait(retry_seconds)
            retry_seconds = min(30, retry_seconds * 2)

    def stop(self) -> None:
        self._stop_event.set()
        process = self.process
        if process is not None and process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()


def start_public_tunnel(local_port: int) -> LocalhostRunTunnel:
    tunnel = LocalhostRunTunnel(local_port)
    tunnel.start()
    return tunnel
