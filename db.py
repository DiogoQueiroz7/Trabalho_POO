import sqlite3, pathlib

_database = pathlib.Path("speedbox.db")


def conn():
    conexao = sqlite3.connect(_database)
    conexao.row_factory = sqlite3.Row

    return conexao

def init():
    with conn() as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )

            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL,
                profile_id INTEGER NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                FOREIGN KEY (profile_id) REFERENCES profiles (id)
            )

            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                endereco TEXT NOT NULL,
                cpf TEXT NOT NULL
                user_id INTEGER NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )

            CREATE TABLE IF NOT EXISTS administradores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nivel_acesso TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )

            CREATE TABLE IF NOT EXISTS tipos_veiculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )

            CREATE TABLE IF NOT EXISTS veiculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                placa TEXT NOT NULL,
                cor TEXT NOT NULL,
                tipo_veiculo_id INTEGER NOT NULL,
                cliente_id INTEGER NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (tipo_veiculo_id) REFERENCES tipos_veiculos (id),
                FOREIGN KEY (cliente_id) REFERENCES clientes (id)
            )
            """
        )