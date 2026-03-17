# Cortex Architecture (Phase 5)

## Current Foundation

- Frontend: Next.js App Router + Tailwind + Framer Motion scaffolding
- Backend: FastAPI with task APIs, memory APIs, and orchestrated multi-agent runtime
- Infra: Docker Compose setup for PostgreSQL + Redis

## Memory System

- Short-term memory:
  - runtime context memory map per workflow
  - timeline event tracking per workflow
- Long-term memory (PostgreSQL):
  - `memory_records` table
  - objective, summary, strategy, workflow mode
  - plan steps, deliverables, tags
- Recall engine:
  - lexical relevance scoring against objective/summary/tags
  - Redis-cached recall responses for fast demo playback

## Workflow Memory Loop

1. Recall top related memories for incoming objective.
2. Pass memory hints into orchestrator/planner context.
3. Execute full agent pipeline.
4. Persist new long-term memory record from final snapshot.

## Upcoming Build Order

1. Tool abstractions
2. Collaboration runtime and websocket stream
3. Dashboard and timeline visualization
4. Demo mode autopilot
