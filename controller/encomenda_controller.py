from repository.encomenda_repository import EncomendaRepository
from model.encomenda import Encomenda
from controller.session_controller import SessionController
from repository.cliente_repository import ClienteRepository

class EncomendaController:
    def __init__(self):
        self.encomenda_repository = EncomendaRepository()

    def create_encomenda(self, descricao, peso, volume, transportadora_id):
        session_controller = SessionController()
        session = session_controller.get_session()

        if not session:
            raise Exception("Usuário não está logado.")
        cliente_repository = ClienteRepository()
        cliente_id = cliente_repository.buscar_por_user_id(session['user_id'])["id"]
        encomenda = Encomenda(
            descricao=descricao,
            peso=peso,
            volume=volume,
            cliente_id=cliente_id,
            transportadora_id=transportadora_id
        )
        return self.encomenda_repository.create(encomenda)

    def get_all_encomendas(self):
        return self.encomenda_repository.get_all()
    
    def get_all_encomendas_cliente(self, user_id):
        return self.encomenda_repository.get_all_cliente(user_id)
