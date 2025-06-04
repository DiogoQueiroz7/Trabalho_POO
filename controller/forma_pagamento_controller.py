from repository.forma_pagamento_repository import FormaPagamentoRepository
from model.forma_pagamento import Pix, CartaoCredito, Boleto 

class FormaPagamentoController:
    def __init__(self):
        self.__repositorio_fp = FormaPagamentoRepository() 

    def criar_pix(self, chave_pix: str): 
        if not chave_pix or not isinstance(chave_pix, str):
            print("Erro: A chave PIX fornecida é inválida.")
            return None
        novo_pix = Pix(chave_pix=chave_pix) 
        self.__repositorio_fp.salvar(novo_pix)
        print(f"Forma de pagamento PIX cadastrada com sucesso!")

    def criar_cartao_credito(self, numero_cartao: str, nome_titular: str,
                             data_validade: str, codigo_seguranca: str): 
        novo_cartao = CartaoCredito( 
            numero_cartao=numero_cartao,
            nome_titular=nome_titular,
            data_validade=data_validade,
            codigo_seguranca=codigo_seguranca
        )
        self.__repositorio_fp.salvar(novo_cartao)
        print(f"Forma de pagamento Cartão de Crédito cadastrada com sucesso!")

    def get_forma_pagamento_by_id(self, forma_pagamento_id):
        return self.__repositorio_fp.get_by_id(forma_pagamento_id)
        
    def criar_boleto(self, codigo_barras: str): 
        novo_boleto = Boleto(codigo_barras=codigo_barras) 
        if not novo_boleto.codigo_barras: 
            print("Erro: Código de barras do boleto inválido. Não será salvo.")
            return None
        self.__repositorio_fp.salvar(novo_boleto)
        print(f"Forma de pagamento Boleto cadastrada com sucesso!")

    def listar_todas_formas_pagamento(self): 
        return self.__repositorio_fp.listar()