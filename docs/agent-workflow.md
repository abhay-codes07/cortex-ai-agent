# Agent Workflow (Phase 5)

1. Workflow starts by recalling relevant long-term memory records from PostgreSQL + Redis cache.
2. Orchestrator analyzes objective complexity and uses memory hints to choose workflow mode.
3. Planner generates milestone plan and injects strongest recalled insight.
4. Research aligns findings to planned milestones.
5. Decision selects strategy from profile + findings.
6. Execution completes deliverables with milestone evidence.
7. Memory agent captures snapshot and workflow service persists long-term memory record.

This produces an end-to-end memory loop: recall before execution, persist after execution.
