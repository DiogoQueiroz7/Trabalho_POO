class FormaPagamento: 
    def processar_pagamento(self, valor: float) -> bool:

        raise NotImplementedError("A subclasse deve implementar o método 'processar_pagamento'")

    def __str__(self) -> str:
        return self.__class__.__name__

class Pix(FormaPagamento):

    def __init__(self, chave_pix: str):
        if not chave_pix or not isinstance(chave_pix, str):
            print("Erro: Chave PIX inválida ou não fornecida. Usando chave vazia.")
            self.chave_pix: str = ""
        else:
            self.chave_pix: str = chave_pix

    def processar_pagamento(self, valor: float) -> bool:
        print(f"Iniciando processamento PIX de R${valor:.2f} para a chave '{self.chave_pix}'...")
        if not self.chave_pix:
            print("Falha no processamento PIX: Chave PIX não definida ou inválida.")
            return False
        
        print(f"Pagamento PIX de R${valor:.2f} para '{self.chave_pix}' processado com sucesso.")
        return True

class CartaoCredito(FormaPagamento):

    def __init__(self, numero_cartao: str, nome_titular: str, data_validade: str, codigo_seguranca: str):
        data_de_validadse = True
        if not isinstance(numero_cartao, str) or len(numero_cartao) < 13 or len(numero_cartao) > 19:
            print(f"Erro: Número do cartão inválido ('{numero_cartao}').")
            data_de_validadse = False
        if not isinstance(nome_titular, str) or not nome_titular.strip():
            print(f"Erro: Nome do titular inválido ('{nome_titular}').")
            data_de_validadse = False
        if not isinstance(data_validade, str) or len(data_validade) != 5 or data_validade[2] != '/':
            print(f"Erro: Data de validade inválida ('{data_validade}'). Use o formato MM/YY.")
            data_de_validadse = False
        if not isinstance(codigo_seguranca, str) or not (len(codigo_seguranca) == 3 or len(codigo_seguranca) == 4):
            print(f"Erro: Código de segurança (CVV) inválido ('{codigo_seguranca}').")
            data_de_validadse = False

        if data_de_validadse:
            self.numero_cartao: str = numero_cartao
            self.nome_titular: str = nome_titular
            self.data_validade: str = data_validade
            self.codigo_seguranca: str = codigo_seguranca
        else:
            print("Erro: Dados do cartão de crédito inválidos. O processamento pode falhar.")
            self.numero_cartao: str = ""
            self.nome_titular: str = ""
            self.data_validade: str = ""
            self.codigo_seguranca: str = ""

    def processar_pagamento(self, valor: float) -> bool:
        numero_cartao_display = self.numero_cartao[-4:] if len(self.numero_cartao) >= 4 else "INVÁLIDO"
        print(f"Iniciando processamento Cartão de Crédito de R${valor:.2f} (Final: {numero_cartao_display})...")

        if not all([self.numero_cartao, self.nome_titular, self.data_validade, self.codigo_seguranca]):
            print("Falha no processamento Cartão de Crédito: Dados do cartão incompletos ou inválidos.")
            return False
            
        print(f"Pagamento com Cartão de Crédito (Final: {numero_cartao_display}) no valor de R${valor:.2f} processado com sucesso.")
        return True

class Boleto(FormaPagamento):
    def __init__(self, codigo_barras: str):
        if not isinstance(codigo_barras, str) or len(codigo_barras) < 20:
            print(f"Erro: Código de barras inválido ('{codigo_barras}'). Deve ser uma string com pelo menos 20 caracteres.")
            self.codigo_barras: str = ""
        else:
            self.codigo_barras: str = codigo_barras

    def processar_pagamento(self, valor: float) -> bool:
        print(f"Iniciando processamento Boleto de R${valor:.2f} (Código: '{self.codigo_barras[:20]}...')...")
        if not self.codigo_barras:
            print("Falha no processamento Boleto: Código de barras não definido ou inválido.")
            return False
        
        print(f"Pagamento com Boleto (Código: '{self.codigo_barras[:20]}...') no valor de R${valor:.2f} processado com sucesso.")
        return True
