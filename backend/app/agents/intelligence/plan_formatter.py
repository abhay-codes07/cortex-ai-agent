from app.agents.intelligence.milestone_planner import PlanMilestone


class PlanFormatter:
    def summarize(self, milestones: list[PlanMilestone]) -> list[str]:
        return [f"{m.sequence}. {m.title} ({m.owner})" for m in milestones]
