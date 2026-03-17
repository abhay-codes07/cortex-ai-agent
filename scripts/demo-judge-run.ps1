#!/usr/bin/env powershell
$ErrorActionPreference = 'Stop'

Write-Host 'Listing demo scenarios...'
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/demo/scenarios" -Method Get | Out-Null

Write-Host 'Running launch-sprint scenario...'
$body = @{ scenario_id = 'launch-sprint' } | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/demo/run" -Method Post -ContentType "application/json" -Body $body | Out-Null

Write-Host 'Checking realtime status...'
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/realtime/status" -Method Get
