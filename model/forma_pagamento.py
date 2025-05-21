from datetime import datetime
class FormaPagamento:
    def __init__(self, id_forma_pagamento, tipo: str, data_cadastro = None):
        self._id_forma_pagamento = id_forma_pagamento
        self._tipo = tipo

        if isinstance(data_cadastro, datetime):
            self._data_cadastro = data_cadastro
        else: 
            self._data_cadastro = datetime.now()

    @property
    def id_forma_pagamento(self):
        return self._id_forma_pagamento

    @id_forma_pagamento.setter
    def id_forma_pagamento(self, novo_id: int):
        if isinstance(novo_id, int) and novo_id > 0:
            self._id_forma_pagamento = novo_id
        else:
            print(f"Erro: ID da forma de pagamento inválido ('{novo_id}'). O ID deve ser um inteiro positivo.")

    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def data_cadastro(self) -> datetime:
        return self._data_cadastro

    def processar_pagamento(self, valor: float) -> bool:
        raise NotImplementedError("A subclasse deve implementar o método 'processar_pagamento'")

    def obter_detalhes_para_salvar(self) -> dict:
        return {}

    def __str__(self) -> str:
        return f"{self.__class__.__name__} (ID: {self.id_forma_pagamento}, Tipo: {self.tipo})"


class Pix(FormaPagamento):
    def __init__(self, chave_pix: str, id_forma_pagamento = None, data_cadastro = None):
        super().__init__(id_forma_pagamento, "Pix", data_cadastro)
        if not chave_pix or not isinstance(chave_pix, str):
            print("Alerta: Chave PIX inválida ou não fornecida. Uma chave PIX válida é necessária.")
            self._chave_pix: str = ""
        else:
            self._chave_pix: str = chave_pix

    @property
    def chave_pix(self) -> str:
        return self._chave_pix

    def processar_pagamento(self, valor: float) -> bool:
        print(f"Iniciando processamento PIX de R${valor:.2f} para a chave '{self.chave_pix}'...")
        if not self.chave_pix:
            print("Falha no processamento PIX: Chave PIX não definida ou inválida.")
            return False
        print(f"Pagamento PIX de R${valor:.2f} para '{self.chave_pix}' processado com sucesso (simulação).")
        return True

    def obter_detalhes_para_salvar(self) -> dict:
        return {"chave_pix": self.chave_pix}


class CartaoCredito(FormaPagamento):
    def __init__(self, numero_cartao: str, nome_titular: str, data_validade: str,
                 codigo_seguranca: str, id_forma_pagamento = None, data_cadastro = None):
        super().__init__(id_forma_pagamento, "CartaoCredito", data_cadastro)
        
        self._numero_cartao: str = ""
        self._ultimos_digitos: str = ""
        self._nome_titular: str = ""
        self._data_validade: str = ""
        
        dados_validos_para_objeto = True

        if not isinstance(numero_cartao, str) or not (13 <= len(numero_cartao) <= 19):  
            print(f"Alerta de Cartão: Número do cartão ('{numero_cartao}') está inválido.") 
            dados_validos_para_objeto = False 
        else:
            self._numero_cartao = numero_cartao 
            self._ultimos_digitos = numero_cartao[-4:] 

        if not isinstance(nome_titular, str) or not nome_titular.strip(): 
            print(f"Alerta de Cartão: Nome do titular ('{nome_titular}') é inválido.") 
            dados_validos_para_objeto = False 
        else:
            self._nome_titular = nome_titular.strip() 

        if not isinstance(data_validade, str) or len(data_validade) != 5 or data_validade[2] != '/': 
            print(f"Alerta de Cartão: Data de validade ('{data_validade}') inválida. Use o formato MM/AA.") 
            dados_validos_para_objeto = False 
        else:
            self._data_validade = data_validade 

        if not isinstance(codigo_seguranca, str) or not (3 <= len(codigo_seguranca) <= 4): 
            print(f"Alerta de Cartão: Código de segurança (CVV) ('{codigo_seguranca}') é inválido.") 

        if not dados_validos_para_objeto: 
            print("Aviso IMPORTANTE de Cartão: Um ou mais dados principais desse cartão fornecido são inválidos. " 
                  "O Cartao de Credito foi criado, mas pode não ser funcional ou salvável.") 
            if not self._ultimos_digitos: self._numero_cartao = "" 
            if not self._nome_titular: self._nome_titular = "" 
            if not self._data_validade: self._data_validade = "" 

    @property
    def ultimos_digitos(self) -> str:
        return self._ultimos_digitos

    @property
    def nome_titular(self) -> str:
        return self._nome_titular

    @property
    def data_validade(self) -> str:
        return self._data_validade

    def processar_pagamento(self, valor: float) -> bool:
        numero_cartao_display = self._ultimos_digitos if self._ultimos_digitos else "INVÁLIDO" 
        print(f"Iniciando processamento Cartão de Crédito de R${valor:.2f} (Final: {numero_cartao_display})...") 

        if not all([self._ultimos_digitos, self._nome_titular, self._data_validade]): 
            print("Falha no processamento Cartão de Crédito: Dados do cartão incompletos ou inválidos no objeto.") 
            return False 
        print(f"Pagamento com Cartão de Crédito (Final: {numero_cartao_display}) no valor de R${valor:.2f} processado com sucesso (simulação).") 
        return True

    def obter_detalhes_para_salvar(self) -> dict:
        return {
            "ultimos_digitos": self._ultimos_digitos, 
            "nome_titular": self._nome_titular, 
            "data_validade_cartao": self._data_validade 
        }


class Boleto(FormaPagamento):
    def __init__(self, codigo_barras: str, id_forma_pagamento = None, data_cadastro = None):
        super().__init__(id_forma_pagamento, "Boleto", data_cadastro)
        if not isinstance(codigo_barras, str) or len(codigo_barras) < 20: 
            print(f"Alerta: Código de barras ('{codigo_barras}') é inválido. Deve ser uma string com pelo menos 20 caracteres.") 
            self._codigo_barras: str = "" 
        else:
            self._codigo_barras: str = codigo_barras 

    @property
    def codigo_barras(self) -> str:
        return self._codigo_barras

    def processar_pagamento(self, valor: float) -> bool:
        display_codigo = (self.codigo_barras[:20] + '...' if len(self.codigo_barras) > 20 
                          else self.codigo_barras if self.codigo_barras else "INVÁLIDO") 

        print(f"Iniciando processamento Boleto de R${valor:.2f} (Código: '{display_codigo}')...") 
        if not self.codigo_barras: 
            print("Falha no processamento Boleto: Código de barras não definido ou inválido.") 
            return False 
        print(f"Pagamento com Boleto (Código: '{display_codigo}') no valor de R${valor:.2f} processado com sucesso.") 
        return True 

    def obter_detalhes_para_salvar(self) -> dict:
        return {"codigo_barras": self.codigo_barras} 