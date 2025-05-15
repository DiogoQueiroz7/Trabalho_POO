from model.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, id, placa, modelo, capacidade_carga, adequacao_urbana, agilidade):
        super().__init__(id, placa, modelo, capacidade_carga)
        self.__adequacao_urbana = adequacao_urbana
        self.__agilidade = agilidade

    @property
    def adequacao_urbana(self):
        return self.__adequacao_urbana

    @adequacao_urbana.setter
    def adequacao_urbana(self, value):
        self.__adequacao_urbana = value

    @property
    def agilidade(self):
        return self.__agilidade

    @agilidade.setter
    def agilidade(self, value):
        self.__agilidade = value