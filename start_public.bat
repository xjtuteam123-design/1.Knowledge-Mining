@echo off
setlocal
cd /d "%~dp0"

set "PYTHON_EXE="

python -c "import gradio, openai, pypdf, networkx, plotly, pyvis" >nul 2>&1
if not errorlevel 1 set "PYTHON_EXE=python"

if not defined PYTHON_EXE if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" -c "import gradio, openai, pypdf, networkx, plotly, pyvis" >nul 2>&1
    if not errorlevel 1 set "PYTHON_EXE=.venv\Scripts\python.exe"
)

if not defined PYTHON_EXE if exist "..\rag-project-main\.venv\Scripts\python.exe" (
    "..\rag-project-main\.venv\Scripts\python.exe" -c "import gradio, openai, pypdf, networkx, plotly, pyvis" >nul 2>&1
    if not errorlevel 1 set "PYTHON_EXE=..\rag-project-main\.venv\Scripts\python.exe"
)

if not defined PYTHON_EXE (
    echo No Python environment with all required packages was found.
    echo Run: python -m pip install -r requirements.txt
    pause
    exit /b 1
)

"%PYTHON_EXE%" -c "import sys; print('Using Python:', sys.executable)"
"%PYTHON_EXE%" scripts\start_public.py
endlocal
