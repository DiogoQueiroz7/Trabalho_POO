from repository.session_repository import SessionRepository
from functions.utils.arquivo import ArquivoUtils

class SessionController:
    def login(self, email, password):
        session_repository = SessionRepository()
        user = session_repository.verficar_login(email, password)

        if not user:
            return None

        user_id = user[0]
        try:
            # Leitura do arquivo de sessão
            if ArquivoUtils().lerArquivoSessao():
                return True

            session = session_repository.login(user_id)
            if session:
                ArquivoUtils().criarArquivoSessao(session)
                return True
            return True
        except Exception as e:
            print(f"Erro ao criar sessão: {e}")
            return False

    def delete_session(self, session_id):
        session_repository = SessionRepository()
        session_repository.delete_session(session_id)
        return True
    
    def get_session(self):
        token = ArquivoUtils().retornarTokenArquivo()
        if not token:
            return None
        session_repository = SessionRepository()
        session = session_repository.get_session(token)
        return session
