import sqlite3
import json
from datetime import datetime

db_name = "studyplanner.db"

def get_db():
    return sqlite3.connect(db_name)

def init_db():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS plans ( id INTEGER PRIMARY KEY AUTOINCREMENT, created TEXT, free_time TEXT, lessons TEXT)")

    db.commit()
    db.close()

def save_plan(free_time, lessons):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("INSERT INTO plans (created, free_time, lessons) VALUES (?, ?, ?)",(datetime.now().isoformat(), free_time, json.dumps(lessons)))


    db.commit()
    db.close()

def get_recent_plans(limit=5):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT id, created, free_time, lessons FROM plans ORDER BY id DESC LIMIT ?", (limit,))

    rows = cursor.fetchall()
    db.close()

    return rows
