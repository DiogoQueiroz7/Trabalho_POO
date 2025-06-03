from model.administrador import Administrador
from controller.administrador_controller import AdministradorController
from functions.utils.arquivo import ArquivoUtils
from view.session_view import SessionView
from view.transportadora_view import TransportadoraView
from view.veiculo_view import VeiculoView
from view.encomenda_view import EncomendaView
from view.dashboard_view import DashboardView
from controller.encomenda_controller import EncomendaController
from controller.transportadora_controller import TransportadoraController

class AdministradorView:
    def __init__(self):
        pass

    def cadastrar_administrador(self):
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")

        controller = AdministradorController(Administrador(nome, email, senha))
        controller.salvar()
        print("Administrador cadastrado com sucesso!")

    def listar_administradores(self):
        controller = AdministradorController()
        administradores = controller.listar()
        print("\n--- Administradores Cadastrados ---")
        for a in administradores:
            print(f"{a.nome} - {a.email}")

def menu_administrador_deslogado():
    view = AdministradorView()
    while True:
        print("\n1 - Cadastrar Administrador\n2 - Login\n0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            view.cadastrar_administrador()
        elif opcao == "2":
            SessionView().login()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_administrador_logado():
    print("\n--- Menu Administrador Logado ---")
    print("\n1 - Listar Administradores\n2 - Listar todas encomendas\n3 - Listar transportadoras\n4 - Cadastrar Transportadoras\n5 - Cadastrar Veiculo\n6 - Listar Veiculos\n0 - Sair")
    opcao = input("Escolha: ")

    view = AdministradorView()
    if opcao == "1":
        view.listar_administradores()
    elif opcao == "2":
        EncomendaView(encomenda_controller=EncomendaController()).display_encomendas()
    elif opcao == "3":
        TransportadoraView(transportadora_controller=TransportadoraController()).display_transportadoras()
    elif opcao == "4":
        TransportadoraView(transportadora_controller=TransportadoraController()).add_transportadora()
    elif opcao == "5":
        tipo_veiculo = input("Digite o tipo de veículo (carro/moto): ").strip().lower()
        if tipo_veiculo == "carro":
            VeiculoView().cadastrar_carro()
        elif tipo_veiculo == "moto":
            VeiculoView().cadastrar_moto()
        else:
            print("Tipo de veículo inválido. Por favor, escolha entre 'carro' ou 'moto'.")
    elif opcao == "6":
        VeiculoView().listar()
    elif opcao == "0":
        print("Saindo do sistema...")
        SessionView().logout()
        DashboardView().render()
    else:
        print("Opção inválida, por favor escolha um valor entre 0 e 6.")
while True:
    if ArquivoUtils().lerArquivoSessao():
        menu_administrador_logado()
    else:
        menu_administrador_deslogado()