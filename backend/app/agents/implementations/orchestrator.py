from app.agents.base import BaseAgent
from app.agents.context import RuntimeContext
from app.agents.contracts import AgentResult
from app.agents.intelligence import ObjectiveAnalyzer
from app.agents.prompt_templates import ORCHESTRATOR_PROMPT
from app.agents.types import AgentRole


class OrchestratorAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(role=AgentRole.orchestrator, name='Orchestrator Agent')
        self.analyzer = ObjectiveAnalyzer()

    def run(self, context: RuntimeContext) -> AgentResult:
        profile = self.analyzer.analyze(context.objective)
        workflow_mode = 'parallel-fastlane' if profile.execution_style == 'parallel' else 'iterative-safe'
        memory_hints = context.recall('memory_hints', [])

        hint_note = f' using {len(memory_hints)} memory hints' if memory_hints else ''
        thought = self.thought(
            step='Coordinate workflow',
            reasoning=f'{ORCHESTRATOR_PROMPT} Objective analyzed with complexity={profile.complexity_score}; selecting {workflow_mode} mode{hint_note}.',
        )
        action = self.action(
            'set_workflow',
            {
                'sequence': ['planner', 'research', 'decision', 'execution', 'memory'],
                'mode': workflow_mode,
                'complexity_score': profile.complexity_score,
                'urgency_score': profile.urgency_score,
                'memory_hints_count': len(memory_hints),
            },
        )
        message = self.message(
            AgentRole.planner,
            f'Create an executable plan in {workflow_mode} mode for: {context.objective}',
            {'memory_hints': memory_hints[:2]},
        )

        context.remember(
            'objective_profile',
            {
                'complexity_score': profile.complexity_score,
                'urgency_score': profile.urgency_score,
                'research_depth': profile.research_depth,
                'execution_style': profile.execution_style,
            },
        )
        context.set_state('workflow_mode', workflow_mode)
        context.set_state('workflow_sequence', ['planner', 'research', 'decision', 'execution', 'memory'])
        context.add_timeline_event('orchestrating', 'Orchestrator selected workflow mode', {'mode': workflow_mode})

        return AgentResult(
            agent=self.role,
            status='ok',
            output={'coordinated': True, 'workflow_mode': workflow_mode, 'memory_hints': memory_hints[:2]},
            thoughts=[thought],
            actions=[action],
            messages=[message],
        )
