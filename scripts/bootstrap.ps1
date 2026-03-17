#!/usr/bin/env powershell
$ErrorActionPreference = 'Stop'

Write-Host 'Starting Cortex infrastructure...'
docker compose -f infra/docker-compose.yml up -d

Write-Host 'Cortex setup complete. Start backend and frontend in separate terminals.'
