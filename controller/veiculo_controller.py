from repository.veiculo_repository import VeiculoRepository

class VeiculoController:
    def __init__(self):
        self.repo = VeiculoRepository()

    def salvar(self, veiculo):
        return self.repo.salvar(veiculo)

    def listar(self):
        return self.repo.listar()

    def cadastrar_moto(self, veiculo, adequecao, agilidade, cilindrada, carga):
        tipo_id = self.repo.buscar_ou_criar_tipo("Moto")
        veiculo._tipo_veiculo_id = tipo_id
        veiculo_id = self.repo.salvar(veiculo)
        self.repo.salvar_moto(veiculo_id, adequecao, agilidade, cilindrada, carga)

    def cadastrar_carro(self, veiculo, adequecao, agilidade, modelo, carga):
        tipo_id = self.repo.buscar_ou_criar_tipo("Carro")
        veiculo._tipo_veiculo_id = tipo_id
        veiculo_id = self.repo.salvar(veiculo)
        self.repo.salvar_carro(veiculo_id, adequecao, agilidade, modelo, carga)