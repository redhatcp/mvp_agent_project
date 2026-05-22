import sqlite3

DB_FILE = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            status TEXT,
            result TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_task(name, status="pending", result=""):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (name, status, result) VALUES (?, ?, ?)", (name, status, result))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

def update_task(task_id, status, result=""):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status=?, result=? WHERE id=?", (status, result, task_id))
    conn.commit()
    conn.close()