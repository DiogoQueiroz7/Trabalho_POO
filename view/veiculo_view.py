from model.veiculo import Veiculo
from controller.veiculo_controller import VeiculoController

class VeiculoView:
    def __init__(self):
        self.controller = VeiculoController()

    def cadastrar_moto(self):
        placa = input("Placa: ")
        cor = input("Cor: ")
        cliente_id = int(input("ID do Cliente: "))
        adequecao = input("Adequação Urbana: ")
        agilidade = int(input("Agilidade: "))
        cilindrada = int(input("Cilindrada: "))
        carga = float(input("Capacidade de Carga: "))
        veiculo = Veiculo(None, placa, cor, None, cliente_id)
        self.controller.cadastrar_moto(veiculo, adequecao, agilidade, cilindrada, carga)
        print("Moto cadastrada com sucesso!")

    def cadastrar_carro(self):
        placa = input("Placa: ")
        cor = input("Cor: ")
        cliente_id = int(input("ID do Cliente: "))
        adequecao = int(input("Adequação Urbana (1/0): "))
        agilidade = int(input("Agilidade: "))
        modelo = input("Modelo: ")
        carga = float(input("Capacidade de Carga: "))
        veiculo = Veiculo(None, placa, cor, None, cliente_id)
        self.controller.cadastrar_carro(veiculo, adequecao, agilidade, modelo, carga)
        print("Carro cadastrado com sucesso!")

    def listar(self):
        veiculos = self.controller.listar()
        for v in veiculos:
            print(f"Placa: {v['placa']} - Cor: {v['cor']} - Tipo ID: {v['tipo_veiculo_id']} - Cliente ID: {v['cliente_id']}")


## === menu principal ===
if __name__ == "__main__":
    view = VeiculoView()
    while True:
        opcao = input("\n==== Menu Funcionário SpeedBox ====\n1. Cadastrar Carro\n2. Cadastrar Moto\n3. Listar Veículos\n0. Sair\nEscolha: ")
        if opcao == "1":
            view.cadastrar_carro()
        elif opcao == "2":
            view.cadastrar_moto()
        elif opcao == "3":
            view.listar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
