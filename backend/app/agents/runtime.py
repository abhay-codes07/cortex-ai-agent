from app.agents.context import RuntimeContext
from app.agents.registry import AgentRegistry
from app.agents.sequence import DEFAULT_AGENT_SEQUENCE
from app.agents.transcript import CollaborationTranscript


class AgentRuntime:
    def __init__(self, registry: AgentRegistry):
        self.registry = registry
        self.sequence = DEFAULT_AGENT_SEQUENCE

    def run_once(self, context: RuntimeContext) -> CollaborationTranscript:
        transcript = CollaborationTranscript()
        for role in self.sequence:
            agent = self.registry.require(role)
            result = agent.run(context)
            transcript.add_result(result)
        return transcript
