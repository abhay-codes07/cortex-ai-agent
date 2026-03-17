from datetime import datetime

from sqlalchemy.orm import Session

from app.schemas.collaboration import CollaborationRunRequest
from app.schemas.demo import DemoRunRequest, DemoRunResponse, DemoScenario, DemoScenariosResponse
from app.schemas.workflow import WorkflowRunRequest
from app.services.collaboration_service import CollaborationService
from app.services.realtime_service import emit_event
from app.services.workflow_service import WorkflowService


class DemoService:
    def __init__(self, db: Session):
        self.workflow_service = WorkflowService(db)
        self.collaboration_service = CollaborationService(db)

    def scenarios(self) -> DemoScenariosResponse:
        items = [
            DemoScenario(
                id='launch-sprint',
                title='Launch Sprint Orchestration',
                objective='Plan and execute a 7-day launch sprint with milestones, ownership, and visible execution logs.',
                mode='workflow',
                rounds=2,
            ),
            DemoScenario(
                id='collab-war-room',
                title='Collaboration War Room',
                objective='Coordinate a cross-functional war room where agents collaborate in multiple rounds and execute tools.',
                mode='collaboration',
                rounds=2,
            ),
            DemoScenario(
                id='investor-readout',
                title='Investor Readout Simulation',
                objective='Prepare an investor-grade execution brief with memory recall, strategy selection, and delivery artifacts.',
                mode='workflow',
                rounds=2,
            ),
        ]
        return DemoScenariosResponse(items=items, count=len(items))

    def run(self, payload: DemoRunRequest) -> DemoRunResponse:
        scenario = self._resolve_scenario(payload)
        started_at = datetime.utcnow()
        emit_event('demo', f'Demo scenario started: {scenario.title}', {'scenario_id': scenario.id})

        if scenario.mode == 'collaboration':
            result = self.collaboration_service.run(
                CollaborationRunRequest(
                    title=scenario.title,
                    objective=scenario.objective,
                    rounds=scenario.rounds,
                )
            )
            result_payload = result.model_dump(mode='json')
        else:
            result = self.workflow_service.run(
                WorkflowRunRequest(
                    title=scenario.title,
                    objective=scenario.objective,
                )
            )
            result_payload = result.model_dump(mode='json')

        completed_at = datetime.utcnow()
        emit_event('demo', f'Demo scenario completed: {scenario.title}', {'scenario_id': scenario.id})

        return DemoRunResponse(
            scenario=scenario,
            started_at=started_at,
            completed_at=completed_at,
            result=result_payload,
        )

    def _resolve_scenario(self, payload: DemoRunRequest) -> DemoScenario:
        scenarios = self.scenarios().items
        if payload.scenario_id:
            match = next((scenario for scenario in scenarios if scenario.id == payload.scenario_id), None)
            if match:
                return match

        if payload.objective:
            return DemoScenario(
                id='custom-objective',
                title='Custom Demo Objective',
                objective=payload.objective,
                mode='workflow',
                rounds=2,
            )

        return scenarios[0]
