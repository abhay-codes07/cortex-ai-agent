# Local Setup Guide

## Prerequisites

- Node.js 20+
- Python 3.11+
- Docker Desktop

## Boot Sequence

1. `powershell ./scripts/bootstrap.ps1`
2. `cd backend && powershell ./run.ps1`
3. `cd frontend && npm install && npm run dev`

## Verify

- Frontend: http://localhost:3000
- Backend health: http://localhost:8000/health
