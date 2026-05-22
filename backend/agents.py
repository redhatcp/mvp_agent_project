from backend.tasks import run_agent_task
from backend.database import insert_task

def schedule_agent(agent_name: str):
    task_id = insert_task(agent_name)
    run_agent_task.delay(task_id, agent_name)
    return task_id