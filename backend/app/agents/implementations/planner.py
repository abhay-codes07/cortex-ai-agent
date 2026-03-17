from app.agents.base import BaseAgent
from app.agents.context import RuntimeContext
from app.agents.contracts import AgentResult
from app.agents.prompt_templates import PLANNER_PROMPT
from app.agents.types import AgentRole


class PlannerAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(role=AgentRole.planner, name='Planner Agent')

    def run(self, context: RuntimeContext) -> AgentResult:
        steps = [
            'Clarify expected output and constraints',
            'Collect required information and assumptions',
            'Choose best execution strategy',
            'Execute tasks and validate output',
        ]
        thought = self.thought(
            step='Break objective into plan',
            reasoning=f'{PLANNER_PROMPT} Constructing a practical 4-step plan that can be executed in sequence by specialized agents.',
        )
        action = self.action('draft_plan', {'steps': steps})
        message = self.message(AgentRole.research, 'Gather evidence and options to support the proposed plan.')

        context.remember('plan_steps', steps)

        return AgentResult(
            agent=self.role,
            status='ok',
            output={'plan_steps': steps},
            thoughts=[thought],
            actions=[action],
            messages=[message],
        )
