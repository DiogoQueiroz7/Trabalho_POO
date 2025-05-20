from model.veiculo import Veiculo

class Carro(Veiculo):
    '''
    aqui vemos a classe carro herdar atributos da sua classe pai "Veiculos" usando o super()
    '''
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
    
    '''pelo o que eu pesquesei um veiculo comum geralmente
    anda 10 minutos por km, carros gastam 2,50 por km (valor ficticio)'''
    
    def calcular_tempo(self, distancia_km):
        return distancia_km * 10

    def calcular_custo(self, distancia_km):
        return distancia_km * 2.5