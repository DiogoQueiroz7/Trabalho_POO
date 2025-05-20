from repository.movimentacao_repository import MovimentacaoRepository

class MovimentacaoController:
    def __init__(self):
        self.repo = MovimentacaoRepository()

    def registrar(self, movimentacao):
        return self.repo.registrar(movimentacao)

    def listar_por_veiculo(self, veiculo_id):
        return self.repo.listar_por_veiculo(veiculo_id)