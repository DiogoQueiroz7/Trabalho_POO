from datetime import datetime
class FormaPagamento:
    def __init__(self, id_forma_pagamento=None, tipo="Indefinido"):
        self._id_forma_pagamento = id_forma_pagamento
        self._tipo = tipo
        self._data_cadastro = datetime.now() 

    @property
    def id_forma_pagamento(self):
        return self._id_forma_pagamento

    @id_forma_pagamento.setter
    def id_forma_pagamento(self, novo_id): 
        self._id_forma_pagamento = novo_id

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, novo_tipo): 
        self._tipo = novo_tipo
        
    @property
    def data_cadastro(self):
        return self._data_cadastro

    def processar_pagamento(self, valor):
        print(f"Pagamento de R${valor} via {self.tipo} processado.")
        return True

    def obter_detalhes_para_salvar(self):
        return {"tipo": self.tipo}

    def __str__(self):
        return f"{self.__class__.__name__} (ID: {self.id_forma_pagamento}, Tipo: {self.tipo})"
class Pix(FormaPagamento):
    def __init__(self, chave_pix, id_forma_pagamento=None): 
        super().__init__(id_forma_pagamento, "Pix")
        self._chave_pix = chave_pix

    @property
    def chave_pix(self):
        return self._chave_pix

    @chave_pix.setter
    def chave_pix(self, nova_chave): 
        self._chave_pix = nova_chave
        
    def obter_detalhes_para_salvar(self):
        return {"tipo": self.tipo, "chave_pix": self.chave_pix}
class CartaoCredito(FormaPagamento):
    def __init__(self, numero_cartao, nome_titular, data_validade,
                 codigo_seguranca, id_forma_pagamento=None): 
        super().__init__(id_forma_pagamento, "CartaoCredito")
        self._numero_cartao = numero_cartao
        self._ultimos_digitos = numero_cartao[-4:] if numero_cartao else ""
        self._nome_titular = nome_titular
        self._data_validade = data_validade
        self._codigo_seguranca = codigo_seguranca 

    @property
    def ultimos_digitos(self):
        return self._ultimos_digitos

    @property
    def nome_titular(self):
        return self._nome_titular
        
    @nome_titular.setter
    def nome_titular(self, novo_nome_titular): 
        self._nome_titular = novo_nome_titular

    @property
    def data_validade(self):
        return self._data_validade

    @data_validade.setter
    def data_validade(self, nova_data_validade): 
        self._data_validade = nova_data_validade
        
    def obter_detalhes_para_salvar(self):
        return {
            "tipo": self.tipo,
            "ultimos_digitos": self.ultimos_digitos, 
            "nome_titular": self.nome_titular, 
            "data_validade_cartao": self.data_validade 
        }
class Boleto(FormaPagamento):
    def __init__(self, codigo_barras, id_forma_pagamento=None): 
        super().__init__(id_forma_pagamento, "Boleto")
        self._codigo_barras = codigo_barras

    @property
    def codigo_barras(self):
        return self._codigo_barras

    @codigo_barras.setter
    def codigo_barras(self, novo_codigo_barras): 
        self._codigo_barras = novo_codigo_barras
        
    def obter_detalhes_para_salvar(self):
        return {"tipo": self.tipo, "codigo_barras": self.codigo_barras}