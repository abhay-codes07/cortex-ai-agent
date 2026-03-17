# Cortex Architecture (Phase 9)

## Current Foundation

- Frontend: Premium dashboard with live timeline/log panels and realtime status indicator
- Backend: FastAPI with task, memory, workflow, tools, collaboration, and realtime APIs
- Infra: Docker Compose setup for PostgreSQL + Redis

## Realtime Layer

- WebSocket endpoint:
  - `WS /api/v1/realtime/ws`
- Realtime manager:
  - connection tracking
  - broadcast fanout to all clients
- Event emission points:
  - task create/status updates
  - workflow step transitions
  - collaboration turns/rounds
  - tool execution callbacks
  - memory recall/persist events

## Frontend Streaming Behavior

- Dashboard opens websocket connection on load
- Realtime status chip shows `connecting|connected|disconnected`
- During live runs, websocket events append to:
  - timeline panel
  - log stream panel
  - agent node status transitions
- If websocket/backend is unavailable, deterministic fallback simulation still runs

## Upcoming Build Order

1. Demo mode autopilot polish
2. Final README/screenshots and launch narrative
