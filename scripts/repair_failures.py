"""Repair failed PDFs with Unicode cleanup, Poppler extraction, or Windows OCR."""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rag_store import DB_PATH, ingest_path  # noqa: E402


PDFTOPPM = Path(r"D:\latex\texlive\2026\bin\windows\pdftoppm.exe")
PDFTOTEXT = Path(r"D:\latex\texlive\2026\bin\windows\pdftotext.exe")
OCR_SCRIPT = ROOT / "scripts" / "windows_ocr.ps1"


def emit(payload: dict) -> None:
    print(json.dumps(payload, ensure_ascii=False), flush=True)


def page_count(path: Path) -> int:
    return len(PdfReader(str(path)).pages)


def poppler_pages(path: Path) -> list[tuple[int, str]]:
    pages = []
    for page in range(1, page_count(path) + 1):
        process = subprocess.run(
            [str(PDFTOTEXT), "-f", str(page), "-l", str(page), "-enc", "UTF-8", str(path), "-"],
            capture_output=True,
            check=True,
        )
        pages.append((page, process.stdout.decode("utf-8", errors="replace")))
    return pages


def ocr_pages(path: Path, dpi: int) -> list[tuple[int, str]]:
    count = page_count(path)
    language = "zh-Hans" if re.search(r"[\u3400-\u9fff]", path.name) else "en-US"
    pages = []
    temp_parent = ROOT / "data" / "ocr-temp"
    temp_parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="paper-", dir=temp_parent) as temporary:
        image = Path(temporary) / "page.png"
        prefix = image.with_suffix("")
        for page in range(1, count + 1):
            subprocess.run(
                [
                    str(PDFTOPPM), "-f", str(page), "-l", str(page), "-singlefile",
                    "-png", "-r", str(dpi), str(path), str(prefix),
                ],
                capture_output=True,
                check=True,
            )
            process = subprocess.run(
                [
                    "powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
                    str(OCR_SCRIPT), "-ImagePath", str(image), "-LanguageTag", language,
                ],
                capture_output=True,
                check=True,
            )
            text = process.stdout.decode("utf-8", errors="replace").strip()
            pages.append((page, text))
            emit({"event": "ocr_page", "name": path.name, "page": page, "pages": count, "characters": len(text)})
            image.unlink(missing_ok=True)
    return pages


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
        sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--dpi", type=int, default=200)
    args = parser.parse_args()
    with sqlite3.connect(DB_PATH) as connection:
        rows = connection.execute("SELECT source_path,error FROM failures ORDER BY source_path").fetchall()
    if args.limit:
        rows = rows[: args.limit]
    emit({"event": "start", "failures": len(rows), "dpi": args.dpi})
    repaired = failed = 0
    for number, (source_path, error) in enumerate(rows, 1):
        source = Path(source_path)
        try:
            if "No extractable text" in error:
                pages = ocr_pages(source, args.dpi)
                method = "windows_ocr"
                result = ingest_path(source, pages_override=pages)
            elif "cryptography" in error:
                pages = poppler_pages(source)
                method = "poppler"
                result = ingest_path(source, pages_override=pages)
            else:
                method = "unicode_cleanup"
                result = ingest_path(source)
            ok = result.get("status") in {"indexed", "duplicate", "already_indexed"}
            repaired += int(ok)
            failed += int(not ok)
            emit({"event": "document", "number": number, "total": len(rows), "name": source.name, "method": method, **result})
        except Exception as exc:
            failed += 1
            emit({"event": "document", "number": number, "total": len(rows), "name": source.name, "status": "failed", "error": str(exc)})
    emit({"event": "complete", "repaired": repaired, "failed": failed})
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
