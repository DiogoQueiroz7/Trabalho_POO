from datetime import datetime
class Pagamento:

    STATUS_CONFIRMADO = "Confirmado"

    def __init__(self,
                 valor: float,
                 encomenda_id: int,
                 forma_pagamento_id: int,
                 id_pagamento = None, 
                 data_pagamento = None, 
                 status = STATUS_CONFIRMADO): 

        self._id_pagamento = id_pagamento
        self._valor: float = 0.0 
        self.valor = valor 

        if data_pagamento is None:
            self._data_pagamento: datetime = datetime.now()
        elif isinstance(data_pagamento, datetime):
            self._data_pagamento: datetime = data_pagamento
        else:
            print(f"Alerta de Inicialização: data_pagamento inválida ('{data_pagamento}'). Usando data e hora atuais.")
            self._data_pagamento: datetime = datetime.now()
            
        self._status_pagamento: str = status if status else Pagamento.STATUS_CONFIRMADO

        if not isinstance(encomenda_id, int) or encomenda_id <= 0:
            print(f"Alerta de Inicialização: ID da encomenda inválido ('{encomenda_id}'). Será usado o valor 0.")
            self._encomenda_id: int = 0 
        else:
            self._encomenda_id: int = encomenda_id
        if not isinstance(forma_pagamento_id, int) or forma_pagamento_id <= 0:
            print(f"Alerta de Inicialização: ID da forma de pagamento inválido ('{forma_pagamento_id}'). Será usado o valor 0.")
            self._forma_pagamento_id: int = 0
        else:
            self._forma_pagamento_id: int = forma_pagamento_id

    @property
    def id_pagamento(self): 
        return self._id_pagamento

    @id_pagamento.setter
    def id_pagamento(self, novo_id: int): 
        if isinstance(novo_id, int) and novo_id > 0:
            self._id_pagamento = novo_id
        else:
            print(f"Erro ao definir ID do pagamento: ID inválido ('{novo_id}'). Deve ser um inteiro positivo.")

    @property
    def valor(self) -> float:
        return self._valor

    @valor.setter
    def valor(self, novo_valor: float): 
        if not isinstance(novo_valor, (int, float)): 
            print(f"Erro ao definir valor: O valor ('{novo_valor}') deve ser numérico. Valor não alterado.")
            return
        if novo_valor < 0:
            print(f"Erro ao definir valor: O valor ('{novo_valor}') não pode ser negativo. Valor não alterado.")
            return 
        self._valor = float(novo_valor) 

    @property
    def data_pagamento(self) -> datetime: 
        return self._data_pagamento

    @property
    def status_pagamento(self) -> str: 
        return self._status_pagamento

    @property
    def encomenda_id(self) -> int: 
        return self._encomenda_id

    @property
    def forma_pagamento_id(self) -> int:
        return self._forma_pagamento_id

    @forma_pagamento_id.setter
    def forma_pagamento_id(self, nova_forma_id: int): 
        if isinstance(nova_forma_id, int) and nova_forma_id > 0:
            self._forma_pagamento_id = nova_forma_id
        else:
            print(f"Erro ao definir ID da forma de pagamento: ID inválido ('{nova_forma_id}'). Deve ser um inteiro positivo.")

    def __str__(self) -> str: 
        data_formatada = self._data_pagamento.strftime('%Y-%m-%d %H:%M:%S') if self._data_pagamento else "N/A"
        valor_formatado = f"R${self.valor:.2f}"

        return (f"Pagamento(ID: {self.id_pagamento}, Valor: {valor_formatado}, "
                f"Data: {data_formatada}, Status: {self.status_pagamento}, "
                f"Encomenda ID: {self.encomenda_id}, Forma Pagamento ID: {self.forma_pagamento_id})")