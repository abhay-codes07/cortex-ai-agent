# Cortex - Autonomous AI Workforce

Autonomous multi-agent system that plans, reasons, and executes tasks in real time.

![Python](https://img.shields.io/badge/Python-3.11%2B-0F172A?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-0F172A?style=for-the-badge&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-Frontend-0F172A?style=for-the-badge&logo=nextdotjs&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data-0F172A?style=for-the-badge&logo=postgresql&logoColor=white)
![Hackathon Project](https://img.shields.io/badge/Hackathon-Airia%20AI%20Agents-0F172A?style=for-the-badge)

---

## What It Feels Like

You give a task -> a team of AI agents gets to work.

- Plan
- Research
- Decide
- Execute
- Learn

---

## Agent Flow Diagram

```mermaid
flowchart LR
    U[User Task] --> O[Orchestrator]
    O --> P[Planner]
    P --> R[Research]
    R --> D[Decision]
    D --> E[Execution]
    E --> M[Memory]
```

---

## System Architecture

```mermaid
flowchart LR
    F[Frontend<br/>Next.js Dashboard] --> B[Backend<br/>FastAPI]
    B --> A[Agent Runtime]
    A --> T[Tool Layer]
    B --> DB[(PostgreSQL + Redis)]
    T --> DB
```

---

## Agents Overview

| Agent | Role |
|---|---|
| Orchestrator Agent | Coordinates the full workflow and agent handoffs |
| Planner Agent | Breaks objectives into actionable milestones |
| Research Agent | Gathers context and supporting signals |
| Decision Agent | Chooses strategy from available evidence |
| Execution Agent | Runs tool-driven actions and completes tasks |
| Memory Agent | Stores short-term + long-term context for recall |

---

## Key Features

- `?` Real-time execution
- `??` Multi-agent collaboration
- `??` Memory system
- `??` Tool calling
- `??` Live logs

---

## Demo

Demo mode runs curated scenarios with one-click autopilot for reliable judging.

![Demo](docs/demo.gif)

---

## UI Preview

![Dashboard](docs/dashboard.png)

---

## Quick Start

```bash
git clone https://github.com/abhay-codes07/cortex-ai-agent.git
cd cortex-ai-agent
docker compose -f infra/docker-compose.yml up -d
```

```bash
cd backend
powershell ./run.ps1
```

```bash
cd frontend
npm install
npm run dev
```

Open: `http://localhost:3000/dashboard`

---

## Why This Is Different

- Not chatbot -> execution system
- Visible reasoning and runtime traces
- True multi-agent coordination
- Real-time intelligence in action
