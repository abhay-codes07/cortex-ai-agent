from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class DemoScenario(BaseModel):
    id: str
    title: str
    objective: str
    mode: str
    rounds: int = 2


class DemoRunRequest(BaseModel):
    scenario_id: str | None = None
    objective: str | None = Field(default=None, min_length=5, max_length=5000)


class DemoRunResponse(BaseModel):
    scenario: DemoScenario
    started_at: datetime
    completed_at: datetime
    result: dict[str, Any]


class DemoScenariosResponse(BaseModel):
    items: list[DemoScenario]
    count: int
