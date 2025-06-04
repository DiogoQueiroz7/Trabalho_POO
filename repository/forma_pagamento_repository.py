from db import conn
from model.forma_pagamento import FormaPagamento, Pix, CartaoCredito, Boleto
from datetime import datetime

class FormaPagamentoRepository:
    def salvar(self, forma_pagamento: FormaPagamento):
        with conn() as banco:
            cursor = banco.cursor()
            detalhes = forma_pagamento.obter_detalhes_para_salvar()
            chave_pix = detalhes.get("chave_pix")
            ultimos_digitos = detalhes.get("ultimos_digitos")
            nome_titular = detalhes.get("nome_titular")
            data_validade = detalhes.get("data_validade_cartao")
            codigo_barras = detalhes.get("codigo_barras")

            sql = """
                INSERT INTO forma_pagamento
                    (tipo, data_cadastro, chave_pix, ultimos_digitos_cartao,
                     nome_titular_cartao, data_validade_cartao, codigo_barras_boleto)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(sql, (
                forma_pagamento.tipo, datetime.now(), chave_pix, ultimos_digitos,
                nome_titular, data_validade, codigo_barras
            ))
            banco.commit()
            return cursor.lastrowid
        
    def get_by_id(self, forma_pagamento_id):
        with conn() as banco: 
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM forma_pagamento WHERE id = ?", (forma_pagamento_id,))
            row = cursor.fetchone() 
            return row

    def listar(self):
        with conn() as banco:
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM forma_pagamento")
            return cursor.fetchall()