from repository.veiculo_repository import VeiculoRepository

class VeiculoController:
    def __init__(self):
        self.repo = VeiculoRepository()

    def salvar(self, veiculo):
        return self.repo.salvar(veiculo)

    def listar(self):
        return self.repo.listar()

    def cadastrar_moto(self, moto):
        tipo_id = self.repo.buscar_ou_criar_tipo("Moto")
        moto._tipo_veiculo_id = tipo_id
        veiculo_id = self.repo.salvar(moto)
        self.repo.salvar_moto(veiculo_id, moto.adequacao_urbana, moto.agilidade, moto.cilindrada, moto.capacidade_carga)

    def cadastrar_carro(self, carro):
        tipo_id = self.repo.buscar_ou_criar_tipo("Carro")
        carro._tipo_veiculo_id = tipo_id
        veiculo_id = self.repo.salvar(carro)
        self.repo.salvar_carro(veiculo_id, carro.adequacao_urbana, carro.agilidade, carro.modelo, carro.capacidade_carga)