# Cortex - Autonomous AI Workforce

A YC-style, demo-first multi-agent product where a team of AI agents plans, collaborates, executes, and learns from memory.

## Vision

Cortex is not a chatbot. It is an autonomous AI workforce. You submit one objective, and specialized AI agents coordinate to deliver outcomes with visible reasoning and live execution logs.

## What Is Live In Phase 6

- FastAPI backend core APIs for tasks, memory, workflows, and tools
- SQLAlchemy task + memory persistence in PostgreSQL
- Redis-backed caching for task and memory reads
- Modular multi-agent runtime with orchestrator + planner intelligence
- Tool execution layer with abstract registry and pluggable tools:
  - email simulator
  - slack simulator
  - web search mock
  - task executor
- Workflow tool-calling integration with timeline evidence and memory capture

## Backend API Surface

- `GET /health`
- `GET /api/v1/status`
- `GET /api/v1/meta`
- `GET /api/v1/system`
- `POST /api/v1/tasks`
- `GET /api/v1/tasks`
- `GET /api/v1/tasks/{task_id}`
- `PATCH /api/v1/tasks/{task_id}/status`
- `POST /api/v1/tasks/{task_id}/start`
- `GET /api/v1/tasks/summary`
- `GET /api/v1/agents`
- `POST /api/v1/agents/simulate`
- `POST /api/v1/workflows/run`
- `POST /api/v1/memory/records`
- `GET /api/v1/memory/recent`
- `POST /api/v1/memory/recall`
- `GET /api/v1/tools`
- `POST /api/v1/tools/execute`
- `POST /api/v1/tools/execute/batch`

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

## Demo Helpers

- `powershell ./scripts/demo-agent-simulate.ps1`
- `powershell ./scripts/demo-workflow-run.ps1`
- `powershell ./scripts/demo-memory-recall.ps1`
- `powershell ./scripts/demo-tools.ps1`

## Phase Plan

- Phase 1: Setup and repo initialization (complete)
- Phase 2: Backend core APIs (complete)
- Phase 3: Agent base system (complete)
- Phase 4: Orchestrator + planner workflow intelligence (complete)
- Phase 5: Memory system (complete)
- Phase 6: Tool execution layer (complete)
- Phase 7: Multi-agent collaboration
- Phase 8: Premium dashboard
- Phase 9: Realtime websocket stream
- Phase 10: Demo mode and polish
