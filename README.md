# Cortex - Autonomous AI Workforce

A YC-style, demo-first multi-agent product where a team of AI agents plans, collaborates, executes, and learns from memory.

## Vision

Cortex is not a chatbot. It is an autonomous AI workforce. You submit one objective, and specialized AI agents coordinate to deliver outcomes with visible reasoning and live execution logs.

## What Is Live In Phase 9

- Premium frontend command dashboard with mission control, agent network, logs, timeline, memory, and history panels
- Full backend API surface for tasks, workflows, collaboration, tools, and memory
- Realtime websocket streaming layer from backend to dashboard
- Live run telemetry:
  - agent step transitions
  - tool execution events
  - task status updates
  - memory recall/persist events
- Deterministic fallback simulation remains available for fail-safe demos

## Backend API Surface

- `GET /health`
- `GET /api/v1/status`
- `GET /api/v1/meta`
- `GET /api/v1/system`
- `GET /api/v1/realtime/status`
- `WS /api/v1/realtime/ws`
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
- `powershell ./scripts/demo-realtime-status.ps1`

## Phase Plan

- Phase 1: Setup and repo initialization (complete)
- Phase 2: Backend core APIs (complete)
- Phase 3: Agent base system (complete)
- Phase 4: Orchestrator + planner workflow intelligence (complete)
- Phase 5: Memory system (complete)
- Phase 6: Tool execution layer (complete)
- Phase 7: Multi-agent collaboration (complete)
- Phase 8: Premium dashboard UI (complete)
- Phase 9: Realtime websocket stream (complete)
- Phase 10: Demo mode and polish
