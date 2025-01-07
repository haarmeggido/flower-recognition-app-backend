import sqlite3
from models.database import get_db_connection



def add_user(username, hashed_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True

def get_user_password(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result

def get_user_full(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    if not user:
        return None
    return {
        "username": user[1],
        "email": user[3],
        "total_recognitions": user[4],
        "unique_recognitions": user[5],
        "flower_mask": user[6],
    }

def get_user_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    result = conn.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
    ).fetchone()
    if result:
        return {
            "id": result[0],
            "username": result[1],
            "password": result[2],
            "email": result[3],
            "total_recognitions": result[4],
            "unique_recognitions": result[5],
            "flower_mask": result[6],
        }
    return None


def update_user(username, email, total_recognitions, unique_recognitions, flower_mask):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE users
        SET email = ?, total_recognitions = ?, unique_recognitions = ?, flower_mask = ?
        WHERE username = ?
    """, (email, total_recognitions, unique_recognitions, flower_mask, username))
    conn.commit()
    conn.close()
