from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.main import run_task

app = FastAPI(title="AI Meta-Agent Orchestration API")

# Dummy user DB
users_db = {
    "user123": {
        "name": "Arooj",
        "role": "student",
        "capabilities": ["summarizer", "deadline_extractor"]
    },
    "admin001": {
        "name": "Super Admin",
        "role": "admin",
        "capabilities": ["*"]
    }
}

class TaskRequest(BaseModel):
    user_id: str
    user_query: str

@app.post("/run-task")
def handle_task(req: TaskRequest):
    if req.user_id not in users_db:
        raise HTTPException(status_code=403, detail="Invalid user ID")
    result = run_task(req.user_id, req.user_query, users_db)
    return result
