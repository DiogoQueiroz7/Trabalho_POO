from controller.forma_pagamento_controller import FormaPagamentoController
from controller.pagamento_controller import PagamentoController
from controller.encomenda_controller import EncomendaController

class PagamentoView:
    def __init__(self):
        self.fp_controller = FormaPagamentoController()
        self.p_controller = PagamentoController()
        self.encomenda_controller = EncomendaController()

    def e_inteiro(self, texto): 
        if not texto:
            return False
        algarismos = "0123456789"
        for caractere in texto:
            if caractere not in algarismos:
                return False
        return True

    def e_float(self, texto): 
        if not texto:
            return False
        algarismos = "0123456789"
        ponto_encontrado = False
        for caractere in texto:
            if caractere in algarismos:
                continue
            elif caractere == '.':
                if ponto_encontrado:
                    return False 
                ponto_encontrado = True
            else:
                return False 
        return True

    def menu_principal_pagamentos(self):
        while True:
            print("\n==== Menu Pagamentos SpeedBox ====")
            print("1. Adicionar Forma de Pagamento")
            print("2. Listar Formas de Pagamento")
            print("3. Criar Pagamento")
            print("4. Listar Pagamentos")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.adicionar_forma_pagamento_menu()
            elif opcao == "2":
                print("\nListando Formas de Pagamento...")
                formas = self.fp_controller.listar_todas_formas_pagamento()
                if formas:
                    for fp in formas:
                        detalhes = f"  ID: {fp['id']}, Tipo: {fp['tipo']}"
                        
                        if fp['tipo'] == 'Pix':
                            chave = fp['chave_pix'] if fp['chave_pix'] else "Não informado"
                            detalhes += f", Chave: {chave}"
                        elif fp['tipo'] == 'CartaoCredito':
                            final_cartao = fp['ultimos_digitos_cartao'] if fp['ultimos_digitos_cartao'] else "Não informado"
                            detalhes += f", Final do Cartão: {final_cartao}"
                        elif fp['tipo'] == 'Boleto':
                            codigo = fp['codigo_barras_boleto']
                            display_codigo = "Não informado"
                            if codigo:
                                display_codigo = codigo[:20] + '...' if len(codigo) > 20 else codigo
                            detalhes += f", Cód. Barras: {display_codigo}"
                        
                        print(detalhes)
                else:
                    print("Nenhuma forma de pagamento encontrada.")
            elif opcao == "3":
                 self.criar_pagamento() 
            elif opcao == "4":
                print("\nListando Todos os Pagamentos...")
                pagamentos = self.p_controller.listar_todos_os_pagamentos()
                if pagamentos:
                    for p in pagamentos:
                        print(f"  ID: {p['id']}, Valor: R${p['valor']:.2f}, Status: {p['status']}, Enc. ID: {p['encomenda_id']}")
                else:
                    print("Nenhum pagamento encontrado.")
            elif opcao == "0":
                print("Saindo do menu de pagamentos...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def adicionar_forma_pagamento_menu(self):
        print("\n--- Adicionar Forma de Pagamento ---")
        print("1. PIX")
        print("2. Cartão de Crédito")
        print("3. Boleto")
        tipo = input("Escolha o tipo: ")

        if tipo == "1":
            chave = input("Chave PIX: ")
            self.fp_controller.criar_pix(chave)
        elif tipo == "2":
            num = input("Número do Cartão: ")
            titular = input("Nome do Titular: ")
            val = input("Validade (MM/AA): ")
            cvv = input("CVV: ")
            self.fp_controller.criar_cartao_credito(num, titular, val, cvv)
        elif tipo == "3":
            cod = input("Código de Barras: ")
            self.fp_controller.criar_boleto(cod)
        else:
            print("Tipo inválido.")

    def criar_pagamento(self): 
        print("\nCriando Novo Pagamento...")
        print("\n--- Encomendas Disponíveis ---")
        encomendas_disponiveis = self.encomenda_controller.get_all_encomendas()
        if not encomendas_disponiveis:
            print("Nenhuma encomenda disponível para pagamento. Crie uma encomenda primeiro.")
            return
        for enc in encomendas_disponiveis:
            print(f"ID: {enc['id']}, Descrição: {enc['descricao']}")
        print("\n--- Formas de Pagamento Disponíveis ---")
        formas_pgto_disponiveis = self.fp_controller.listar_todas_formas_pagamento()
        if not formas_pgto_disponiveis:
            print("Nenhuma forma de pagamento cadastrada. Cadastre uma forma de pagamento primeiro.")
            return
        for fp in formas_pgto_disponiveis:
            detalhes_fp = f"  ID: {fp['id']}, Tipo: {fp['tipo']}"
            if fp['tipo'] == 'Pix':
                chave = fp['chave_pix'] if fp['chave_pix'] else "Não informado"
                detalhes_fp += f", Chave: {chave}"
            elif fp['tipo'] == 'CartaoCredito':
                final_cartao = fp['ultimos_digitos_cartao'] if fp['ultimos_digitos_cartao'] else "Não informado"
                detalhes_fp += f", Final do Cartão: {final_cartao}"
            elif fp['tipo'] == 'Boleto':
                codigo = fp['codigo_barras_boleto']
                display_codigo = "Não informado"
                if codigo:
                    display_codigo = codigo[:20] + '...' if len(codigo) > 20 else codigo
                detalhes_fp += f", Cód. Barras: {display_codigo}"
            print(detalhes_fp)
        
        val_str = input("Valor (ex: 50.99): R$")
        enc_id_str = input("Digite o ID da Encomenda para este pagamento: ") 
        fp_id_str = input("ID da Forma de Pagamento: ")

        valido_input_basico = True
        if not self.e_inteiro(enc_id_str):
            print("Erro de Formato: ID da encomenda deve ser um número inteiro.")
            valido_input_basico = False
        
        if not self.e_inteiro(fp_id_str):
            print("Erro de Formato: ID da forma de pagamento deve ser um número inteiro.")
            valido_input_basico = False

        if not self.e_float(val_str):
            print("Erro de Formato: O valor do pagamento deve ser um número válido.")
            valido_input_basico = False
        
        if not valido_input_basico:
            return 

        val = float(val_str)
        enc_id = int(enc_id_str)
        fp_id = int(fp_id_str)

        if val <= 0:
            print("Erro: O valor do pagamento deve ser maior que zero.")
            return
        encomenda_existente = self.encomenda_controller.get_encomenda_by_id(enc_id)
        if not encomenda_existente:
            print(f"Erro: Encomenda com ID {enc_id} não encontrada. Por favor, verifique o ID e tente novamente.")
            return
        
        forma_pagamento_existente = self.fp_controller.get_forma_pagamento_by_id(fp_id)
        if not forma_pagamento_existente:
            print(f"Erro: Forma de Pagamento com ID {fp_id} não encontrada. Por favor, verifique o ID e tente novamente.")
            return
        
        self.p_controller.criar_pagamento(val, enc_id, fp_id)


if __name__ == "__main__":
    try:
        import db
        db.init()
        print("Banco de dados inicializado/verificado com sucesso.")
    except Exception as e:
        print(f"ATENÇÃO: Erro ao inicializar o banco de dados: {e}")
        print("As tabelas podem não existir. Verifique o arquivo db.py e sua execução.")

    view = PagamentoView()
    view.menu_principal_pagamentos() 