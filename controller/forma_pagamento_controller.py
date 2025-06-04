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

        if not numero_cartao or not numero_cartao.isdigit() or not (13 <= len(numero_cartao) <= 19):
            print("Erro: Número do Cartão inválido. Deve conter apenas números e ter entre 13 e 19 dígitos.")
            return
        
        if not nome_titular or not isinstance(nome_titular, str) or len(nome_titular.strip()) < 3 :
            print("Erro: Nome do Titular inválido. Deve ser preenchido.")
            return

        if not (len(data_validade) == 5 and 
                data_validade[2] == '/' and 
                data_validade[0:2].isdigit() and 
                data_validade[3:5].isdigit()):
            print("Erro: Data de Validade inválida. Use o formato MM/AA e certifique-se de que mês e ano são numéricos (ex: 12/25).")
            return

        mes = int(data_validade[0:2])

        if not (1 <= mes <= 12):
                print("Erro: Mês na Data de Validade inválido. Deve ser entre 01 e 12.")
                return
        
        if not codigo_seguranca or not codigo_seguranca.isdigit() or not (3 <= len(codigo_seguranca) <= 4):
            print("Erro: CVV inválido. Deve conter apenas números e ter 3 ou 4 dígitos.")
            return

        novo_cartao = CartaoCredito( 
            numero_cartao=numero_cartao,
            nome_titular=nome_titular.strip(), 
            data_validade=data_validade,
            codigo_seguranca=codigo_seguranca
        )
        self.__repositorio_fp.salvar(novo_cartao)
        print(f"Forma de pagamento Cartão de Crédito cadastrada com sucesso!")

    def get_forma_pagamento_by_id(self, forma_pagamento_id):
        return self.__repositorio_fp.get_by_id(forma_pagamento_id)
        
    def criar_boleto(self, codigo_barras: str): 
        novo_boleto = Boleto(codigo_barras=codigo_barras) 
        self.__repositorio_fp.salvar(novo_boleto)
        print(f"Forma de pagamento Boleto cadastrada com sucesso!")

    def listar_todas_formas_pagamento(self): 
        return self.__repositorio_fp.listar()