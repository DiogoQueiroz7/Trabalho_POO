class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = senha

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
        return f"Usuario(nome={self.nome}, email={self.email})"
