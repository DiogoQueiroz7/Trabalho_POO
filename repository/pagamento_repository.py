from db import conn
from model.pagamento import Pagamento
from datetime import datetime

class PagamentoRepository:
    def salvar(self, pagamento: Pagamento):
        with conn() as banco:
            cursor = banco.cursor()
            sql = """
                INSERT INTO pagamentos
                    (valor, data, status, encomenda_id, forma_pagamento_id)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (
                pagamento.valor,
                datetime.now(),
                pagamento.status_pagamento,
                pagamento.encomenda_id,
                pagamento.forma_pagamento_id
            ))
            banco.commit()
            return cursor.lastrowid

    def listar(self):
        with conn() as banco:
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM pagamentos")
            return cursor.fetchall()