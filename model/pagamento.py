from datetime import datetime

class Pagamento:

    STATUS_PENDENTE = "Pendente"
    STATUS_CONFIRMADO = "Confirmado"
    STATUS_CANCELADO = "Cancelado"
    STATUS_FALHOU = "Falhou"

    def __init__(self,
                 id_pagamento: int,
                 valor: float,
                 encomenda_id: int,
                 data_pagamento: datetime = None,
                 metodo_pagamento: str = "Não Especificado"):

        if not isinstance(id_pagamento, int) or id_pagamento <= 0:
            print(f"Erro de Inicialização: ID do pagamento inválido ('{id_pagamento}'). Atribuindo ID padrão 0.")
            self._id_pagamento: int = 0
        else:
            self._id_pagamento: int = id_pagamento

        self._valor: float = 0.0  
        self.valor = valor  

        if data_pagamento is None:
            self._data_pagamento: datetime = datetime.now()
        elif isinstance(data_pagamento, datetime):
            self._data_pagamento: datetime = data_pagamento
        else:
            print(f"Erro de Inicialização: data_pagamento inválida ('{data_pagamento}'). Usando data e hora atuais.")
            self._data_pagamento: datetime = datetime.now()

        self._status_pagamento: str = Pagamento.STATUS_PENDENTE
        self._metodo_pagamento: str = metodo_pagamento

        if not isinstance(encomenda_id, int) or encomenda_id <= 0:
            print(f"Erro de Inicialização: ID da encomenda inválido ('{encomenda_id}'). Atribuindo ID padrão 0.")
            self._encomenda_id: int = 0
        else:
            self._encomenda_id: int = encomenda_id

    @property
    def id(self) -> int:
        return self._id_pagamento

    @property
    def valor(self) -> float:
        return self._valor

    @valor.setter
    def valor(self, novo_valor: float) -> None:
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
    def metodo_pagamento(self) -> str:
        return self._metodo_pagamento

    def _verificar_ids_validos(self) -> bool:

        if self._id_pagamento == 0 or self._encomenda_id == 0:
            print(f"Atenção: Pagamento com ID {self.id} ou Encomenda ID {self.encomenda_id} possui dados de ID padrão (0), "
                  "indicando possível erro na inicialização. A operação pode não ser confiável.")
            return False
        return True

    def confirmar_pagamento(self) -> None:

        self._verificar_ids_validos() 

        if self._status_pagamento == Pagamento.STATUS_PENDENTE:
            self._status_pagamento = Pagamento.STATUS_CONFIRMADO
            print(f"Pagamento ID {self.id} confirmado.")
        elif self._status_pagamento == Pagamento.STATUS_CONFIRMADO:
            print(f"Pagamento ID {self.id} já está confirmado.")
        else:
            print(f"Não é possível confirmar o pagamento ID {self.id} com status '{self._status_pagamento}'.")

    def cancelar_pagamento(self) -> None:

        self._verificar_ids_validos()

        if self._status_pagamento in [Pagamento.STATUS_PENDENTE, Pagamento.STATUS_CONFIRMADO]:
            self._status_pagamento = Pagamento.STATUS_CANCELADO
            print(f"Pagamento ID {self.id} cancelado.")
        elif self._status_pagamento == Pagamento.STATUS_CANCELADO:
            print(f"Pagamento ID {self.id} já está cancelado.")
        else:
            print(f"Não é possível cancelar o pagamento ID {self.id} com status '{self._status_pagamento}'.")

    def falhar_pagamento(self) -> None:

        self._verificar_ids_validos()

        if self._status_pagamento == Pagamento.STATUS_PENDENTE:
            self._status_pagamento = Pagamento.STATUS_FALHOU
            print(f"Pagamento ID {self.id} marcado como falho.")
        else:
            print(f"Não é possível marcar como falho o pagamento ID {self.id} com status '{self._status_pagamento}'.")

    def __str__(self) -> str:
        return (f"Pagamento(ID: {self.id}, Valor: R${self.valor:.2f}, "
                f"Data: {self.data_pagamento.strftime('%Y-%m-%d %H:%M:%S')}, "
                f"Status: {self.status_pagamento}, Encomenda ID: {self.encomenda_id}, "
                f"Método: {self.metodo_pagamento})")
