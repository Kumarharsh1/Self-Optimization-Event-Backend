from fastapi import APIRouter
from app.engine.workflow_engine import WorkflowEngine

router = APIRouter(prefix="/events", tags=["Events"])
engine = WorkflowEngine()

@router.post("")
def trigger_event(event: dict):
    result = engine.process_event(event)
    return {
        "message": "Event processed",
        "result": result
    }
