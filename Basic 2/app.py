from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import uuid
import os
import sqlite3
from contextlib import closing
from pathlib import Path

# PostgreSQL
import psycopg

# Définition des chemins / URL
DB_PATH = Path(os.getenv("TODO_DB_PATH", "data/todo.db"))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
DB_URL = os.getenv("TODO_DB_URL")
USE_POSTGRES = bool(DB_URL)

# --- SQLite ---
def init_sqlite():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS todos (id TEXT PRIMARY KEY, title TEXT, done INTEGER)"
        )
        conn.commit()

def all_todos_sqlite() -> Dict[str, Dict[str, str]]:
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM todos").fetchall()
        return {row["id"]: {"title": row["title"], "done": bool(row["done"])} for row in rows}

def add_todo_sqlite(title: str) -> str:
    todo_id = str(uuid.uuid4())
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.execute(
            "INSERT INTO todos (id, title, done) VALUES (?, ?, ?)", (todo_id, title, 0)
        )
        conn.commit()
    return todo_id

def mark_done_sqlite(todo_id: str):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.execute("UPDATE todos SET done = 1 WHERE id = ?", (todo_id,))
        conn.commit()

# --- PostgreSQL ---
def init_pg():
    with psycopg.connect(DB_URL, autocommit=True) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS todos (id TEXT PRIMARY KEY, title TEXT, done BOOLEAN)"
        )

def all_todos_pg() -> Dict[str, Dict[str, str]]:
    with psycopg.connect(DB_URL, autocommit=True) as conn:
        rows = conn.execute("SELECT * FROM todos").fetchall()
        return {row[0]: {"title": row[1], "done": row[2]} for row in rows}

def add_todo_pg(title: str) -> str:
    todo_id = str(uuid.uuid4())
    with psycopg.connect(DB_URL, autocommit=True) as conn:
        conn.execute(
            "INSERT INTO todos (id, title, done) VALUES (%s, %s, %s)", (todo_id, title, False)
        )
    return todo_id

def mark_done_pg(todo_id: str):
    with psycopg.connect(DB_URL, autocommit=True) as conn:
        conn.execute("UPDATE todos SET done = TRUE WHERE id = %s", (todo_id,))

# Initialisation de la base
if USE_POSTGRES:
    init_pg()
else:
    init_sqlite()

# Création de l’application FastAPI
app = FastAPI(title="Todo API")

# Modèle de données pour POST
class TodoIn(BaseModel):
    title: str

# Endpoint healthcheck
@app.get("/health")
def healthcheck():
    return {"status": "ok"}

# Lister tous les todos
@app.get("/todos")
def list_todos():
    return all_todos_pg() if USE_POSTGRES else all_todos_sqlite()

# Créer un todo
@app.post("/todos")
def create(todo: TodoIn):
    todo_id = add_todo_pg(todo.title) if USE_POSTGRES else add_todo_sqlite(todo.title)
    return {"id": todo_id, "title": todo.title, "done": False}

# Marquer un todo comme fait
@app.post("/todos/{todo_id}/done")
def complete(todo_id: str):
    mark_done_pg(todo_id) if USE_POSTGRES else mark_done_sqlite(todo_id)
    return {"id": todo_id, "done": True}
