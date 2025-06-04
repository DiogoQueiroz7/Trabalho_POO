from controller.encomenda_controller import EncomendaController
from repository.transportadora_repository import TransportadoraRepository
from view.pagamento_view import PagamentoView 

class EncomendaView:
    def __init__(self, encomenda_controller):
        self.encomenda_controller = encomenda_controller

    def display_encomendas(self):
        encomendas = self.encomenda_controller.get_all_encomendas()
        if not encomendas: 
            print("Nenhuma encomenda para exibir.")
            return
        for encomenda in encomendas:
            print(f"Descrição: {encomenda['descricao']}, Peso: {encomenda['peso']}, Volume: {encomenda['volume']}, Cliente ID: {encomenda['cliente_id']}, Transportadora ID: {encomenda['transportadora_id']}")

    def add_encomenda(self):
        descricao = input("Digite a descrição da encomenda: ")
        peso = float(input("Digite o peso da encomenda (kg): "))
        volume = float(input("Digite o volume da encomenda (m³): "))

        print("Para adicionar uma encomenda, você precisa informar o numero da transportadora.")
        transportadoras = TransportadoraRepository().get_all()

        if not transportadoras: 
            print("Nenhuma transportadora cadastrada. Cadastre uma transportadora primeiro.")
            return

        for transportadora in transportadoras:
            print(f"ID: {transportadora['id']}, Razão Social: {transportadora['razao_social']}")
            
        print("Informe o ID da transportadora que você deseja utilizar:")
        transportadora_id = int(input("Digite o ID da transportadora: "))

        try:
            self.encomenda_controller.create_encomenda(
                descricao, peso, volume, transportadora_id
            )
            print("Encomenda adicionada com sucesso!")

            while True:
                escolha_pagamento = input("Deseja prosseguir para o pagamento desta encomenda? (s/n): ").strip().lower()
                if escolha_pagamento == 's':
                    print("\nRedirecionando para o Menu de Pagamentos...")
                    pagamento_view = PagamentoView()
                    pagamento_view.menu_principal_pagamentos()
                    break
                elif escolha_pagamento == 'n':
                    print("Ok, pagamento não iniciado.")
                    break
                else:
                    print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")

        except Exception as e:
            print(f"Ocorreu um erro ao adicionar a encomenda: {e}")
            print("Por favor, verifique se você está logado e se os dados da transportadora são válidos.")


    def display_encomendas_cliente(self, user_id):
        encomendas = self.encomenda_controller.get_all_encomendas_cliente(user_id) #
        cliente_encomendas = [e for e in encomendas]
        
        if not cliente_encomendas:
            print("Nenhuma encomenda encontrada para este cliente.")
            return
        
        for encomenda in cliente_encomendas:
            print(f"Numero da encomenda: {encomenda['id']}, Peso: {encomenda['peso']}, Volume: {encomenda['volume']}, Transportadora: {encomenda['transportadora']}")

def menu(): 
    print("\n--- MENU ENCOMENDAS ---")
    print("1. Listar Todas as Encomendas")
    print("2. Adicionar Nova Encomenda")
    print("3. Realizar Pagamento para Encomenda") 
    print("4. Sair do Menu de Encomendas") 
    return input("Escolha uma opção: ")

def main_encomenda_view(): 
    encomenda_controller = EncomendaController()
    encomenda_view = EncomendaView(encomenda_controller)


    while True:
        choice = menu()
        if choice == '1':
            encomenda_view.display_encomendas()
        elif choice == '2':
            encomenda_view.add_encomenda() 
        elif choice == '3': 
            print("\nVerificando encomendas existentes...")
            todas_as_encomendas = encomenda_view.encomenda_controller.get_all_encomendas()
            if not todas_as_encomendas:
                print("Nenhuma encomenda cadastrada no sistema. Crie uma encomenda primeiro para poder realizar um pagamento.")
            else:
                print("Redirecionando para o Menu de Pagamentos...")
                pagamento_view = PagamentoView()
                pagamento_view.menu_principal_pagamentos()
        elif choice == '4': 
            print("Saindo do Menu de Encomendas...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_encomenda_view()