from model.veiculo import Veiculo

class Carro(Veiculo):
    '''
    aqui vemos a classe carro herdar atributos da sua classe pai "Veiculos" usando o super()
    '''
    def __init__(self, id, placa, cor, tipo_veiculo_id, cliente_id, adequacao_urbana, agilidade, modelo, capacidade_carga):
        super().__init__(id, placa, cor, tipo_veiculo_id, cliente_id)
        self._adequacao_urbana = adequacao_urbana
        self._agilidade = agilidade
        self._modelo = modelo
        self._capacidade_carga = capacidade_carga

    @property
    def adequacao_urbana(self):
        return self._adequacao_urbana

    @adequacao_urbana.setter
    def adequacao_urbana(self, value):
        self._adequacao_urbana = value

    @property
    def agilidade(self):
        return self._agilidade

    @agilidade.setter
    def agilidade(self, value):
        self._agilidade = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def capacidade_carga(self):
        return self._capacidade_carga

    @capacidade_carga.setter
    def capacidade_carga(self, value):
        self._capacidade_carga = value
    
   