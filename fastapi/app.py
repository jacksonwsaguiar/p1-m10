from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

conn = sqlite3.connect('users.db',check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        password TEXT
    )
''')
conn.commit()

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

@app.post("/user/", response_model=User)
def create_user(user: User):
    cursor.execute('''
        INSERT INTO users (name, email, password)
        VALUES (?, ?, ?)
    ''', (user.name, user.email, user.password))
    conn.commit()
    user.id = cursor.lastrowid
    return user

@app.get("/user/")
def read_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return users

@app.put("/user/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    cursor.execute('''
        UPDATE users
        SET name = ?, email = ?, password = ?
        WHERE id = ?
    ''', (user.name, user.email, user.password, user_id))
    conn.commit()
    user.id = user_id
    return user

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    return {"message": "User deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
