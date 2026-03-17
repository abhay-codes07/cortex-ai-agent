#!/usr/bin/env powershell
$ErrorActionPreference = 'Stop'

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/realtime/status" -Method Get
