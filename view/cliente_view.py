from model.cliente import Cliente
from controller.cliente_controller import ClienteController
from view.encomenda_view import EncomendaView
from view.session_view import SessionView
from view.dashboard_view import DashboardView
from controller.encomenda_controller import EncomendaController
from functions.utils.arquivo import ArquivoUtils

class ClienteView:
    def __init__(self):
        pass
def cadastrar_cliente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    senha = input("Senha: ")
    endereco = input("Endereço: ")

    controller = ClienteController()
    cliente = Cliente(nome, email, senha, cpf, endereco, None)
    controller.salvar(cliente)
    print(f"Olá {cliente.nome} obrigado por se cadastrar em nosso sistema, realize login para enviar sua primeira encomenda!")

def listar_clientes():
    controller = ClienteController()
    clientes = controller.listar()
    print("\n--- Clientes Cadastrados ---")
    for c in clientes:
        print(f"{c.nome} - {c.cpf} - {c.endereco}")

def menu_logado():
    print("\n--- Menu Cliente Logado ---")
    print("\n1 - Enviar uma encomenda \n2 - Ver minhas encomendas \n0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        EncomendaView(encomenda_controller=EncomendaController()).add_encomenda()
    elif opcao == "2":
        user_id = ArquivoUtils().lerArquivoSessao()
        if user_id:
            EncomendaView(encomenda_controller=EncomendaController()).display_encomendas_cliente(user_id)
        else:
            print("Você precisa estar logado para ver suas encomendas.")
    elif opcao == "0":
        print("Saindo do sistema...")
        DashboardView().render()
    else:
        print("Opção inválida, por favor escolha um valor entre 0 e 2.")

def menu_deslogado():
    print("\n--- Menu Cliente Deslogado ---")
    print("\n1 - Cadastro \n2 - Realizar Login \n0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        SessionView().login()
    elif opcao == "0":
        print("Saindo do sistema...")
        DashboardView().render()
    else:
        print("Opção inválida, por favor escolha um valor entre 0 e 2.")

while True:
    print("\n--- Bem-vindo ao Sistema de Encomendas ---")
    if ArquivoUtils().lerArquivoSessao():
        menu_logado()
    else:
        menu_deslogado()
