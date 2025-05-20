from repository.administrador_repository import AdministradorRepository

class AdministradorController:
    def __init__(self, administrador=None):
        self.__administrador = administrador
        self.__administrador_repository = AdministradorRepository()

    def salvar(self):
        self.__administrador_repository.salvar(self.__administrador)

    def listar(self):
        return self.__administrador_repository.listar()