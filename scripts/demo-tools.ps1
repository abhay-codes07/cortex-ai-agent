#!/usr/bin/env powershell
$ErrorActionPreference = 'Stop'

$body = @{
  calls = @(
    @{ name = 'web_search'; payload = @{ query = 'yc launch demo strategy' } },
    @{ name = 'send_slack'; payload = @{ channel = '#cortex-live'; message = 'Tool layer demo run' } },
    @{ name = 'send_email'; payload = @{ recipient = 'founder@cortex.ai'; subject = 'Tool Demo'; body = 'All systems operational' } }
  )
} | ConvertTo-Json -Depth 4

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/tools/execute/batch" -Method Post -ContentType "application/json" -Body $body
