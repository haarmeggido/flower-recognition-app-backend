import sqlite3
from config import DATABASE

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT DEFAULT NULL,
            total_recognitions INTEGER DEFAULT 0,
            unique_recognitions INTEGER DEFAULT 0,
            flower_mask INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def get_db_connection():
    return sqlite3.connect(DATABASE)
