from db import conn
import random
import string

class SessionRepository:
    def __init__(self):
        self.db = conn()

    def verficar_login(self, email, password):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ? AND senha = ?", (email, password))
        user = cursor.fetchone()

        if not user:
            return False

        return user

    def login(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT sessions.token, profiles.nome AS perfil FROM sessions INNER JOIN users ON sessions.user_id = users.id LEFT JOIN profiles ON users.profile_id = profiles.id WHERE sessions.id = ?", (user_id,))
        session = cursor.fetchone()

        if not session:
            letras = string.ascii_letters
            token = ''.join(random.choice(letras) for _ in range(15))
            cursor.execute("INSERT INTO sessions (user_id, token) VALUES (?, ?)", (user_id, token))
            self.db.commit()
            session_id = cursor.lastrowid
            cursor.execute("SELECT sessions.token, profiles.nome AS perfil FROM sessions INNER JOIN users ON sessions.user_id = users.id LEFT JOIN profiles ON users.profile_id = profiles.id WHERE sessions.id = ?", (session_id,))
            session = cursor.fetchone()
            print(session)

        return dict(session)
    
    def get_session(self, token):
        cursor = self.db.cursor()
        cursor.execute("SELECT sessions.id, sessions.token, users.id AS user_id, profiles.nome AS perfil FROM sessions INNER JOIN users ON sessions.user_id = users.id LEFT JOIN profiles ON users.profile_id = profiles.id WHERE sessions.token = ?", (token,))
        session = cursor.fetchone()

        if not session:
            return None

        return dict(session)

    def delete_session(self, session_id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM sessions WHERE id = ?", (session_id,))
        self.db.commit()