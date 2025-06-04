from db import conn
from model.encomenda import Encomenda

class EncomendaRepository:
    def __init__(self):
        self.db = conn()  # Aqui estamos chamando a função para obter a conexão

    def create(self, encomenda):
        encomenda_data = {
            "descricao": encomenda.descricao,
            "peso": encomenda.peso,
            "volume": encomenda.volume,
            "cliente_id": encomenda.cliente_id,
            "transportadora_id": encomenda.transportadora_id
        }
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO encomendas (descricao, peso, volume, cliente_id, transportadora_id)
            VALUES (:descricao, :peso, :volume, :cliente_id, :transportadora_id)
        """, encomenda_data)
        self.db.commit()  # importante para salvar as alterações
        return encomenda

    def get_all(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM encomendas")
        rows = cursor.fetchall()
        return rows
    
    def get_by_id(self, encomenda_id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM encomendas WHERE id = ?", (encomenda_id,))
        row = cursor.fetchone() 
        return row
    
    def get_all_cliente(self, user_id):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT encomendas.id, encomendas.descricao, encomendas.peso, encomendas.volume, 
                transportadoras.razao_social AS transportadora 
            FROM encomendas 
            INNER JOIN clientes ON clientes.id = encomendas.cliente_id 
            INNER JOIN users ON users.id = clientes.user_id 
            LEFT JOIN transportadoras ON transportadoras.id = encomendas.transportadora_id 
            WHERE users.id = ?
        """, (user_id,))
        rows = cursor.fetchall()
        return rows

