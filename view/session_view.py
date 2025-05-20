from controller.session_controller import SessionController

class SessionView:
    def __init__(self):
        pass

    def login(self):
        email = input("Email: ")
        password = input("Senha: ")

        controller = SessionController()
        session = controller.login(email, password)

        if session:
            return print(f"Login realizado com sucesso, seu dados de sessão são: {dict(session)}")
        
        return print("Email ou senha inválidos.")
    
    def logout(self):
        controller = SessionController()
        session_id = input("Informe o id da sessao: ")
        controller.delete_session(session_id)

        return print("Logout realizado com sucesso.")
    
def menu():
    session_view = SessionView()
    while True:
        print("\n1 - Login\n2 - Logout\n0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            session_view.login()
        elif opcao == "2":
            session_view.logout()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
if __name__ == "__main__":
    menu()