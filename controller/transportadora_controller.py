from model.transportadora import Transportadora
from repository.transportadora_repository import TransportadoraRepository

class TransportadoraController:
    def __init__(self):
        self.transportadora_repository = TransportadoraRepository()

    def create_transportadora(self, razao_social, cnpj, endereco):
        transportadora = Transportadora(razao_social, cnpj, endereco)
        return self.transportadora_repository.create(transportadora)

    def get_all_transportadoras(self):
        return self.transportadora_repository.get_all()