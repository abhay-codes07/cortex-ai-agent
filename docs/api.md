# API Reference (Phase 2)

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

## Sample create request

```json
{
  "title": "Launch growth experiment",
  "prompt": "Design and execute a multi-channel user acquisition experiment for 7 days."
}
```
