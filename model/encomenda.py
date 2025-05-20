class Encomenda:
    def __init__(self, descricao, peso, volume, cliente_id, transportadora_id):
        self.descricao = descricao
        self.peso = peso
        self.volume = volume
        self.cliente_id = cliente_id
        self.transportadora_id = transportadora_id

    def __repr__(self):
        return f"Encomenda(descricao='{self.descricao}', peso={self.peso}, volume={self.volume}, cliente_id={self.cliente_id}, transportadora_id={self.transportadora_id})"
    def __str__(self):
        return f"Encomenda: {self.descricao}, Peso: {self.peso}, Volume: {self.volume}, Cliente ID: {self.cliente_id}, Transportadora ID: {self.transportadora_id}"