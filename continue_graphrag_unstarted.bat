@echo off
setlocal
cd /d "%~dp0"

echo Continue only documents that have not been attempted yet.
echo Completed and failed documents are skipped. The failed set remains available for a later repair run.
echo Source text is split into 30000-character segments to prevent truncated 16000-token JSON output.
echo Network outages pause safely and are retried every 5 minutes.
python scripts\run_graphrag_resilient.py

echo.
echo Unstarted-document batch finished or stopped.
pause
endlocal
