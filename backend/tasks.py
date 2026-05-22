from celery import Celery
from backend.database import update_task
from backend.notifications import send_feishu_message

celery_app = Celery("tasks", broker="redis://redis:6379/0")

@celery_app.task
def run_agent_task(task_id, agent_name):
    import time, random
    update_task(task_id, "running")
    time.sleep(random.randint(1,3))
    result = f"{agent_name} completed successfully"
    update_task(task_id, "done", result)
    send_feishu_message(f"任务完成: {agent_name}, ID: {task_id}")
    return result