#!/usr/bin/env powershell
$ErrorActionPreference = 'Stop'

$body = @{
  scenario_id = 'launch-sprint'
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/demo/run" -Method Post -ContentType "application/json" -Body $body
