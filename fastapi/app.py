from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Criar a conexão com o banco de dados SQLite
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Criar a tabela 'users' se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')
conn.commit()

# Definindo a estrutura dos dados do usuário usando Pydantic
class User(BaseModel):
    id: int
    name: str
    email: str

# Rota para criar um novo usuário
@app.post("/users/", response_model=User)
def create_user(user: User):
    cursor.execute('''
        INSERT INTO users (name, email)
        VALUES (?, ?)
    ''', (user.name, user.email))
    conn.commit()
    user.id = cursor.lastrowid
    return user

# Rota para obter todos os usuários
@app.get("/users/", response_model=list[User])
def read_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    return users

# Rota para obter um usuário específico por ID
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Rota para atualizar um usuário por ID
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    cursor.execute('''
        UPDATE users
        SET name = ?, email = ?
        WHERE id = ?
    ''', (user.name, user.email, user_id))
    conn.commit()
    user.id = user_id
    return user

# Rota para deletar um usuário por ID
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    return {"message": "User deleted successfully"}

# Para rodar o servidor usando uvicorn
# Execute este arquivo com o comando: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
