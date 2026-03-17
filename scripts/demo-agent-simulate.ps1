#!/usr/bin/env powershell
$ErrorActionPreference = 'Stop'

$body = @{
  task_id   = 'demo-phase3'
  objective = 'Coordinate a launch sprint with clear milestones and output summary'
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/agents/simulate" -Method Post -ContentType "application/json" -Body $body
