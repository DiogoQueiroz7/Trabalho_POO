class DashboardView:
    def __init__(self):
        pass

    def render(self):
        print(r"""
        ______   _______   ________  ________  _______   _______    ______   __    __ 
        /      \ /       \ /        |/        |/       \ /       \  /      \ /  |  /  |
        /$$$$$$  |$$$$$$$  |$$$$$$$$/ $$$$$$$$/ $$$$$$$  |$$$$$$$  |/$$$$$$  |$$ |  $$ |
        $$ \__$$/ $$ |__$$ |$$ |__    $$ |__    $$ |  $$ |$$ |__$$ |$$ |  $$ |$$  \/$$/ 
        $$      \ $$    $$/ $$    |   $$    |   $$ |  $$ |$$    $$< $$ |  $$ | $$  $$<  
        $$$$$$  |$$$$$$$/  $$$$$/    $$$$$/    $$ |  $$ |$$$$$$$  |$$ |  $$ |  $$$$  \ 
        /  \__$$ |$$ |      $$ |_____ $$ |_____ $$ |__$$ |$$ |__$$ |$$ \__$$ | $$ /$$  |
        $$    $$/ $$ |      $$       |$$       |$$    $$/ $$    $$/ $$    $$/ $$ |  $$ |
        $$$$$$/  $$/       $$$$$$$$/ $$$$$$$$/ $$$$$$$/  $$$$$$$/   $$$$$$/  $$/   $$/ 
                                                                                        
                                                                                        
        """)

        print(f"Digite qual área você deseja acessar:")
        print("1 - Clientes")
        print("2 - Administradores")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                from view.cliente_view import ClienteView
                cliente_view = ClienteView()
                cliente_view.render()
            case "2":
                from view.administrador_view import AdministradorView
                administrador_view = AdministradorView()
                administrador_view.render()
            case "0":
                print("Saindo do sistema...")
            case _:
                print("Opção inválida. Tente novamente.")

