# Cortex — Autonomous AI Workforce

Phase 1 scaffolding for a production-grade multi-agent platform.

## Monorepo Layout

- `frontend/` Next.js App Router + Tailwind + Framer Motion + shadcn-ready UI foundations
- `backend/` FastAPI service for orchestration, memory, tools, and realtime streams
- `infra/` Docker Compose for PostgreSQL and Redis
- `docs/` Product and architecture docs

## Quick Start

1. Copy env templates:
   - `cp .env.example .env`
   - `cp frontend/.env.local.example frontend/.env.local`
   - `cp backend/.env.example backend/.env`
2. Start data services:
   - `docker compose -f infra/docker-compose.yml up -d`
3. Start backend:
   - `cd backend && python -m venv .venv && .venv\\Scripts\\activate && pip install -r requirements.txt && uvicorn app.main:app --reload --port 8000`
4. Start frontend:
   - `cd frontend && npm install && npm run dev`

## Phase 1 Status

- [x] Repo initialized on `main`
- [x] Frontend scaffolded
- [x] Backend scaffolded
- [x] Infra baseline added
- [x] Foundational docs added

Later phases will add multi-agent runtime, tools, memory intelligence, websockets, and demo mode polish.
