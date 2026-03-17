# Cortex Architecture (Phase 6)

## Current Foundation

- Frontend: Next.js App Router + Tailwind + Framer Motion scaffolding
- Backend: FastAPI with task, memory, workflow, and tools APIs
- Infra: Docker Compose setup for PostgreSQL + Redis

## Tool System

- Tool abstraction:
  - base tool interface
  - typed tool call/result contracts
  - registry + bootstrap wiring
- Tool implementations:
  - email simulator
  - slack simulator
  - web search mock
  - task executor
- Tool service:
  - single and batch execution
  - API exposure for direct demo triggers

## Workflow Integration

1. Workflow injects a tool executor callback into runtime context.
2. Execution agent performs tool calls as part of milestone completion.
3. Tool outputs are added to timeline and stored in memory snapshots.

## Upcoming Build Order

1. Multi-agent collaboration UX layer
2. Frontend luxury dashboard
3. Realtime websocket stream
4. Demo mode autopilot
