@echo off
setlocal
cd /d "%~dp0"

echo Continue the next 2000-document GraphRAG batch.
echo Completed documents are skipped by document ID; pending and failed items are retried.
echo The first 9 items are patents. This command calls the configured DeepSeek API.
python scripts\extract_graphrag.py --include-file reports\graph_next_2000_ids.txt --selection all --workers 2

echo.
echo Batch finished or stopped. Review reports\graph_run_status.json.
pause
endlocal
