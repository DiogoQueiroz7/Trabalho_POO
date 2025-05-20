from db import conn
from model.pagamento import Pagamento #
from datetime import datetime

class PagamentoRepository:
    def salvar(self, pagamento: Pagamento) -> int | None: #
        """
        Salva um novo pagamento no banco de dados.
        Retorna o ID se salvar, ou None se der erro.
        """
        banco = conn()
        cursor = banco.cursor()

        try:
            data_pagamento_obj = pagamento.data_pagamento #
            if isinstance(data_pagamento_obj, str):
                try:
                    data_pagamento_obj = datetime.fromisoformat(data_pagamento_obj)
                except ValueError:
                    print(f"Alerta: Formato de data_pagamento string inválido ('{data_pagamento_obj}'). Usando data atual para o repositório.")
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
            pagamento.id_pagamento = id_gerado #
            return id_gerado
        except Exception as e:
            print(f"Ops! Algum erro ocorreu ao salvar o pagamento: {e}")
            banco.rollback()
            return None
        finally:
            banco.close()

    def listar(self) -> list[Pagamento]: #
        """
        Pega todos os pagamentos do banco.
        """
        banco = conn()
        cursor = banco.cursor()
        lista_de_pagamentos = []

        try:
            cursor.execute("SELECT * FROM pagamentos")
            registros = cursor.fetchall()

            for registro in registros:
                data_pag_str = registro["data"]
                data_pag = datetime.fromisoformat(data_pag_str) if data_pag_str else datetime.now()

                pagamento_obj = Pagamento( #
                    id_pagamento=registro["id"],
                    valor=registro["valor"],
                    data_pagamento=data_pag,
                    status=registro["status"],
                    encomenda_id=registro["encomenda_id"],
                    forma_pagamento_id=registro["forma_pagamento_id"]
                )
                lista_de_pagamentos.append(pagamento_obj)

            return lista_de_pagamentos
        except Exception as e:
            print(f"Ops! Algum erro ocorreu ao listar os pagamentos: {e}")
            return []
        finally:
            banco.close()

    def buscar_por_id(self, id_para_buscar: int) -> Pagamento | None: #
        """
        Busca um pagamento específico pelo seu ID.
        """
        banco = conn()
        cursor = banco.cursor()

        try:
            cursor.execute("SELECT * FROM pagamentos WHERE id = ?", (id_para_buscar,))
            registro = cursor.fetchone()

            if registro:
                data_pag_str = registro["data"]
                data_pag = datetime.fromisoformat(data_pag_str) if data_pag_str else datetime.now()

                return Pagamento( #
                    id_pagamento=registro["id"],
                    valor=registro["valor"],
                    data_pagamento=data_pag,
                    status=registro["status"],
                    encomenda_id=registro["encomenda_id"],
                    forma_pagamento_id=registro["forma_pagamento_id"]
                )
            else:
                return None 
        except Exception as e:
            print(f"Ops! Algum erro ocorreu ao buscar o pagamento: {e}")
            return None
        finally:
            banco.close()

    def atualizar_status(self, pagamento_id: int, novo_status: str) -> bool:
        """
        Muda o status de um pagamento no banco.
        Retorna True se conseguiu, False se não.
        """
        if novo_status not in [Pagamento.STATUS_PENDENTE, Pagamento.STATUS_CONFIRMADO, Pagamento.STATUS_CANCELADO, Pagamento.STATUS_FALHOU]: #
            print(f"Erro: O status '{novo_status}' não é válido.")
            return False

        banco = conn()
        cursor = banco.cursor()
        try:
            sql = "UPDATE pagamentos SET status = ? WHERE id = ?"
            cursor.execute(sql, (novo_status, pagamento_id))
            banco.commit()

            
            if cursor.rowcount > 0:
                return True 
            else:
                return False 
        except Exception as e:
            print(f"Ops! Algum erro ocorreu ao atualizar o status do pagamento ID {pagamento_id}: {e}")
            banco.rollback()
            return False
        finally:
            banco.close()