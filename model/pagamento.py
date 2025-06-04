from datetime import datetime

class Pagamento:
    STATUS_CONFIRMADO = "Confirmado"

    def __init__(self, valor, encomenda_id, forma_pagamento_id, id_pagamento=None, data_pagamento=None, status=STATUS_CONFIRMADO):
        self._id_pagamento = id_pagamento
        self._valor = float(valor) if valor is not None else 0.0 
        self._encomenda_id = encomenda_id
        self._forma_pagamento_id = forma_pagamento_id
        self._data_pagamento = data_pagamento if data_pagamento else datetime.now()
        self._status_pagamento = status

    @property
    def id_pagamento(self):
        return self._id_pagamento

    @id_pagamento.setter
    def id_pagamento(self, novo_id):
        self._id_pagamento = novo_id

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        self._valor = float(novo_valor) if novo_valor is not None else 0.0 

    @property
    def data_pagamento(self):
        return self._data_pagamento

    @data_pagamento.setter
    def data_pagamento(self, nova_data):
        self._data_pagamento = nova_data if nova_data else datetime.now()

    @property
    def status_pagamento(self):
        return self._status_pagamento
    
    @status_pagamento.setter
    def status_pagamento(self, novo_status):
        self._status_pagamento = novo_status

    @property
    def encomenda_id(self):
        return self._encomenda_id

    @encomenda_id.setter
    def encomenda_id(self, nova_encomenda_id):
        self._encomenda_id = nova_encomenda_id

    @property
    def forma_pagamento_id(self):
        return self._forma_pagamento_id

    @forma_pagamento_id.setter
    def forma_pagamento_id(self, nova_forma_id):
        self._forma_pagamento_id = nova_forma_id

    def __str__(self):
        data_formatada = self._data_pagamento.strftime('%Y-%m-%d %H:%M:%S') if self._data_pagamento else "N/A"
        valor_formatado = f"R${self.valor:.2f}" if self.valor is not None else "R$0.00"

        return (f"Pagamento(ID: {self.id_pagamento}, Valor: {valor_formatado}, "
                f"Data: {data_formatada}, Status: {self.status_pagamento}, "
                f"Encomenda ID: {self.encomenda_id}, Forma Pagamento ID: {self.forma_pagamento_id})")