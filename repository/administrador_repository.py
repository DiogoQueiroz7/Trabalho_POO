from db import conn
from model.administrador import Administrador

class AdministradorRepository:
    def salvar(self, administrador):
        with conn() as c:
            cursor = c.cursor()

            verifica_profile = cursor.execute(
                "SELECT * FROM profiles WHERE nome = ?", ("administrador",)
            ).fetchone()

            if not verifica_profile:
                cursor.execute(
                    "INSERT INTO profiles (nome) VALUES (?)",
                    ("administrador",)
                )
                profile_id = cursor.lastrowid
            else:
                profile_id = verifica_profile["id"]

            cursor.execute(
                "INSERT INTO users (nome, email, senha, profile_id) VALUES (?, ?, ?, ?)",
                (administrador.nome, administrador.email, administrador.senha, profile_id)
            )
            user_id = cursor.lastrowid

            cursor.execute(
                "INSERT INTO administradores (nivel_acesso, user_id) VALUES (?, ?)",
                (administrador.get_nivel_acesso, user_id)
            )

            c.commit()

    def listar(self):
        with conn() as c:
            cursor = c.cursor()
            cursor.execute(
                "SELECT * FROM administradores INNER JOIN users ON administradores.user_id = users.id"
            )
            rows = cursor.fetchall()

            administradores = []
            for row in rows:
                administrador = Administrador(
                    row["id"],
                    row["nome"],
                    row["email"],
                    row["senha"]
                )
                administradores.append(administrador)

            return administradores