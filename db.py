import sqlite3, pathlib

_database = pathlib.Path("speedbox.db")


def conn():
    conexao = sqlite3.connect(_database)
    conexao.row_factory = sqlite3.Row

    return conexao

def init():
    with conn() as c:
        c.executescript("""
            PRAGMA foreign_keys = ON;

            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                senha TEXT NOT NULL,
                profile_id INTEGER NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (profile_id) REFERENCES profiles (id)
            );

            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                endereco TEXT NOT NULL,
                cpf TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            );

            CREATE TABLE IF NOT EXISTS administradores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nivel_acesso TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            );

            CREATE TABLE IF NOT EXISTS tipos_veiculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
                        
            CREATE TABLE IF NOT EXISTS moto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                adequecaoUrbana TEXT NOT NULL,
                agilidade INT NOT NULL,
                cilindrada INT NOT NULL,
                capacidadeCarga FLOAT NOT NULL,
                tipo_veiculo_id INTEGER NOT NULL,
                FOREIGN KEY (tipo_veiculo_id) REFERENCES tipos_veiculos (id)
            );
                        
            CREATE TABLE IF NOT EXISTS carro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                adequecaoUrbana INTEGER NOT NULL,
                agilidade INT NOT NULL,
                modelo TEXT NOT NULL,
                capacidadeCarga FLOAT NOT NULL,
                tipo_veiculo_id INTEGER NOT NULL,
                FOREIGN KEY (tipo_veiculo_id) REFERENCES tipos_veiculos (id)
            );

            CREATE TABLE IF NOT EXISTS veiculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                placa TEXT NOT NULL,
                cor TEXT NOT NULL,
                tipo_veiculo_id INTEGER NOT NULL,
                cliente_id INTEGER NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (tipo_veiculo_id) REFERENCES tipos_veiculos (id),
                FOREIGN KEY (cliente_id) REFERENCES clientes (id)
            );

            CREATE TABLE IF NOT EXISTS transportadoras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                razao_social TEXT NOT NULL,
                cnpj TEXT NOT NULL,
                endereco TEXT NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS transportadoras_veiculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                transportadora_id INTEGER NOT NULL,
                veiculo_id INTEGER NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (transportadora_id) REFERENCES transportadoras (id),
                FOREIGN KEY (veiculo_id) REFERENCES veiculos (id)
            );

            CREATE TABLE IF NOT EXISTS encomendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                peso REAL NOT NULL,
                volume REAL NOT NULL,
                cliente_id INTEGER NOT NULL,
                transportadora_id INTEGER NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (cliente_id) REFERENCES clientes (id),
                FOREIGN KEY (transportadora_id) REFERENCES transportadoras (id)
            );

            CREATE TABLE IF NOT EXISTS forma_pagamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                valor TEXT NOT NULL,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS pagamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor REAL NOT NULL,
                data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT NOT NULL,
                encomenda_id INTEGER NOT NULL,
                forma_pagamento_id INTEGER NOT NULL,
                FOREIGN KEY (forma_pagamento_id) REFERENCES forma_pagamento (id),
                FOREIGN KEY (encomenda_id) REFERENCES encomendas (id)
            );

            CREATE TABLE IF NOT EXISTS veiculos_movimentacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                veiculo_id INTEGER NOT NULL,
                data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                localizacao TEXT NOT NULL,
                status INTEGER NOT NULL,
                cliente_id INTEGER NOT NULL,
                transportadora_id INTEGER NOT NULL,
                FOREIGN KEY (veiculo_id) REFERENCES veiculos (id),
                FOREIGN KEY (cliente_id) REFERENCES clientes (id),
                FOREIGN KEY (transportadora_id) REFERENCES transportadoras (id)
            );
        """)
