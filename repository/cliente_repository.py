from db import conn
from model.cliente import Cliente

class ClienteRepository:
    def salvar(self, cliente):
        with conn() as c:
            cursor = c.cursor() 

            verifica_profile = cursor.execute(
                "SELECT * FROM profiles WHERE nome = ?", ("cliente",)
            ).fetchone()

            if not verifica_profile:
                cursor.execute(
                    "INSERT INTO profiles (nome) VALUES (?)",
                    ("cliente",)
                )
                profile_id = cursor.lastrowid
            else:
                profile_id = verifica_profile["id"]

            cursor.execute(
                "INSERT INTO users (nome, email, senha, profile_id) VALUES (?, ?, ?, ?)",
                (cliente.nome, cliente.email, cliente.senha, profile_id)
            )
            user_id = cursor.lastrowid

            cursor.execute(
                "INSERT INTO clientes (endereco, cpf, user_id) VALUES (?, ?, ?)",
                (cliente.endereco, cliente.cpf, user_id)
            )

        
            c.commit()

    def buscar_por_user_id(self, user_id):
        with conn() as c:
            cursor = c.cursor()
            cursor.execute(
                "SELECT clientes.id, clientes.endereco, clientes.cpf, clientes.user_id, users.nome, users.email, users.senha "
                "FROM clientes INNER JOIN users ON clientes.user_id = users.id WHERE users.id = ?",
                (user_id,)
            )
            row = cursor.fetchone()

            if row:
                return {
                    "id": row["id"],
                    "nome": row["nome"],
                    "email": row["email"],
                    "senha": row["senha"],
                    "cpf": row["cpf"],
                    "endereco": row["endereco"],
                    "user_id": row["user_id"]
                }
            return None

    def listar(self):
        with conn() as c:
            cursor = c.cursor()
            cursor.execute(
                "SELECT * FROM clientes INNER JOIN users ON clientes.user_id = users.id"
            )
            rows = cursor.fetchall()

            clientes = []
            for row in rows:
                cliente = Cliente(
                    row["id"],
                    row["nome"],
                    row["email"],
                    row["senha"],
                    row["cpf"],
                    row["endereco"],
                    row["user_id"]
                )
                clientes.append(cliente)

            return clientes
