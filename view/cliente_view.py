from model.cliente import Cliente
from controller.cliente_controller import ClienteController

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
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    controller = ClienteController()
    clientes = controller.listar()
    print("\n--- Clientes Cadastrados ---")
    for c in clientes:
        print(f"{c.nome} - {c.cpf} - {c.endereco}")

# Simulação de menu
while True:
    print("\n1 - Cadastrar Cliente\n2 - Listar Clientes\n0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
