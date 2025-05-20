from datetime import datetime

class FormaPagamento: 
    '''
    Classe Abstrata que está representando as formas de pagamento
    '''
    def __init__(self, id_forma_pagamento: int | None, tipo: str, data_cadastro: datetime | str | None = None): 
        '''
        Inicializa uma Instância nova de forma de pagamento 
        '''
        self._id_forma_pagamento = id_forma_pagamento
        self._tipo = tipo 

        if isinstance(data_cadastro, str):
            try:
                self._data_cadastro = datetime.fromisoformat(data_cadastro)
            except ValueError:
                print(f"Alerta: Formato de data_cadastro string inválido ('{data_cadastro}'). Usando data atual.")
                self._data_cadastro = datetime.now()
        elif isinstance(data_cadastro, datetime):
            self._data_cadastro = data_cadastro
        else:
            self._data_cadastro = datetime.now()

    @property
    def id_forma_pagamento(self) -> int | None:
        '''
        identificar unico da forma de pagamento
        '''
        return self._id_forma_pagamento

    @id_forma_pagamento.setter
    def id_forma_pagamento(self, novo_id: int) -> None:
        '''
        define o id da forma de pagamento
        '''
        if isinstance(novo_id, int) and novo_id > 0:
            self._id_forma_pagamento = novo_id
        else:
            print(f"Erro: ID da forma de pagamento inválido ('{novo_id}').")


    @property
    def tipo(self) -> str:
        return self._tipo

    @property
    def data_cadastro(self) -> datetime:
        '''
        define data e hora do cadastro    
        ''' 
        return self._data_cadastro 
    


    def processar_pagamento(self, valor: float) -> bool:
        """
        Processa um pagamento utilizando determinada forma de pagamento."""
        raise NotImplementedError("A subclasse deve implementar o método 'processar_pagamento'")

    def obter_detalhes_para_salvar(self) -> dict:
        '''
        usado pra retornar um dicionário com os detlahes da forma de pagametno
        '''

        return {}

    def __str__(self) -> str:
        return f"{self.__class__.__name__} (ID: {self.id_forma_pagamento}, Tipo: {self.tipo})"


class Pix(FormaPagamento):
    '''
    representa a forma de pagamento do pix, herda de FormaPagamento
    '''
    def __init__(self, chave_pix: str, id_forma_pagamento: int | None = None, data_cadastro: datetime | str | None = None):
        super().__init__(id_forma_pagamento, "Pix", data_cadastro)
        if not chave_pix or not isinstance(chave_pix, str):
            print("Alerta: Chave PIX inválida ou não fornecida. Usando chave vazia.")
            self._chave_pix: str = ""
        else:
            self._chave_pix: str = chave_pix

    @property
    def chave_pix(self) -> str:
        return self._chave_pix

    def processar_pagamento(self, valor: float) -> bool:
        '''
        tentativa de simular o processamento de um pagamento por pix, retornando true para quando der certo e false para quando der errado
        '''
        print(f"Iniciando processamento PIX de R${valor:.2f} para a chave '{self.chave_pix}'...")
        if not self.chave_pix:
            print("Falha no processamento PIX: Chave PIX não definida ou inválida.")
            return False
        
        print(f"Pagamento PIX de R${valor:.2f} para '{self.chave_pix}' processado com sucesso.")
        return True

    def obter_detalhes_para_salvar(self) -> dict:
        '''
        retorna os detalhes da transação do pix
        '''
        return {"chave_pix": self.chave_pix}


