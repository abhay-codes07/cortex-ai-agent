from app.agents.contracts import AgentAction, AgentMessage, AgentResult, AgentThought


class CollaborationTranscript:
    def __init__(self) -> None:
        self.results: list[AgentResult] = []
        self.thoughts: list[AgentThought] = []
        self.actions: list[AgentAction] = []
        self.messages: list[AgentMessage] = []

    def add_result(self, result: AgentResult) -> None:
        self.results.append(result)
        self.thoughts.extend(result.thoughts)
        self.actions.extend(result.actions)
        self.messages.extend(result.messages)

    def as_dict(self) -> dict:
        return {
            'results': [result.model_dump(mode='json') for result in self.results],
            'thoughts': [thought.model_dump(mode='json') for thought in self.thoughts],
            'actions': [action.model_dump(mode='json') for action in self.actions],
            'messages': [message.model_dump(mode='json') for message in self.messages],
        }
