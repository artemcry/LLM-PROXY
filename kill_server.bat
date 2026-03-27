@echo off
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8080 ^| findstr LISTENING') do taskkill /PID %%a /F 2>nul
wmic process where "commandline like '%%server_bg.py%%'" call terminate 2>nul
echo LLMProxy stopped.
