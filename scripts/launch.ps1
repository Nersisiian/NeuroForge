#!/usr/bin/env pwsh

Write-Host "🧠 Зажигаем NeuroForge..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd "\neuroforge-small-brain"; python -m venv venv; .\venv\Scripts\activate; pip install -e .; uvicorn src.main:app --reload" -WindowStyle Normal
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd "\neuroforge-fluid-canvas"; npm install; npm run dev" -WindowStyle Normal
Start-Sleep -Seconds 3
Start-Process "http://localhost:5173"
Write-Host "💥 NeuroForge запущен. Скажи ему, что ты хочешь создать." -ForegroundColor Green
