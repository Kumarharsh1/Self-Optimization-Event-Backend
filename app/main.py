from fastapi import FastAPI
from app.api.events import router as event_router

app = FastAPI(title="OrchestrAI Workflow Engine")

app.include_router(event_router)

@app.get("/")
def health():
    return {
        "status": "running",
        "engine": "Self-Optimizing Workflow Engine"
    }
