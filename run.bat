@echo off
title Stormy
echo Starting Stormy...

cd /d "%\~dp0"

if exist venv (
    echo Using existing venv...
    call venv\Scripts\activate.bat
) else (
    echo Creating new virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install --upgrade pip
    pip install -r requirements.txt
)

python -m stormy.api.routes

echo.
echo Press any key to close...
pause >nul
