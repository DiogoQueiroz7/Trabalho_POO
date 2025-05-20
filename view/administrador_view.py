from model.administrador import Administrador
from controller.administrador_controller import AdministradorController

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

def menu_administrador():
    view = AdministradorView()
    while True:
        print("\n1 - Cadastrar Administrador\n2 - Listar Administradores\n0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            view.cadastrar_administrador()
        elif opcao == "2":
            view.listar_administradores()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
if __name__ == "__main__":
    menu_administrador()