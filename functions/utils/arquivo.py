import json

class ArquivoUtils:
    def criarArquivoSessao(self, conteudo=None):
        try:
            with open("session.json", "w") as arquivo:
                if conteudo is None:
                    conteudo = {"session": "vazia"}
                json.dump(conteudo, arquivo)
            print("Arquivo de sessão criado com sucesso.")
        except Exception as e:
            print(f"Erro ao criar o arquivo de sessão: {e}")
    def lerArquivoSessao(self):
        try:
            with open("session.json", "r") as arquivo:
                if(arquivo.readable()):
                    return True
                return False
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao ler arquivo de sessão: {e}")
            return False
    def retornarTokenArquivo(self):
        try:
            with open("session.json", "r") as arquivo:
                conteudo = json.load(arquivo)
                return conteudo.get("token", None)
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao ler o token do arquivo de sessão: {e}")
            return None
        
    def retornarIdUsuarioArquivo(self):
        try:
            with open("session.json", "r") as arquivo:
                conteudo = json.load(arquivo)
                return conteudo.get("", None)
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao ler o id do usuário do arquivo de sessão: {e}")
            return None