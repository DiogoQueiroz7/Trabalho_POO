from db import conn
from model.pagamento import Pagamento 
from datetime import datetime

class PagamentoRepository:
    def salvar(self, pagamento: Pagamento): 
        banco = conn()
        cursor = banco.cursor()

        data_pagamento_obj = pagamento.data_pagamento 

        if isinstance(data_pagamento_obj, str):
            print(f"Alerta: data_pagamento_obj é uma string ('{data_pagamento_obj}') no repositório. Espera-se datetime.")
            data_pagamento_obj = datetime.now() 
        elif not isinstance(data_pagamento_obj, datetime):
            print(f"Alerta: data_pagamento com tipo inesperado ('{type(data_pagamento_obj)}'). Usando data atual para o repositório.")
            data_pagamento_obj = datetime.now()
        
        data_pagamento_str = data_pagamento_obj.isoformat()

        sql = """
            INSERT INTO pagamentos
                (valor, data, status, encomenda_id, forma_pagamento_id)
            VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (
            pagamento.valor, 
            data_pagamento_str,
            pagamento.status_pagamento, 
            pagamento.encomenda_id, 
            pagamento.forma_pagamento_id 
        ))
        banco.commit()
        id_gerado = cursor.lastrowid
        pagamento.id_pagamento = id_gerado 
        
        banco.close() 
        return id_gerado

    def listar(self): 
        banco = conn()
        cursor = banco.cursor()
        lista_de_pagamentos = []

        cursor.execute("SELECT * FROM pagamentos")
        registros = cursor.fetchall()

        for registro in registros:
            data_pag_str = registro["data"]
            data_pag = datetime.fromisoformat(data_pag_str) if data_pag_str else datetime.now()

            pagamento_obj = Pagamento( 
                id_pagamento=registro["id"],
                valor=registro["valor"],
                data_pagamento=data_pag,
                status=registro["status"],
                encomenda_id=registro["encomenda_id"],
                forma_pagamento_id=registro["forma_pagamento_id"]
            )
            lista_de_pagamentos.append(pagamento_obj)

        banco.close() 
        return lista_de_pagamentos

    def buscar_por_id(self, id_para_buscar: int): 
        banco = conn()
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM pagamentos WHERE id = ?", (id_para_buscar,))
        registro = cursor.fetchone()

        pagamento_encontrado = None
        if registro:
            data_pag_str = registro["data"]
            data_pag = datetime.fromisoformat(data_pag_str) if data_pag_str else datetime.now()

            pagamento_encontrado = Pagamento( 
                id_pagamento=registro["id"],
                valor=registro["valor"],
                data_pagamento=data_pag,
                status=registro["status"],
                encomenda_id=registro["encomenda_id"],
                forma_pagamento_id=registro["forma_pagamento_id"]
            )
        
        banco.close() 
        return pagamento_encontrado

    def atualizar_status(self, pagamento_id: int, novo_status: str) -> bool: 
        if novo_status not in [Pagamento.STATUS_PENDENTE, Pagamento.STATUS_CONFIRMADO, Pagamento.STATUS_CANCELADO, Pagamento.STATUS_FALHOU]: #
            print(f"Erro: O status '{novo_status}' não é válido.")
            return False

        banco = conn()
        cursor = banco.cursor()

        sql = "UPDATE pagamentos SET status = ? WHERE id = ?"
        cursor.execute(sql, (novo_status, pagamento_id))
        banco.commit()

        sucesso = False
        if cursor.rowcount > 0:
            sucesso = True
        
        banco.close() 
        return sucesso