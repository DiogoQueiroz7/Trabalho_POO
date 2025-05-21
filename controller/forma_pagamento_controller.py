from repository.forma_pagamento_repository import FormaPagamentoRepository
from model.forma_pagamento import FormaPagamento, Pix, CartaoCredito, Boleto 
from datetime import datetime

class FormaPagamentoController:
    def __init__(self):
        self.__repositorio_fp = FormaPagamentoRepository() 

    def criar_pix(self, chave_pix: str): 
        """
        Cria um objeto Pix e tenta salvá-lo usando o repositório.
        Retorna o objeto Pix se bem-sucedido, None caso contrário.
        """
        if not chave_pix or not isinstance(chave_pix, str):
            print("Erro: A chave PIX fornecida é inválida.")
            return None

        novo_pix = Pix(chave_pix=chave_pix) 

        id_salvo = self.__repositorio_fp.salvar(novo_pix) 
        if id_salvo:
            novo_pix.id_forma_pagamento = id_salvo
            print(f"Forma de pagamento PIX (ID: {id_salvo}) cadastrada com sucesso!")
            return novo_pix
        else:
            print("Erro: Não foi possível salvar a forma de pagamento PIX.")
            return None

    def criar_cartao_credito(self, numero_cartao: str, nome_titular: str,
                             data_validade: str, codigo_seguranca: str): 

        novo_cartao = CartaoCredito( 
            numero_cartao=numero_cartao,
            nome_titular=nome_titular,
            data_validade=data_validade,
            codigo_seguranca=codigo_seguranca
        )

        if not novo_cartao.ultimos_digitos or not novo_cartao.nome_titular or not novo_cartao.data_validade:
            print("Erro: Dados obrigatórios do cartão de crédito parecem inválidos ou incompletos. Não será salvo.")
            return None

        id_salvo = self.__repositorio_fp.salvar(novo_cartao) 
        if id_salvo:
            novo_cartao.id_forma_pagamento = id_salvo
            print(f"Forma de pagamento Cartão de Crédito (ID: {id_salvo}) cadastrada com sucesso!")
            return novo_cartao
        else:
            print("Erro: Não foi possível salvar a forma de pagamento Cartão de Crédito.")
            return None
        
    def criar_boleto(self, codigo_barras: str): 
        """
        Cria um objeto Boleto e tenta salvá-lo.
        Retorna o objeto Boleto se bem-sucedido, None caso contrário.
        """
        novo_boleto = Boleto(codigo_barras=codigo_barras) 

        if not novo_boleto.codigo_barras: 
            print("Erro: Código de barras do boleto inválido. Não será salvo.")
            return None

        id_salvo = self.__repositorio_fp.salvar(novo_boleto) 
        if id_salvo:
            novo_boleto.id_forma_pagamento = id_salvo
            print(f"Forma de pagamento Boleto (ID: {id_salvo}) cadastrada com sucesso!")
            return novo_boleto
        else:
            print("Erro: Não foi possível salvar a forma de pagamento Boleto.")
            return None

    def listar_todas_formas_pagamento(self): 
        print("Buscando todas as formas de pagamento...")
        formas_pagamento = self.__repositorio_fp.listar() 
        if not formas_pagamento:
            print("Nenhuma forma de pagamento encontrada.")
        return formas_pagamento

    def buscar_forma_pagamento_por_id(self, id_fp: int):
        if not isinstance(id_fp, int) or id_fp <= 0:
            print("Erro: ID da forma de pagamento inválido.")
            return None

        print(f"Buscando forma de pagamento com ID: {id_fp}...")
        forma_pagamento = self.__repositorio_fp.buscar_por_id(id_fp) 
        if not forma_pagamento:
            print(f"Forma de pagamento com ID {id_fp} não encontrada.")
        return forma_pagamento