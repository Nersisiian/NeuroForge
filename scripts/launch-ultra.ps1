#!/usr/bin/env pwsh
Write-Host "🧠 NeuroForge ULTRA запускается через Docker..." -ForegroundColor Cyan
docker-compose -f docker/docker-compose.yml up --build
Write-Host "💥 Ультра-система готова на http://localhost:3000" -ForegroundColor Green
