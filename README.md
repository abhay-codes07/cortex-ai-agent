# Cortex - Autonomous AI Workforce

A YC-style, demo-first multi-agent product where a team of AI agents plans, collaborates, executes, and learns from memory.

## Vision

Cortex is not a chatbot. It is an autonomous AI workforce. You submit one objective, and specialized AI agents coordinate to deliver outcomes with visible reasoning and live execution logs.

## What Is Live In Phase 8

- Premium Next.js frontend with startup-grade landing and command dashboard
- Mission control with task input, demo mode, and auto-run collaboration demo
- Animated agent network, live logs stream, and execution timeline playback
- Memory recall and task history context panels
- API-first data flow with deterministic fallback simulation for judge-safe demos
- Backend APIs for tasks, agents, workflows, collaboration, tools, and memory

## Dashboard Features

- Task input + run controls
- Demo mode with preloaded mission templates
- Agent status visualization (thinking, working, done)
- Live log stream and execution timeline
- Memory recall context
- Task history

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

## Screenshots

- `docs/screenshots/landing.png` (placeholder)
- `docs/screenshots/dashboard-overview.png` (placeholder)
- `docs/screenshots/live-collaboration.png` (placeholder)
- `docs/screenshots/demo-mode.png` (placeholder)

## Phase Plan

- Phase 1: Setup and repo initialization (complete)
- Phase 2: Backend core APIs (complete)
- Phase 3: Agent base system (complete)
- Phase 4: Orchestrator + planner workflow intelligence (complete)
- Phase 5: Memory system (complete)
- Phase 6: Tool execution layer (complete)
- Phase 7: Multi-agent collaboration (complete)
- Phase 8: Premium dashboard UI (complete)
- Phase 9: Realtime websocket stream
- Phase 10: Demo mode and polish
