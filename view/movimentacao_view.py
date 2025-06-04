from model.movimentacao import Movimentacao
from controller.movimentacao_controller import MovimentacaoController
from datetime import datetime

class MovimentacaoView:
    def __init__(self):
        self.controller = MovimentacaoController()

    def registrar(self):
        try:
            veiculo_id = int(input("ID do Veículo: "))
            cliente_id = int(input("ID do Cliente: "))
            transportadora_id = int(input("ID da Transportadora: "))
        except ValueError:
            print("insira apenas numeros")
            return
        localizacao = input("Localização: ")
        status = input("Status: ")
        datahora = datetime.now()
        mov = Movimentacao(None, veiculo_id, datahora, localizacao, status, cliente_id, transportadora_id)
        self.controller.registrar(mov)
        print("Movimentação registrada com sucesso!")

    def listar_por_veiculo(self):
        veiculo_id = int(input("ID do Veículo: "))
        historico = self.controller.listar_por_veiculo(veiculo_id)
        for m in historico:
            print(f"Data/Hora: {m['data_hora']} | Localização: {m['localizacao']} | Status: {m['status']}")

if __name__ == "__main__":
    view = MovimentacaoView()
    while True:
        opcao = input("\n==== Menu Movimentacao ====\n1. registrar movimentacao\n2. listar por veiculo\n0. Sair\nEscolha: ")
        if opcao == "1":
            view.registrar()
        elif opcao == "2":
            view.listar_por_veiculo()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")