#!/usr/bin/env powershell
$ErrorActionPreference = 'Stop'

$body = @{
  title     = 'Demo Workflow Task'
  objective = 'Plan and execute a YC launch sprint for Cortex with clear milestones, strategy, and deliverables.'
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/workflows/run" -Method Post -ContentType "application/json" -Body $body
