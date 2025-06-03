from db import conn
from model.transportadora import Transportadora

class TransportadoraRepository:
    def __init__(self):
        self.db = conn()  # chama a função para obter a conexão

    def create(self, transportadora):
        transportadora_data = {
            "razao_social": transportadora.razao_social,
            "cnpj": transportadora.cnpj,
            "endereco": transportadora.endereco
        }
        cursor = self.db.cursor() 
        cursor.execute("""
            INSERT INTO transportadoras (razao_social, cnpj, endereco)
            VALUES (:razao_social, :cnpj, :endereco)
        """, transportadora_data)
        self.db.commit()
        return transportadora

    def get_all(self):
        cursor = self.db.cursor() 
        cursor.execute("SELECT * FROM transportadoras")
        rows = cursor.fetchall()
        return rows
