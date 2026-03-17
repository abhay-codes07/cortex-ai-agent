# Cortex - Autonomous AI Workforce

A YC-style, demo-first multi-agent product where a team of AI agents plans, collaborates, executes, and learns from memory.

## Vision

Cortex is not a chatbot. It is an autonomous AI workforce. You submit one objective, and specialized AI agents coordinate to deliver outcomes with visible reasoning and live execution logs.

## What Is Live In Phase 7

- FastAPI backend core APIs for tasks, workflows, memory, tools, and collaboration
- SQLAlchemy task + memory persistence in PostgreSQL
- Redis-backed caching for task and memory reads
- Modular multi-agent runtime with orchestrator + planner intelligence
- Tool execution layer with pluggable abstractions
- Multi-agent collaboration runtime:
  - message bus and inbox delivery
  - multi-round execution loops
  - collaboration session events and replayable transcript

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
- `POST /api/v1/collaboration/run`
- `GET /api/v1/collaboration/sessions`
- `POST /api/v1/memory/records`
- `GET /api/v1/memory/recent`
- `POST /api/v1/memory/recall`
- `GET /api/v1/tools`
- `POST /api/v1/tools/execute`
- `POST /api/v1/tools/execute/batch`

## Demo Helpers

- `powershell ./scripts/demo-agent-simulate.ps1`
- `powershell ./scripts/demo-workflow-run.ps1`
- `powershell ./scripts/demo-memory-recall.ps1`
- `powershell ./scripts/demo-tools.ps1`
- `powershell ./scripts/demo-collaboration-run.ps1`

## Phase Plan

- Phase 1: Setup and repo initialization (complete)
- Phase 2: Backend core APIs (complete)
- Phase 3: Agent base system (complete)
- Phase 4: Orchestrator + planner workflow intelligence (complete)
- Phase 5: Memory system (complete)
- Phase 6: Tool execution layer (complete)
- Phase 7: Multi-agent collaboration (complete)
- Phase 8: Premium dashboard
- Phase 9: Realtime websocket stream
- Phase 10: Demo mode and polish
