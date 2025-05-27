from repository.pagamento_repository import PagamentoRepository 
from model.pagamento import Pagamento 

class PagamentoController:
    def __init__(self):
        self.__repositorio_pag = PagamentoRepository() 

    def criar_pagamento(self, valor: float, encomenda_id: int, forma_pagamento_id: int): 
        if not isinstance(valor, (float, int)) or valor <= 0:
            print("Erro: o Valor precisa ser maior que Zero.")
            return None
        if not isinstance(encomenda_id, int) or encomenda_id <= 0:
            print("Erro: O ID da encomenda é inválido.")
            return None
        if not isinstance(forma_pagamento_id, int) or forma_pagamento_id <= 0:
            print("Erro: O ID da forma de pagamento é inválido.")
            return None
        
        novo_pagamento = Pagamento( 
            valor=float(valor),
            encomenda_id=encomenda_id,
            forma_pagamento_id=forma_pagamento_id
        )

        id_salvo = self.__repositorio_pag.salvar(novo_pagamento)
        if id_salvo:
            print(f"Pagamento de R${novo_pagamento.valor:.2f} criado com sucesso.")
        else:
            print("Erro: Não foi possível salvar o pagamento.")

    def listar_todos_os_pagamentos(self): 
        return self.__repositorio_pag.listar()