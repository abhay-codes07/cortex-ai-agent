from app.agents.base import BaseAgent
from app.agents.context import RuntimeContext
from app.agents.contracts import AgentResult
from app.agents.intelligence import MilestonePlanner, ObjectiveAnalyzer, PlanFormatter
from app.agents.prompt_templates import PLANNER_PROMPT
from app.agents.types import AgentRole


class PlannerAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(role=AgentRole.planner, name='Planner Agent')
        self.milestone_planner = MilestonePlanner()
        self.formatter = PlanFormatter()
        self.analyzer = ObjectiveAnalyzer()

    def run(self, context: RuntimeContext) -> AgentResult:
        profile_data = context.recall('objective_profile', {})
        profile = self.analyzer.from_scores(
            objective=context.objective,
            complexity=int(profile_data.get('complexity_score', 1)),
            urgency=int(profile_data.get('urgency_score', 1)),
        )

        milestones = self.milestone_planner.build(profile)
        plan_steps = self.formatter.summarize(milestones)

        thought = self.thought(
            step='Break objective into plan',
            reasoning=f'{PLANNER_PROMPT} Built {len(plan_steps)} milestones tuned for complexity score {profile.complexity_score}.',
        )
        action = self.action('draft_plan', {'steps': plan_steps, 'milestone_count': len(milestones)})
        message = self.message(AgentRole.research, 'Gather evidence and options aligned with these milestones.')

        context.remember('plan_steps', plan_steps)
        context.remember('plan_milestones', [m.__dict__ for m in milestones])
        context.add_timeline_event('planning', 'Planner generated milestone plan', {'milestones': len(milestones)})

        return AgentResult(
            agent=self.role,
            status='ok',
            output={'plan_steps': plan_steps, 'milestones': [m.__dict__ for m in milestones]},
            thoughts=[thought],
            actions=[action],
            messages=[message],
        )
