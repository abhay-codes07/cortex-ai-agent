# Frontend Experience (Phase 9)

## Primary Views

- Landing page (`/`)
- Premium dashboard (`/dashboard`)

## Dashboard Modules

- Mission Control task composer
- Agent network visualization with live statuses
- Live logs stream panel
- Execution timeline panel
- Memory recall panel
- Task history panel

## Realtime UX

- WebSocket connection to `WS /api/v1/realtime/ws`
- Live connection state chip (`connecting`, `connected`, `disconnected`)
- Streaming event updates drive:
  - timeline cards
  - log lines
  - agent state transitions

## Demo Mode Guarantees

- Uses deterministic fallback simulation when backend is unreachable
- Streams staged timeline logs with no crashes
- Supports one-click collaboration auto-demo

## Screenshot Placeholders

- `docs/screenshots/landing.png`
- `docs/screenshots/dashboard-overview.png`
- `docs/screenshots/live-collaboration.png`
- `docs/screenshots/realtime-stream.png`
- `docs/screenshots/demo-mode.png`
