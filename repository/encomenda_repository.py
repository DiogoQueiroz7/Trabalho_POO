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
        return [Encomenda(**row) for row in rows]
