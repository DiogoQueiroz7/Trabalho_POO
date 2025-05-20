from controller.encomenda_controller import EncomendaController

class EncomendaView:
    def __init__(self, encomenda_controller):
        self.encomenda_controller = encomenda_controller

    def display_encomendas(self):
        encomendas = self.encomenda_controller.get_all_encomendas()
        for encomenda in encomendas:
            print(f"Descrição: {encomenda.descricao}, Peso: {encomenda.peso}, Volume: {encomenda.volume}, Cliente ID: {encomenda.cliente_id}, Transportadora ID: {encomenda.transportadora_id}")

    def add_encomenda(self):
        descricao = input("Digite a descrição da encomenda: ")
        peso = float(input("Digite o peso da encomenda (kg): "))
        volume = float(input("Digite o volume da encomenda (m³): "))
        cliente_id = int(input("Digite o ID do cliente: "))
        transportadora_id = int(input("Digite o ID da transportadora: "))

        self.encomenda_controller.create_encomenda(
            descricao, peso, volume, cliente_id, transportadora_id
        )
        print("Encomenda adicionada com sucesso!")
    
def menu():
    print("\n--- MENU ---")
    print("1. Listar Encomendas")
    print("2. Adicionar Encomenda")
    print("3. Sair")
    return input("Escolha uma opção: ")

def main():
    encomenda_controller = EncomendaController()
    encomenda_view = EncomendaView(encomenda_controller)

    while True:
        choice = menu()
        if choice == '1':
            encomenda_view.display_encomendas()
        elif choice == '2':
            encomenda_view.add_encomenda()
        elif choice == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
