from app.agents.base import BaseAgent
from app.agents.context import RuntimeContext
from app.agents.contracts import AgentResult
from app.agents.prompt_templates import DECISION_PROMPT
from app.agents.types import AgentRole


class DecisionAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(role=AgentRole.decision, name='Decision Agent')

    def run(self, context: RuntimeContext) -> AgentResult:
        findings = context.recall('research_findings', [])
        plan = context.recall('plan_steps', [])

        selected_strategy = {
            'strategy': 'iterative_execution',
            'why': 'Combines fast loops, clear milestones, and transparent logs for dependable demos.',
            'inputs': {'plan_steps': len(plan), 'findings': len(findings)},
        }

        thought = self.thought(
            step='Select best strategy',
            reasoning=f'{DECISION_PROMPT} Prioritizing low-risk, high-visibility execution path aligned with speed and demo reliability.',
        )
        action = self.action('select_strategy', selected_strategy)
        message = self.message(AgentRole.execution, 'Execute with iterative milestones and stream visible progress.')

        context.set_state('selected_strategy', selected_strategy)

        return AgentResult(
            agent=self.role,
            status='ok',
            output={'selected_strategy': selected_strategy},
            thoughts=[thought],
            actions=[action],
            messages=[message],
        )
