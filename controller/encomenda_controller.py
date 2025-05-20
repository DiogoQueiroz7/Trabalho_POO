from repository.encomenda_repository import EncomendaRepository
from model.encomenda import Encomenda

class EncomendaController:
    def __init__(self):
        self.encomenda_repository = EncomendaRepository()

    def create_encomenda(self, descricao, peso, volume, cliente_id, transportadora_id):
        encomenda = Encomenda(
            descricao=descricao,
            peso=peso,
            volume=volume,
            cliente_id=cliente_id,
            transportadora_id=transportadora_id
        )
        return self.encomenda_repository.create(encomenda)

    def get_all_encomendas(self):
        return self.encomenda_repository.get_all()
