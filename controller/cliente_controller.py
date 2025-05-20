from repository.cliente_repository import ClienteRepository

class ClienteController:
    def __init__(self):
        self.__cliente_repository = ClienteRepository()

    def salvar(self, cliente):
        self.__cliente_repository.salvar(cliente)

    def listar(self):
        return self.__cliente_repository.listar()