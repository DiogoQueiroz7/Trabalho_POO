from db import conn

class MovimentacaoRepository:
    def registrar(self, movimentacao):
        with conn() as c:
            cursor = c.cursor()
            cursor.execute("""
                INSERT INTO veiculos_movimentacao (veiculo_id, data_hora, localizacao, status, cliente_id, transportadora_id)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                movimentacao.veiculo_id,
                movimentacao.datahora,
                movimentacao.localizacao,
                movimentacao.status,
                movimentacao.cliente_id,
                movimentacao.transportadora_id
            ))
            movimentacao.id = cursor.lastrowid
        return movimentacao.id

    def listar_por_veiculo(self, veiculo_id):
        with conn() as c:
            cursor = c.cursor()
            cursor.execute("""
                SELECT * FROM veiculos_movimentacao WHERE veiculo_id = ? ORDER BY data_hora DESC
            """, (veiculo_id,))
            return cursor.fetchall()