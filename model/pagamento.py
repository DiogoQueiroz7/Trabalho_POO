from datetime import datetime

class Pagamento:
    """
    Representa um registro de pagamento associado a uma encomenda.
    Esta classe gerencia os detalhes de um pagamento, incluindo seu valor,
    status, data, e os IDs da encomenda e da forma de pagamento relacionadas.
    """

    STATUS_PENDENTE = "Pendente"
    STATUS_CONFIRMADO = "Confirmado"
    STATUS_CANCELADO = "Cancelado"
    STATUS_FALHOU = "Falhou"

    def __init__(self,
                 valor: float,
                 encomenda_id: int,
                 forma_pagamento_id: int, 
                 id_pagamento: int | None = None, 
                 data_pagamento: datetime | None = None,
                 status: str | None = None): 

        self._id_pagamento: int | None = id_pagamento 

        self._valor: float = 0.0
        self.valor = valor 

        if data_pagamento is None:
            self._data_pagamento: datetime = datetime.now()
        elif isinstance(data_pagamento, datetime):
            self._data_pagamento: datetime = data_pagamento
        else:
            print(f"Alerta de Inicialização: data_pagamento inválida ('{data_pagamento}'). Usando data e hora atuais.")
            self._data_pagamento: datetime = datetime.now()

        self._status_pagamento: str = status if status else Pagamento.STATUS_PENDENTE

        if not isinstance(encomenda_id, int) or encomenda_id <= 0:
            print(f"Alerta de Inicialização: ID da encomenda inválido ('{encomenda_id}').")
            self._encomenda_id: int = 0 
        else:
            self._encomenda_id: int = encomenda_id

        if not isinstance(forma_pagamento_id, int) or forma_pagamento_id <= 0:
            print(f"Alerta de Inicialização: ID da forma de pagamento inválido ('{forma_pagamento_id}').")
            self._forma_pagamento_id: int = 0 
        else:
            self._forma_pagamento_id: int = forma_pagamento_id

    @property
    def id_pagamento(self) -> int | None: #Define o id do pagamento 
        return self._id_pagamento

    @id_pagamento.setter
    def id_pagamento(self, novo_id: int) -> None: 
        if isinstance(novo_id, int) and novo_id > 0:
            self._id_pagamento = novo_id
        else:
            print(f"Erro ao definir ID do pagamento: ID inválido ('{novo_id}').")


    @property
    def valor(self) -> float: #define o valor do pagamento 
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
    def data_pagamento(self) -> datetime: #data e hora do pagaemtno 
        return self._data_pagamento

    @property
    def status_pagamento(self) -> str: #qual o status atual do pamento? pendente, confirmado...
        return self._status_pagamento

    @property
    def encomenda_id(self) -> int:
        return self._encomenda_id
    
    @property
    def forma_pagamento_id(self) -> int: 
        return self._forma_pagamento_id

    
    @forma_pagamento_id.setter
    def forma_pagamento_id(self, nova_forma_id: int) -> None:
        if isinstance(nova_forma_id, int) and nova_forma_id > 0:
            self._forma_pagamento_id = nova_forma_id
        else:
            print(f"Erro ao definir ID da forma de pagamento: ID inválido ('{nova_forma_id}').")


    def _ids_realmente_validos_para_operacao(self) -> bool:
        """
        Verifica internamente se os IDs essenciais (pagamento, encomenda, forma de pagamento)
        são válidos para realizar operações de mudança de status.
        """
        
        if not self._id_pagamento or self._id_pagamento <= 0:
            print(f"Atenção: Pagamento ID {self.id_pagamento} não está persistido ou possui ID inválido.")
            return False
        if not self._encomenda_id or self._encomenda_id <= 0:
            print(f"Atenção: Encomenda ID {self.encomenda_id} inválido para o pagamento ID {self.id_pagamento}.")
            return False
        if not self._forma_pagamento_id or self._forma_pagamento_id <= 0:
            print(f"Atenção: Forma de Pagamento ID {self.forma_pagamento_id} inválido para o pagamento ID {self.id_pagamento}.")
            return False
        return True

    def confirmar_pagamento(self) -> bool: 
        """
        Muda o status do pagamento para 'Confirmado'.
        Só pode ser confirmado se o status atual for 'Pendente' e os IDs
        relevantes (pagamento, encomenda, forma de pagamento) forem válidos."""
        if not self._ids_realmente_validos_para_operacao():
            return False
        if self._status_pagamento == Pagamento.STATUS_PENDENTE:
            self._status_pagamento = Pagamento.STATUS_CONFIRMADO
            print(f"Pagamento ID {self.id_pagamento} confirmado.")
            return True
        elif self._status_pagamento == Pagamento.STATUS_CONFIRMADO:
            print(f"Pagamento ID {self.id_pagamento} já está confirmado.")
            return True 
        else:
            print(f"Não é possível confirmar o pagamento ID {self.id_pagamento} com status '{self._status_pagamento}'.")
            return False

    def cancelar_pagamento(self) -> bool:
        """
        muda o status para cancelado e só pode ser cancelado se o status atual 
        for "pendente" ou "confirmado" e os ids relevantes forem válidos
        """
        if not self._ids_realmente_validos_para_operacao():
            return False
        if self._status_pagamento in [Pagamento.STATUS_PENDENTE, Pagamento.STATUS_CONFIRMADO]:
            self._status_pagamento = Pagamento.STATUS_CANCELADO
            print(f"Pagamento ID {self.id_pagamento} cancelado.")
            return True
        elif self._status_pagamento == Pagamento.STATUS_CANCELADO:
            print(f"Pagamento ID {self.id_pagamento} já está cancelado.")
            return True
        else:
            print(f"Não é possível cancelar o pagamento ID {self.id_pagamento} com status '{self._status_pagamento}'.")
            return False

    def falhar_pagamento(self) -> bool:
        """
        Muda o status do pagamento para 'Falhou'.
        Só pode ser marcado como falho se o status atual for 'Pendente'
        e os IDs relevantes forem válidos."""
        
        if not self._ids_realmente_validos_para_operacao():
            return False
        if self._status_pagamento == Pagamento.STATUS_PENDENTE:
            self._status_pagamento = Pagamento.STATUS_FALHOU
            print(f"Pagamento ID {self.id_pagamento} marcado como falho.")
            return True
        else:
            print(f"Não é possível marcar como falho o pagamento ID {self.id_pagamento} com status '{self._status_pagamento}'.")
            return False

    def __str__(self) -> str:
        return (f"Pagamento(ID: {self.id_pagamento}, Valor: R${self.valor:.2f}, "
                f"Data: {self.data_pagamento.strftime('%Y-%m-%d %H:%M:%S')}, "
                f"Status: {self.status_pagamento}, Encomenda ID: {self.encomenda_id}, "
                f"Forma Pagamento ID: {self.forma_pagamento_id})")