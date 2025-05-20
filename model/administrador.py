from model.usuario import Usuario

class Administrador(Usuario):
    def __init__(self, nome, email, senha):
        super().__init__(nome, email, senha)
        self.__nivel_acesso = "TOTAL"

    @property
    def get_nivel_acesso(self):
        return self.__nivel_acesso
    
    @get_nivel_acesso.setter
    def set_nivel_acesso(self, nivel_acesso):
        self.__nivel_acesso = nivel_acesso