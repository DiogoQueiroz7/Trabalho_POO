from controller.transportadora_controller import TransportadoraController
from model.transportadora import Transportadora  # importando o modelo

class TransportadoraView:
    def __init__(self, transportadora_controller):
        self.transportadora_controller = transportadora_controller

    def display_transportadoras(self):
        transportadoras = self.transportadora_controller.get_all_transportadoras()
        for transportadora in transportadoras:
            print(f"ID: {transportadora['id']}, Razão Social: {transportadora['razao_social']}, CNPJ: {transportadora['cnpj']}, Endereço: {transportadora['endereco']}")
    def add_transportadora(self):
        razao_social = input("Digite a razão social da transportadora: ")
        cnpj = input("Digite o CNPJ da transportadora: ")
        endereco = input("Digite o endereço da transportadora: ")

        # Chama o método correto do controller passando os parâmetros
        self.transportadora_controller.create_transportadora(razao_social, cnpj, endereco)
        print("Transportadora adicionada com sucesso!")


def menu():
    print("1. Listar Transportadoras")
    print("2. Adicionar Transportadora")
    print("3. Sair")
    return input("Escolha uma opção: ")

def main():
    transportadora_controller = TransportadoraController()
    transportadora_view = TransportadoraView(transportadora_controller)

    while True:
        choice = menu()
        if choice == '1':
            transportadora_view.display_transportadoras()
        elif choice == '2':
            transportadora_view.add_transportadora()
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
