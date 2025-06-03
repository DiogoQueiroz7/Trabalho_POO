from model.veiculo import Veiculo

class Moto(Veiculo):
    '''
    Classe Moto herdando de Veiculo com todos os campos necessários.
    '''
    def __init__(self, id, placa, cor, tipo_veiculo_id, cliente_id, adequacao_urbana, agilidade, cilindrada, capacidade_carga):
        super().__init__(id, placa, cor, tipo_veiculo_id, cliente_id)
        self.adequacao_urbana = adequacao_urbana
        self.agilidade = agilidade
        self.cilindrada = cilindrada
        self.capacidade_carga = capacidade_carga

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
    def cilindrada(self):
        return self._cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        self._cilindrada = value

    @property
    def capacidade_carga(self):
        return self._capacidade_carga

    @capacidade_carga.setter
    def capacidade_carga(self, value):
        self._capacidade_carga = value