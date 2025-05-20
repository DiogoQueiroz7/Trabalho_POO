from repository.session_repository import SessionRepository

class SessionController:
    def login(self, email, password):
        session_repository = SessionRepository()
        user = session_repository.verficar_login(email, password)

        if not user:
            return None

        user_id = user[0]
        session = session_repository.login(user_id)
        return session

    def delete_session(self, session_id):
        session_repository = SessionRepository()
        session_repository.delete_session(session_id)
        return True
