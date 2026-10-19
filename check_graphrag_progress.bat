@echo off
setlocal
cd /d "%~dp0"

python scripts\graph_batch_progress.py --watch --interval 5

endlocal
