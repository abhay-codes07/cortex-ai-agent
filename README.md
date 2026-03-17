# Cortex - Autonomous AI Workforce

A YC-style, demo-first multi-agent product where a team of AI agents plans, collaborates, executes, and learns from memory.

## Vision

Cortex is not a chatbot. It is an autonomous AI workforce. You submit one objective, and specialized AI agents coordinate to deliver outcomes with visible reasoning and live execution logs.

## What Is Live In Phase 2

- Monorepo foundation with `frontend`, `backend`, `infra`, and `docs`
- Next.js + Tailwind + Framer Motion frontend scaffold with premium landing shell
- FastAPI backend core API layer for tasks, status updates, and summaries
- SQLAlchemy task persistence model and automatic table initialization
- Redis-backed response caching for list/detail/summary reads
- Docker infrastructure for PostgreSQL and Redis

## Backend API Surface

- `GET /health`
- `GET /api/v1/status`
- `GET /api/v1/meta`
- `POST /api/v1/tasks`
- `GET /api/v1/tasks`
- `GET /api/v1/tasks/{task_id}`
- `PATCH /api/v1/tasks/{task_id}/status`
- `POST /api/v1/tasks/{task_id}/start`
- `GET /api/v1/tasks/summary`

## Monorepo Layout

- `frontend/`: Next.js App Router UI
- `backend/`: FastAPI service and multi-agent runtime foundation
- `infra/`: PostgreSQL + Redis compose stack
- `docs/`: Architecture, setup, and roadmap

## Quick Start

1. Copy env templates.
   - `cp .env.example .env`
   - `cp frontend/.env.local.example frontend/.env.local`
   - `cp backend/.env.example backend/.env`
2. Start infra: `docker compose -f infra/docker-compose.yml up -d`
3. Start backend: `cd backend && powershell ./run.ps1`
4. Start frontend: `cd frontend && npm install && npm run dev`

## Phase Plan

- Phase 1: Setup and repo initialization (complete)
- Phase 2: Backend core APIs (complete)
- Phase 3: Agent base system
- Phase 4: Orchestrator + planner
- Phase 5: Memory layer
- Phase 6: Tool execution layer
- Phase 7: Multi-agent collaboration
- Phase 8: Premium dashboard
- Phase 9: Realtime websocket stream
- Phase 10: Demo mode and polish
