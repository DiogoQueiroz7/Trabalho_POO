from model.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, id_usuario, nome, email, senha, cpf, endereco, user_id):
        super().__init__(id_usuario, nome, email, senha)
        self._cpf = cpf
        self._endereco = endereco
        self._user_id = user_id

    @property
    def cpf(self): return self._cpf
    @cpf.setter
    def cpf(self, value): self._cpf = value

    @property
    def endereco(self): return self._endereco
    @endereco.setter
    def endereco(self, value): self._endereco = value

    @property
    def user_id(self): return self._user_id
    @user_id.setter
    def user_id(self, value): self._user_id = value
