# Cortex - Autonomous AI Workforce

A YC-style, demo-first multi-agent product where a team of AI agents plans, collaborates, executes, and learns from memory.

## Vision

Cortex is not a chatbot. It is an autonomous AI workforce. You submit one objective, and specialized AI agents coordinate to deliver outcomes with visible reasoning and live execution logs.

## What Is Live In Phase 1

- Monorepo foundation with `frontend`, `backend`, `infra`, and `docs`
- Next.js + Tailwind + Framer Motion frontend scaffold with premium landing shell
- FastAPI backend scaffold with health and status routes
- Docker infrastructure for PostgreSQL and Redis
- Developer scripts and setup documentation

## Monorepo Layout

- `frontend/`: Next.js App Router UI
- `backend/`: FastAPI service and future multi-agent runtime
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
- Phase 2: Backend core APIs
- Phase 3: Agent base system
- Phase 4: Orchestrator + planner
- Phase 5: Memory layer
- Phase 6: Tool execution layer
- Phase 7: Multi-agent collaboration
- Phase 8: Premium dashboard
- Phase 9: Realtime websocket stream
- Phase 10: Demo mode and polish