class CartaoCredito(FormaPagamento):
    def __init__(self, numero_cartao: str, nome_titular: str, data_validade: str, 
                 codigo_seguranca: str, id_forma_pagamento: int | None = None, data_cadastro: datetime | str | None = None):
        super().__init__(id_forma_pagamento, "CartaoCredito", data_cadastro)
        '''
        incializa uma nova instância de pagamento que herda também da forma pagamento, validando os dados do cartão durante a incialização er armazena as informações mais "publicas"
        '''
        
        self._numero_cartao: str = "" 
        self._ultimos_digitos: str = "" 
        self._nome_titular: str = ""
        self._data_validade: str = "" 

        dados_validos = True
        if not isinstance(numero_cartao, str) or not (13 <= len(numero_cartao) <= 19) or not numero_cartao.isdigit():
            print(f"Alerta: Número do cartão inválido ('{numero_cartao}').")
            dados_validos = False
        else:
            self._numero_cartao = numero_cartao 
            self._ultimos_digitos = numero_cartao[-4:]


        if not isinstance(nome_titular, str) or not nome_titular.strip():
            print(f"Alerta: Nome do titular inválido ('{nome_titular}').")
            dados_validos = False
        else:
            self._nome_titular = nome_titular.strip()

        if not isinstance(data_validade, str) or len(data_validade) != 5 or data_validade[2] != '/':
            print(f"Alerta: Data de validade inválida ('{data_validade}'). Use o formato MM/YY.")
            dados_validos = False
        else:
            self._data_validade = data_validade
            
        if not isinstance(codigo_seguranca, str) or not (3 <= len(codigo_seguranca) <= 4) or not codigo_seguranca.isdigit():
            print(f"Alerta: Código de segurança (CVV) inválido ('{codigo_seguranca}').")
            dados_validos = False
        

        if not dados_validos:
            print("Alerta: Dados do cartão de crédito inválidos. O processamento pode falhar e os dados não serão completamente definidos.")
            if not self._ultimos_digitos: self._numero_cartao = "" 
            if not self._nome_titular: self._nome_titular = ""
            if not self._data_validade: self._data_validade = ""


    @property
    def ultimos_digitos(self) -> str:
        return self._ultimos_digitos
    '''
    os ultimos 4 digitos do cartão
    '''

    @property
    def nome_titular(self) -> str:
        return self._nome_titular

    @property
    def data_validade(self) -> str: 
        return self._data_validade

    def processar_pagamento(self, valor: float) -> bool:
        '''
        tentativa de simular o processamento de uma transação de crédito
        '''
        numero_cartao_display = self._ultimos_digitos if self._ultimos_digitos else "INVÁLIDO"
        print(f"Iniciando processamento Cartão de Crédito de R${valor:.2f} (Final: {numero_cartao_display})...")

        if not all([self._ultimos_digitos, self._nome_titular, self._data_validade]):
            print("Falha no processamento Cartão de Crédito: Dados do cartão incompletos ou inválidos no objeto.")
            return False
        
        print(f"Pagamento com Cartão de Crédito (Final: {numero_cartao_display}) no valor de R${valor:.2f} processado com sucesso.")
        return True

    def obter_detalhes_para_salvar(self) -> dict:
        return {
            "ultimos_digitos": self._ultimos_digitos,
            "nome_titular": self._nome_titular,
            "data_validade_cartao": self._data_validade 
        }


class Boleto(FormaPagamento):
    def __init__(self, codigo_barras: str, id_forma_pagamento: int | None = None, data_cadastro: datetime | str | None = None):
        super().__init__(id_forma_pagamento, "Boleto", data_cadastro)
        if not isinstance(codigo_barras, str) or len(codigo_barras) < 20: # Validação simples
            print(f"Alerta: Código de barras inválido ('{codigo_barras}'). Deve ser uma string com pelo menos 20 caracteres.")
            self._codigo_barras: str = ""
        else:
            self._codigo_barras: str = codigo_barras

    @property
    def codigo_barras(self) -> str:
        return self._codigo_barras

    def processar_pagamento(self, valor: float) -> bool:
        display_codigo = self.codigo_barras[:20] + '...' if len(self.codigo_barras) > 20 else self.codigo_barras #validação do código de barras 
        print(f"Iniciando processamento Boleto de R${valor:.2f} (Código: '{display_codigo}')...")
        if not self.codigo_barras:
            print("Falha no processamento Boleto: Código de barras não definido ou inválido.")
            return False
        
        print(f"Pagamento com Boleto (Código: '{display_codigo}') no valor de R${valor:.2f} processado com sucesso.")
        return True

    def obter_detalhes_para_salvar(self) -> dict:
        return {"codigo_barras": self.codigo_barras}