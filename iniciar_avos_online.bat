@echo off
title Avos Online - Super App Assistivo
echo ========================================================
echo   Iniciando Plataforma Avos Online
echo   Super Aplicativo Assistivo de Gerontecnologia
echo ========================================================
echo.
cd /d "C:\Users\user\avos_online"
echo Abrindo o navegador em http://127.0.0.1:8080 ...
start http://127.0.0.1:8080
echo Iniciando servidor Uvicorn...
python -m uvicorn app:app --host 0.0.0.0 --port 8080 --reload
pause
