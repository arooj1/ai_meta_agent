from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from src.auth import authenticate_user, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.main import run_task

app = FastAPI(title="AI Meta-Agent API")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users_db = {
    "user123": {
        "username": "user123",
        "name": "Arooj",
        "role": "student",
        "password": "test",
        "capabilities": ["summarizer", "deadline_extractor"]
    },
    "admin001": {
        "username": "admin001",
        "name": "Super Admin",
        "role": "admin",
        "password": "admin",
        "capabilities": ["*"]
    }
}

class TaskRequest(BaseModel):
    user_query: str

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/run-task")
async def handle_task(req: TaskRequest, current_user: dict = Depends(get_current_user)):
    return run_task(current_user["username"], req.user_query, users_db)