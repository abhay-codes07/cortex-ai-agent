from dataclasses import dataclass

from app.agents.intelligence.objective_analyzer import ObjectiveProfile


@dataclass
class PlanMilestone:
    title: str
    owner: str
    outcome: str
    sequence: int


class MilestonePlanner:
    def build(self, profile: ObjectiveProfile) -> list[PlanMilestone]:
        base = [
            PlanMilestone(
                title='Define success criteria and constraints',
                owner='Planner Agent',
                outcome='Shared acceptance criteria documented',
                sequence=1,
            ),
            PlanMilestone(
                title='Collect evidence and options',
                owner='Research Agent',
                outcome='Decision-ready findings assembled',
                sequence=2,
            ),
            PlanMilestone(
                title='Select execution strategy',
                owner='Decision Agent',
                outcome='Final strategy approved with rationale',
                sequence=3,
            ),
            PlanMilestone(
                title='Execute milestones and package output',
                owner='Execution Agent',
                outcome='Deliverables completed and summarized',
                sequence=4,
            ),
        ]

        if profile.complexity_score >= 5:
            base.insert(
                3,
                PlanMilestone(
                    title='Run orchestration checkpoint',
                    owner='Orchestrator Agent',
                    outcome='Cross-agent dependencies validated',
                    sequence=4,
                ),
            )
            for index, milestone in enumerate(base, start=1):
                milestone.sequence = index

        return base
