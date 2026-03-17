from dataclasses import dataclass


@dataclass
class ObjectiveProfile:
    objective: str
    complexity_score: int
    urgency_score: int
    research_depth: str
    execution_style: str


class ObjectiveAnalyzer:
    def analyze(self, objective: str) -> ObjectiveProfile:
        text = objective.lower()

        complexity = 1
        urgency = 1

        complexity_keywords = ['integrate', 'architecture', 'system', 'multi-agent', 'production', 'pipeline']
        urgency_keywords = ['today', 'asap', 'urgent', 'immediately', 'deadline', 'launch']

        complexity += sum(1 for token in complexity_keywords if token in text)
        urgency += sum(1 for token in urgency_keywords if token in text)

        return self.from_scores(objective=objective, complexity=complexity, urgency=urgency)

    def from_scores(self, objective: str, complexity: int, urgency: int) -> ObjectiveProfile:
        clamped_complexity = min(max(complexity, 1), 10)
        clamped_urgency = min(max(urgency, 1), 10)
        research_depth = 'deep' if clamped_complexity >= 4 else 'standard'
        execution_style = 'parallel' if clamped_complexity >= 5 else 'iterative'

        return ObjectiveProfile(
            objective=objective,
            complexity_score=clamped_complexity,
            urgency_score=clamped_urgency,
            research_depth=research_depth,
            execution_style=execution_style,
        )
