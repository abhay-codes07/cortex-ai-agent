# Cortex Architecture (Phase 3)

## Current Foundation

- Frontend: Next.js App Router + Tailwind + Framer Motion scaffolding
- Backend: FastAPI with task APIs, system checks, and multi-agent base runtime
- Infra: Docker Compose setup for PostgreSQL + Redis

## Agent Base Layer

- Agent contracts:
  - messages
  - thoughts
  - actions
  - structured results
- Runtime context:
  - objective
  - short-term memory map
  - shared state
- Registry and bootstrap:
  - orchestrator
  - planner
  - research
  - decision
  - execution
  - memory
- Runtime executor:
  - deterministic sequence execution
  - transcript aggregation for UI streaming

## Upcoming Build Order

1. Orchestrator and planner workflow intelligence
2. Memory service wiring
3. Tool abstractions
4. Collaboration runtime and websocket stream
5. Dashboard and timeline visualization
6. Demo mode autopilot
