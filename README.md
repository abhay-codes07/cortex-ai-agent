# Cortex - Autonomous AI Workforce

## ?? Vision

Cortex is not a chatbot. It is an autonomous AI workforce.

You provide a mission. A team of specialized AI agents gets to work in real time: planning, researching, deciding, executing, coordinating, and learning from memory.

The product is designed to impress judges in under 30 seconds through visible intelligence, live execution, and deterministic demo reliability.

## ?? How It Works

1. User submits an objective in the dashboard mission control.
2. Orchestrator profiles complexity and selects execution mode.
3. Planner generates milestone plan with owners and outcomes.
4. Research + Decision agents refine strategy with collaboration loops.
5. Execution agent calls tools (`web_search`, `execute_task`, `send_slack`, `send_email`).
6. Memory agent captures short-term context and persists long-term memory.
7. Realtime events stream over WebSockets to update the UI live.

## ?? Architecture

### Frontend

- Next.js App Router
- TailwindCSS
- Framer Motion
- Premium multi-panel dashboard:
  - mission control
  - agent network visualization
  - live logs
  - timeline
  - memory recall
  - history
  - demo autopilot

### Backend

- FastAPI
- PostgreSQL (tasks + long-term memory)
- Redis (caching)
- Realtime WebSocket manager and event bus

### Agent System

- Orchestrator Agent
- Planner Agent
- Research Agent
- Decision Agent
- Execution Agent
- Memory Agent

### Collaboration + Runtime

- Multi-round collaboration coordinator
- Inter-agent message bus and inbox delivery
- Structured transcript generation
- Workflow orchestration with state transitions

### Tooling Layer

- Email simulator
- Slack simulator
- Web search mock
- Task executor
- Tool registry + batch execution endpoints

## ? Tech Stack

- Frontend: Next.js, TypeScript, TailwindCSS, Framer Motion, Lucide
- Backend: FastAPI, Pydantic, SQLAlchemy
- Data: PostgreSQL, Redis
- Realtime: WebSockets
- DevOps: Docker Compose

## ?? Demo Instructions

### 1) Start infrastructure

```bash
docker compose -f infra/docker-compose.yml up -d
```

### 2) Start backend

```bash
cd backend
powershell ./run.ps1
```

### 3) Start frontend

```bash
cd frontend
npm install
npm run dev
```

### 4) Open dashboard

- `http://localhost:3000/dashboard`

### 5) Run judge-safe demos

```bash
powershell ./scripts/demo-workflow-run.ps1
powershell ./scripts/demo-collaboration-run.ps1
powershell ./scripts/demo-realtime-status.ps1
powershell ./scripts/demo-autopilot.ps1
```

## ?? Screenshots

- `docs/screenshots/landing.png` (placeholder)
- `docs/screenshots/dashboard-overview.png` (placeholder)
- `docs/screenshots/live-collaboration.png` (placeholder)
- `docs/screenshots/realtime-stream.png` (placeholder)
- `docs/screenshots/demo-autopilot.png` (placeholder)

## ?? Why This Wins

- Visible multi-agent coordination, not static chat output
- Live realtime stream of reasoning, actions, and tool calls
- Memory-backed behavior with recall + persistence loop
- Deterministic one-click demo autopilot for no-fail judging
- Clean modular architecture that scales beyond hackathon scope
