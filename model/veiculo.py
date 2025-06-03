class Veiculo:
    def __init__(self, id, placa, cor, tipo_veiculo_id, cliente_id):
        self._id = id
        self._placa = placa
        self._cor = cor
        self._tipo_veiculo_id = tipo_veiculo_id
        self._cliente_id = cliente_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    @property
    def placa(self):
        return self._placa

    @property
    def cor(self):
        return self._cor

    @property
    def tipo_veiculo_id(self):
        return self._tipo_veiculo_id

    @property
    def cliente_id(self):
        return self._cliente_id
    
    '''
    calculo base 
    '''
    