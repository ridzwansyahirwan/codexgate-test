
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tasks = [
    {"id": 1, "title": "Practise FastAPI", "completed": False},
    {"id": 2, "title": "Practise Next.js", "completed": False},
]


class TaskCreate(BaseModel):
    title: str


@app.get("/")
def home():
    return {"message": "CodeXGate setup ready"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    title = task.title.strip()

    if not title:
        raise HTTPException(
            status_code=400,
            detail="Task title cannot be empty",
        )

    new_task = {
        "id": max((t["id"] for t in tasks), default=0) + 1,
        "title": title,
        "completed": False,
    }

    tasks.append(new_task)
    return new_task

@app.delete("/tasks/{task_id}", status_code=200)
def delete_task(task_id: int):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    tasks.remove(task)
    return {"message": "Task deleted successfully"}