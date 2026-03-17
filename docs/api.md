# API Reference (Phase 9)

## Health and system

- `GET /health`
- `GET /api/v1/status`
- `GET /api/v1/meta`
- `GET /api/v1/system`

## Realtime

- `GET /api/v1/realtime/status`
- `WS /api/v1/realtime/ws`

## Tasks

- `POST /api/v1/tasks`
- `GET /api/v1/tasks`
- `GET /api/v1/tasks/{task_id}`
- `PATCH /api/v1/tasks/{task_id}/status`
- `POST /api/v1/tasks/{task_id}/start`
- `GET /api/v1/tasks/summary`

## Agents

- `GET /api/v1/agents`
- `POST /api/v1/agents/simulate`

## Workflows

- `POST /api/v1/workflows/run`

## Collaboration

- `POST /api/v1/collaboration/run`
- `GET /api/v1/collaboration/sessions`

## Memory

- `POST /api/v1/memory/records`
- `GET /api/v1/memory/recent`
- `POST /api/v1/memory/recall`

## Tools

- `GET /api/v1/tools`
- `POST /api/v1/tools/execute`
- `POST /api/v1/tools/execute/batch`

## Realtime event shape

```json
{
  "id": "uuid",
  "type": "event",
  "stage": "executing",
  "message": "execution agent started",
  "metadata": {
    "task_id": "..."
  },
  "timestamp": "2026-03-17T00:00:00.000000"
}
```
