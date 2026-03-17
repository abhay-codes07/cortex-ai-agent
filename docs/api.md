# API Reference (Phase 4)

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

## Workflow run request

```json
{
  "title": "Launch sprint",
  "objective": "Plan and execute a startup launch sprint with clear milestones and timeline outputs."
}
```
