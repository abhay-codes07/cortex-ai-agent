from app.agents.base import BaseAgent
from app.agents.context import RuntimeContext
from app.agents.contracts import AgentResult
from app.agents.prompt_templates import ORCHESTRATOR_PROMPT
from app.agents.types import AgentRole


class OrchestratorAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(role=AgentRole.orchestrator, name='Orchestrator Agent')

    def run(self, context: RuntimeContext) -> AgentResult:
        thought = self.thought(
            step='Coordinate workflow',
            reasoning=f'{ORCHESTRATOR_PROMPT} Received objective and preparing handoff sequence across planner, research, and execution lanes.',
        )
        action = self.action('set_workflow', {'sequence': ['planner', 'research', 'decision', 'execution', 'memory']})
        message = self.message(AgentRole.planner, f'Break down this objective into clear steps: {context.objective}')

        context.set_state('workflow_sequence', ['planner', 'research', 'decision', 'execution', 'memory'])

        return AgentResult(
            agent=self.role,
            status='ok',
            output={'coordinated': True},
            thoughts=[thought],
            actions=[action],
            messages=[message],
        )
