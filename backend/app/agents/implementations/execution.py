from app.agents.base import BaseAgent
from app.agents.context import RuntimeContext
from app.agents.contracts import AgentResult
from app.agents.prompt_templates import EXECUTION_PROMPT
from app.agents.types import AgentRole


class ExecutionAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(role=AgentRole.execution, name='Execution Agent')

    def run(self, context: RuntimeContext) -> AgentResult:
        strategy = context.get_state('selected_strategy', {})
        milestones = context.recall('plan_milestones', [])

        deliverables = [
            'Objective interpreted and execution lane activated',
            'Milestones completed with status evidence',
            'Final output packaged for stakeholder review',
        ]

        if milestones:
            deliverables.append(f"Executed {len(milestones)} planned milestones in coordinated sequence")

        thought = self.thought(
            step='Execute selected strategy',
            reasoning=f'{EXECUTION_PROMPT} Applying strategy into concrete deliverables with milestone-level completion evidence.',
        )
        action = self.action('execute_plan', {'strategy': strategy.get('strategy', 'default'), 'deliverables': deliverables})
        message = self.message(AgentRole.memory, 'Store execution context and outcomes for future recall.')

        context.set_state('deliverables', deliverables)
        context.add_timeline_event('executing', 'Execution agent completed deliverable run', {'deliverables': len(deliverables)})

        return AgentResult(
            agent=self.role,
            status='ok',
            output={'deliverables': deliverables},
            thoughts=[thought],
            actions=[action],
            messages=[message],
        )
