from datetime import datetime

class Movimentacao:
    def __init__(self, id, veiculo_id, datahora, localizacao, status, cliente_id, transportadora_id):
        self.id = id
        self.veiculo_id = veiculo_id
        self.datahora = datahora
        self.localizacao = localizacao 
        self.status = status  
        self.cliente_id = cliente_id
        self.transportadora_id = transportadora_id