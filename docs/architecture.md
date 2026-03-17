# Cortex Architecture (Phase 7)

## Current Foundation

- Frontend: Next.js App Router + Tailwind + Framer Motion scaffolding
- Backend: FastAPI with task, memory, workflow, tools, and collaboration APIs
- Infra: Docker Compose setup for PostgreSQL + Redis

## Collaboration Runtime

- Collaboration message bus:
  - publish/drain per recipient agent
  - delivered + pending message tracking
- Collaboration session model:
  - session id, rounds, event log
  - per-agent turn results
- Multi-round execution:
  - runtime executes agents across configurable rounds
  - inbox context delivered each turn
  - timeline events generated for every turn and round

## UX Impact

- Judges can see explicit cross-agent communication loops.
- Transcript now includes multi-round evidence, not just single-pass output.
- Sessions endpoint enables replay/debug in dashboard timeline views.

## Upcoming Build Order

1. Frontend luxury dashboard and agent visualization
2. Realtime websocket stream
3. Demo mode autopilot and final polish
