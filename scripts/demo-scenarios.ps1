#!/usr/bin/env powershell
$ErrorActionPreference = 'Stop'

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/demo/scenarios" -Method Get
