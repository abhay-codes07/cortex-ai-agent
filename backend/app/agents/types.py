from enum import Enum


class AgentRole(str, Enum):
    orchestrator = 'orchestrator'
    planner = 'planner'
    research = 'research'
    decision = 'decision'
    execution = 'execution'
    memory = 'memory'
