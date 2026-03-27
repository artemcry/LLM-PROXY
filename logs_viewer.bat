@echo off
title LLMProxy Logs
cd /d d:\Projects\LLMProxy\logs
for %%F in (*.log) do set "latest=%%F"
if not defined latest (
    echo No log files found in d:\Projects\LLMProxy\logs
    pause
    exit
)
echo Viewing: %latest%
echo ===========================
type %latest%
echo.
echo ===========================
echo Press Ctrl+C to exit, or any key to refresh...
pause >nul
call "%~f0"
