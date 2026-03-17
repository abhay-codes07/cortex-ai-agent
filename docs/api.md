# API Reference (Phase 7)

## Health and system

- `GET /health`
- `GET /api/v1/status`
- `GET /api/v1/meta`
- `GET /api/v1/system`

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

## Collaboration run request

```json
{
  "title": "Collab demo",
  "objective": "Coordinate a launch plan where multiple AI agents collaborate in real-time with tool calls.",
  "rounds": 2
}
```
