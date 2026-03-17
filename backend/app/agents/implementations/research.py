from app.agents.base import BaseAgent
from app.agents.context import RuntimeContext
from app.agents.contracts import AgentResult
from app.agents.prompt_templates import RESEARCH_PROMPT
from app.agents.types import AgentRole


class ResearchAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(role=AgentRole.research, name='Research Agent')

    def run(self, context: RuntimeContext) -> AgentResult:
        findings = [
            'Market pattern indicates fast iteration wins over large upfront planning.',
            'Concise execution milestones improve completion probability.',
            'Visible progress logs increase stakeholder trust during autonomous runs.',
        ]
        thought = self.thought(
            step='Collect references and context',
            reasoning=f'{RESEARCH_PROMPT} Compiling synthesized findings that the decision agent can evaluate for final path selection.',
        )
        action = self.action('collect_findings', {'findings_count': len(findings)})
        message = self.message(AgentRole.decision, 'Use these findings to select the best execution strategy.', {'findings': findings})

        context.remember('research_findings', findings)

        return AgentResult(
            agent=self.role,
            status='ok',
            output={'findings': findings},
            thoughts=[thought],
            actions=[action],
            messages=[message],
        )
