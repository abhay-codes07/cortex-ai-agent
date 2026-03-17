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
        profile = context.recall('objective_profile', {})
        inbox = context.read_inbox(self.role.value)

        complexity = int(profile.get('complexity_score', 1))
        style = 'parallel_execution' if complexity >= 5 else 'iterative_execution'
        confidence = 'high' if len(findings) >= 4 else 'medium'

        selected_strategy = {
            'strategy': style,
            'why': 'Balances speed with reliability while preserving visible agent reasoning.',
            'inputs': {'plan_steps': len(plan), 'findings': len(findings), 'complexity': complexity, 'inbox': len(inbox)},
            'confidence': confidence,
        }

        thought = self.thought(
            step='Select best strategy',
            reasoning=f'{DECISION_PROMPT} Chose {style} path using plan depth and research confidence.',
        )
        action = self.action('select_strategy', selected_strategy)
        message = self.message(AgentRole.execution, 'Execute selected strategy and stream milestone completion logs.')

        context.set_state('selected_strategy', selected_strategy)
        context.add_timeline_event('deciding', 'Decision agent finalized execution strategy', {'strategy': style})

        return AgentResult(
            agent=self.role,
            status='ok',
            output={'selected_strategy': selected_strategy},
            thoughts=[thought],
            actions=[action],
            messages=[message],
        )
