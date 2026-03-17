# Cortex Architecture (Phase 4)

## Current Foundation

- Frontend: Next.js App Router + Tailwind + Framer Motion scaffolding
- Backend: FastAPI with task APIs, system checks, and orchestrated multi-agent runtime
- Infra: Docker Compose setup for PostgreSQL + Redis

## Orchestrator + Planner Intelligence

- Objective analysis:
  - complexity scoring
  - urgency scoring
  - execution style recommendation
- Dynamic planning:
  - milestone generation with owners
  - plan summary formatting for UI
- Orchestration:
  - role-to-stage state machine
  - automatic task status transitions
  - combined workflow timeline stream

## Upcoming Build Order

1. Memory service wiring
2. Tool abstractions
3. Collaboration runtime and websocket stream
4. Dashboard and timeline visualization
5. Demo mode autopilot
