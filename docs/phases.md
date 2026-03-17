# Phase Plan

## Phase 1 - Project Setup + Repo Init

- [x] Initialize git on `main`
- [x] Add monorepo folder structure
- [x] Scaffold frontend and backend applications
- [x] Add local infra dependencies
- [x] Add baseline docs and env templates

## Phase 2 - Backend Core APIs

- [x] Introduce SQLAlchemy task model and DB session layer
- [x] Add task CRUD-style API endpoints
- [x] Add task status lifecycle update endpoints
- [x] Add summary and history endpoints
- [x] Add Redis-backed cache layer for read-heavy endpoints

## Phase 3 - Agent Base System

- [x] Add typed agent contracts and roles
- [x] Add runtime context with short-term memory state
- [x] Add pluggable base agent abstraction
- [x] Add agent registry and default bootstrap wiring
- [x] Add six base agent implementations
- [x] Add collaboration transcript aggregator
- [x] Add deterministic simulation endpoint

## Phase 4 - Orchestrator + Planner

- [x] Add objective analyzer with complexity and urgency scoring
- [x] Add dynamic milestone planning with ownership mapping
- [x] Add orchestration state machine for lifecycle transitions
- [x] Add workflow run service to coordinate full agent sequence
- [x] Add workflow API endpoint with timeline and transcript output

## Phase 5 - Memory System

- [x] Add persistent memory record model in PostgreSQL
- [x] Add memory repository and service layer
- [x] Add memory create/recent/recall APIs
- [x] Add Redis-cached memory recall responses
- [x] Integrate recall-before-run and persist-after-run workflow loop

## Next Phases

- Phase 6: Tool execution
- Phase 7: Multi-agent collaboration
- Phase 8: Frontend luxury UI
- Phase 9: Realtime WebSockets
- Phase 10: Polish + demo mode
