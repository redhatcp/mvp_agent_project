from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.agents import schedule_agent
from backend.database import init_db

init_db()
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/api/run_agent")
def run_agent(name: str):
    task_id = schedule_agent(name)
    return {"task_id": task_id, "status": "scheduled"}

@app.get("/api/tasks")
def get_tasks():
    import sqlite3
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "status": r[2], "result": r[3]} for r in rows]