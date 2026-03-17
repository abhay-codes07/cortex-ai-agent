#!/usr/bin/env powershell
$ErrorActionPreference = 'Stop'

$body = @{
  title     = 'Collaboration Demo Task'
  objective = 'Coordinate a launch plan where multiple AI agents collaborate in real-time with tool calls.'
  rounds    = 2
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/collaboration/run" -Method Post -ContentType "application/json" -Body $body
