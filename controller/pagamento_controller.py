from repository.pagamento_repository import PagamentoRepository 
from repository.forma_pagamento_repository import FormaPagamentoRepository 
from model.pagamento import Pagamento 
from datetime import datetime

class PagamentoController:
    def __init__(self):
        self.__repositorio_pag = PagamentoRepository() 
        self.__repositorio_fp = FormaPagamentoRepository() 

    def criar_pagamento(self, valor: float, encomenda_id: int, forma_pagamento_id: int): 

        if not isinstance(valor, (float, int)) or valor <= 0:
            print("Erro: o Valor precisa ser maior que Zero.")
            return None
        if not isinstance(encomenda_id, int) or encomenda_id <= 0:
            print("Erro: O ID da encomenda é inválido.")
            return None
        if not isinstance(forma_pagamento_id, int) or forma_pagamento_id <= 0:
            print("Erro: O ID da forma de pagamento é inválido.")
            return None

        forma_pag_existente = self.__repositorio_fp.buscar_por_id(forma_pagamento_id) 
        if not forma_pag_existente:
            print(f"Erro: Forma de pagamento com ID {forma_pagamento_id} não encontrada. Não é possível criar o pagamento.")
            return None

        novo_pagamento = Pagamento( 
            valor=float(valor),
            encomenda_id=encomenda_id,
            forma_pagamento_id=forma_pagamento_id
        )

        id_salvo = self.__repositorio_pag.salvar(novo_pagamento) 
        if id_salvo:
            novo_pagamento.id_pagamento = id_salvo
            print(f"Pagamento (ID: {id_salvo}) de R${novo_pagamento.valor:.2f} criado com sucesso. Status: {novo_pagamento.status_pagamento}.")
            return novo_pagamento
        else:
            print("Erro: Não foi possível salvar o pagamento.")
            return None

    def listar_todos_os_pagamentos(self): 
        print("Buscando todos os pagamentos registrados...")
        pagamentos = self.__repositorio_pag.listar() 
        if not pagamentos:
            print("Nenhum pagamento encontrado.")
        return pagamentos

    def consultar_pagamento_por_id(self, id_pag: int): 
        if not isinstance(id_pag, int) or id_pag <= 0:
            print("Erro: ID do pagamento inválido.")
            return None

        print(f"Buscando pagamento com ID: {id_pag}...")
        pagamento = self.__repositorio_pag.buscar_por_id(id_pag) 
        if not pagamento:
            print(f"Pagamento com ID {id_pag} não encontrado.")
        return pagamento

    def _processar_mudanca_status(self, pagamento_id: int, acao: str) -> bool:
        pagamento_encontrado = self.__repositorio_pag.buscar_por_id(pagamento_id) 
        if not pagamento_encontrado:
            print(f"Erro ao tentar mudar status: Pagamento com ID {pagamento_id} não encontrado.")
            return False

        if pagamento_encontrado.id_pagamento is None:
           pagamento_encontrado.id_pagamento = pagamento_id

        sucesso_na_acao_modelo = False
        if acao == 'confirmar':
            sucesso_na_acao_modelo = pagamento_encontrado.confirmar_pagamento() 
        elif acao == 'cancelar':
            sucesso_na_acao_modelo = pagamento_encontrado.cancelar_pagamento() 
        elif acao == 'falhar':
            sucesso_na_acao_modelo = pagamento_encontrado.falhar_pagamento() 
        else:
            print(f"Erro interno: Ação de status '{acao}' desconhecida.")
            return False

        if sucesso_na_acao_modelo:
            sucesso_no_banco = self.__repositorio_pag.atualizar_status( 
                pagamento_id, pagamento_encontrado.status_pagamento
            )
            if sucesso_no_banco:
                return True
            else:
                print(f"Erro CRÍTICO: Status do Pagamento ID {pagamento_id} foi alterado, mas não conseguiu salvar no banco de dados!")
                return False
        else:
            return False

    def confirmar_pagamento(self, pagamento_id: int) -> bool:
        if not isinstance(pagamento_id, int) or pagamento_id <= 0:
            print("Erro: ID do pagamento para confirmação é inválido.")
            return False
        print(f"Tentando confirmar pagamento ID: {pagamento_id}...")
        return self._processar_mudanca_status(pagamento_id, 'confirmar')

    def cancelar_pagamento(self, pagamento_id: int) -> bool:
        if not isinstance(pagamento_id, int) or pagamento_id <= 0:
            print("Erro: ID do pagamento para cancelamento é inválido.")
            return False
        print(f"Tentando cancelar pagamento ID: {pagamento_id}...")
        return self._processar_mudanca_status(pagamento_id, 'cancelar')

    def marcar_pagamento_como_falho(self, pagamento_id: int) -> bool:
        if not isinstance(pagamento_id, int) or pagamento_id <= 0:
            print("Erro: ID do pagamento para marcar como falho é inválido.")
            return False
        print(f"Tentando marcar pagamento ID: {pagamento_id} como falho...")
        return self._processar_mudanca_status(pagamento_id, 'falhar')