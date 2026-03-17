#!/usr/bin/env powershell
$ErrorActionPreference = 'Stop'

$recallBody = @{
  objective = 'Plan and execute a startup launch sprint with clear milestones and timeline outputs.'
  limit     = 5
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/memory/recall" -Method Post -ContentType "application/json" -Body $recallBody
