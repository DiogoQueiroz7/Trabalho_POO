class Usuario:
    def __init__(self, id_usuario, nome, email, senha):
        self.__id_usuario = id_usuario
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    @property
    def id_usuario(self): return self.__id_usuario

    @property
    def nome(self): return self.__nome
    @nome.setter
    def nome(self, value): self.__nome = value

    @property
    def email(self): return self.__email
    @email.setter
    def email(self, value): self.__email = value

    @property
    def senha(self): return self.__senha
    @senha.setter
    def senha(self, value): self.__senha = value

    def __str__(self):
        return f"Usuario(id_usuario={self.id_usuario}, nome={self.nome}, email={self.email})"
