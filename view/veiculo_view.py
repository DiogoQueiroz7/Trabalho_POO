# from model.veiculo import Veiculo
from model.carro import Carro
from model.moto import Moto
from controller.veiculo_controller import VeiculoController

class VeiculoView:
    def __init__(self):
        self.controller = VeiculoController()
# CADASTRAR MOTO
# ============================================================================================================
    def cadastrar_moto(self):
        placa = input("Placa: ")
        cor = input("Cor: ")
        try:
            cliente_id = int(input("ID do Cliente: "))
            agilidade = int(input("Agilidade: "))
            cilindrada = int(input("Cilindrada: "))
            capacidade_carga = float(input("Capacidade de Carga: "))
        except ValueError:
            print('digite apenas numero')
            return
        adequecao = input("Adequação Urbana: ")
        moto = Moto(None, placa, cor, None, cliente_id, adequecao, agilidade,cilindrada,capacidade_carga)
        self.controller.cadastrar_moto(moto)
        print("Moto cadastrada com sucesso")

# CADASTRAR CARRO
# ============================================================================================================

    def cadastrar_carro(self):
        placa = input("Placa: ")
        cor = input("Cor: ")
        try:
            cliente_id = int(input("ID do Cliente: "))
            adequecao = int(input("Adequação Urbana (1/0): "))
            agilidade = int(input("Agilidade: "))
            capacidade_carga = float(input("Capacidade de Carga: "))
        except ValueError:
            print("digite apenas numeros")
            return
        modelo = input("Modelo: ")
        carro = Carro(None, placa, cor, None, cliente_id, adequecao, agilidade, modelo, capacidade_carga)
        self.controller.cadastrar_carro(carro)
        print("Carro cadastrado com sucesso")

# LISTAR
# ============================================================================================================
    def listar(self):
        veiculos = self.controller.listar()
        for v in veiculos:
            print(f"Placa: {v['placa']}- Cor: {v['cor']}- Tipo ID: {v['tipo_veiculo_id']} - Cliente ID: {v['cliente_id']}")

# ESTIMAR ENTREGA
# ============================================================================================================
    def estimar_entrega(self):

        '''pelo o que eu pesquesei um veiculo comum geralmente
        anda 10 minutos por km, carros gastam 2,50 por km (valor ficticio)'''

        while True:
            print("\n=== Estimar Entrega ===")
            print("1 - Moto")
            print("2 - Carro")
            print("3 - Outros")
            print("4 - Sair")
            opcao = input("Escolha o tipo de veículo: ")

            if opcao == "4":
                break

            try:
                distancia = float(input("informe a distância em km: "))
            except ValueError:
                print("distancia inválida")
                continue

            if opcao == "1":
                tempo = distancia * 7
                custo = distancia * 1.5
                print(f"Moto: Tempo estimado: {tempo:.2f} minutos | Custo: R$ {custo:.2f}")
            elif opcao == "2":
                tempo = distancia * 10
                custo = distancia * 2.5
                print(f"Carro: Tempo estimado: {tempo:.2f} minutos | Custo: R$ {custo:.2f}")
            elif opcao == "3":
                tempo = distancia * 12
                custo = distancia * 3.0
                print(f"Outros: Tempo estimado: {tempo:.2f} minutos | Custo: R$ {custo:.2f}")
            else:
                print("Opção inválida!")

## === menu principal ===
if __name__ == "__main__":
    view = VeiculoView()
    while True:
        opcao = input("\n==== Menu Funcionário SpeedBox ====\n1. Cadastrar Carro\n2. Cadastrar Moto\n3. Listar Veículos\n4. Estimar Entrega\n0. Sair\nEscolha: ")
        if opcao == "1":
            view.cadastrar_carro()
        elif opcao == "2":
            view.cadastrar_moto()
        elif opcao == "3":
            view.listar()
        elif opcao =="4":
            view.estimar_entrega()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
