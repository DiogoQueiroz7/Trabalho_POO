from controller.forma_pagamento_controller import FormaPagamentoController 
from controller.pagamento_controller import PagamentoController 
from model.forma_pagamento import Pix, CartaoCredito, Boleto 
from model.pagamento import Pagamento 
from datetime import datetime

class PagamentoView:
    def __init__(self):
        self.fp_controller = FormaPagamentoController() 
        self.p_controller = PagamentoController() 

    def menu_principal_pagamentos(self):
        while True:
            print("\n==== Menu Pagamentos SpeedBox ====")
            print("1. Gerenciar Formas de Pagamento")
            print("2. Gerenciar Pagamentos")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.menu_formas_de_pagamento_interno()
            elif opcao == "2":
                self.menu_pagamentos_interno()
            elif opcao == "0":
                print("Saindo do menu de pagamentos...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_formas_de_pagamento_interno(self):
        while True:
            print("\n--- Submenu: Formas de Pagamento ---")
            print("1. Adicionar PIX")
            print("2. Adicionar Cartão de Crédito")
            print("3. Adicionar Boleto")
            print("4. Listar Todas")
            print("5. Buscar por ID")
            print("0. Voltar ao Menu Anterior")

            opcao = input("Escolha: ")

            if opcao == "1":
                print("\nAdicionando PIX...")
                chave = input("Chave PIX: ")
                self.fp_controller.criar_pix(chave) 
            elif opcao == "2":
                print("\nAdicionando Cartão de Crédito...")
                num = input("Número do Cartão: ")
                titular = input("Nome do Titular: ")
                val = input("Validade (MM/AA): ")
                cvv = input("CVV: ")
                self.fp_controller.criar_cartao_credito(num, titular, val, cvv) 
            elif opcao == "3":
                print("\nAdicionando Boleto...")
                cod = input("Código de Barras: ")
                self.fp_controller.criar_boleto(cod) 
            elif opcao == "4":
                print("\nListando Formas de Pagamento...")
                formas = self.fp_controller.listar_todas_formas_pagamento() 
                if formas:
                    for fp in formas:
                        detalhes_str = ""
                        if isinstance(fp, Pix): 
                            detalhes_str = f"Chave: {fp.chave_pix}" 
                        elif isinstance(fp, CartaoCredito): 
                            detalhes_str = f"Final: {fp.ultimos_digitos}, Titular: {fp.nome_titular}" 
                        elif isinstance(fp, Boleto): 
                            detalhes_str = f"Cód. Barras: {fp.codigo_barras[:15]}..." if fp.codigo_barras else "N/A" 
                        print(f"  ID: {fp.id_forma_pagamento}, Tipo: {fp.tipo}, Detalhes: {detalhes_str}") 
            elif opcao == "5":
                id_fp_str = input("ID da Forma de Pagamento para buscar: ")
                id_fp = int(id_fp_str) 
                fp = self.fp_controller.buscar_forma_pagamento_por_id(id_fp) 
                if fp:
                    print(f"  Encontrado: ID: {fp.id_forma_pagamento}, Tipo: {fp.tipo}") 
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def menu_pagamentos_interno(self):
        while True:
            print("\n--- Submenu: Pagamentos ---")
            print("1. Criar Novo Pagamento")
            print("2. Listar Todos")
            print("3. Consultar por ID")
            print("4. Confirmar Pagamento")
            print("5. Cancelar Pagamento")
            print("6. Marcar como Falho")
            print("0. Voltar ao Menu Anterior")

            opcao = input("Escolha: ")

            if opcao == "1":
                print("\nCriando Novo Pagamento...")
                val_str = input("Valor (ex: 50.99): R$")
                val = float(val_str) 

                enc_id_str = input("ID da Encomenda: ")
                enc_id = int(enc_id_str) 

                if val <= 0 or enc_id <= 0:
                    print("Erro: Valor e ID da encomenda devem ser positivos.")
                    continue 

                print("Formas de Pagamento disponíveis:")
                formas_disponiveis = self.fp_controller.listar_todas_formas_pagamento() #
                if not formas_disponiveis:
                    print("Nenhuma forma de pagamento cadastrada. Crie uma primeiro.")
                    continue

                for fp_item in formas_disponiveis:
                     print(f"  ID: {fp_item.id_forma_pagamento} - Tipo: {fp_item.tipo}") #

                fp_id_str = input("ID da Forma de Pagamento: ")
                fp_id = int(fp_id_str) 

                if fp_id <= 0:
                    print("Erro: ID da forma de pagamento deve ser positivo.")
                    continue

                self.p_controller.criar_pagamento(val, enc_id, fp_id) 

            elif opcao == "2":
                print("\nListando Todos os Pagamentos...")
                pagamentos = self.p_controller.listar_todos_os_pagamentos() 
                if pagamentos:
                    for p in pagamentos:
                        data_str = p.data_pagamento.strftime('%d/%m/%Y %H:%M') if p.data_pagamento else "N/A" 
                        print(f"  ID: {p.id_pagamento}, Valor: R${p.valor:.2f}, Status: {p.status_pagamento}, Data: {data_str}, Enc. ID: {p.encomenda_id}") 
            elif opcao == "3":
                id_p_str = input("ID do Pagamento para consultar: ")
                id_p = int(id_p_str) 
                p = self.p_controller.consultar_pagamento_por_id(id_p) 
                if p:
                    print(f"  Encontrado: ID: {p.id_pagamento}, Valor: R${p.valor:.2f}, Status: {p.status_pagamento}") 
            elif opcao == "4":
                id_conf_str = input("ID do Pagamento para CONFIRMAR: ")
                id_conf = int(id_conf_str) 
                self.p_controller.confirmar_pagamento(id_conf) 
            elif opcao == "5":
                id_canc_str = input("ID do Pagamento para CANCELAR: ")
                id_canc = int(id_canc_str) 
                self.p_controller.cancelar_pagamento(id_canc) 
            elif opcao == "6":
                id_fail_str = input("ID do Pagamento para marcar como FALHO: ")
                id_fail = int(id_fail_str) 
                self.p_controller.marcar_pagamento_como_falho(id_fail) 
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

if __name__ == "__main__":

    import db 
    try:
        db.init() 
        print("Banco de dados inicializado/verificado com sucesso.")
    except Exception as e:
        print(f"ATENÇÃO: Erro ao inicializar o banco de dados: {e}")
        print("As tabelas podem não existir. Verifique o arquivo db.py e sua execução.")

    view_teste = PagamentoView()
    view_teste.menu_principal_pagamentos()