@echo off
setlocal
cd /d "%~dp0"

echo Continue the new GraphRAG corpus until 500 papers are complete.
echo Only original Markdown is sent for extraction; legacy structured chunks are not used.
echo This command calls the configured DeepSeek API and incurs API charges.
python scripts\extract_graphrag.py --target-total 500 --selection all --workers 2

echo.
echo GraphRAG extraction finished or stopped. Review reports\graph_run_status.json.
pause
endlocal
