from app.agents.base import BaseAgent
from app.agents.context import RuntimeContext
from app.agents.contracts import AgentResult
from app.agents.prompt_templates import RESEARCH_PROMPT
from app.agents.types import AgentRole


class ResearchAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(role=AgentRole.research, name='Research Agent')

    def run(self, context: RuntimeContext) -> AgentResult:
        plan_steps = context.recall('plan_steps', [])
        workflow_mode = context.get_state('workflow_mode', 'iterative-safe')
        inbox = context.read_inbox(self.role.value)

        findings = [
            'Fast iteration beats oversized upfront planning for demo velocity.',
            'Visible milestone updates increase confidence in autonomous systems.',
            f'Workflow mode {workflow_mode} should prioritize transparent status transitions.',
        ]

        if len(plan_steps) >= 5:
            findings.append('Complex plans benefit from orchestration checkpoints before execution handoff.')
        if inbox:
            findings.append('Collaboration messages suggest refining assumptions before final decision step.')

        thought = self.thought(
            step='Collect references and context',
            reasoning=f'{RESEARCH_PROMPT} Compiling findings that directly support planner milestones and orchestration mode.',
        )
        action = self.action('collect_findings', {'findings_count': len(findings), 'aligned_plan_steps': len(plan_steps)})
        message = self.message(
            AgentRole.decision,
            'Use these findings to select the best execution strategy.',
            {'findings': findings},
        )

        context.remember('research_findings', findings)
        context.add_timeline_event('researching', 'Research agent synthesized findings', {'findings': len(findings)})

        return AgentResult(
            agent=self.role,
            status='ok',
            output={'findings': findings},
            thoughts=[thought],
            actions=[action],
            messages=[message],
        )
