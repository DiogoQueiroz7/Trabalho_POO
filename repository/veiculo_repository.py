from db import conn

class VeiculoRepository:
    def salvar(self, veiculo):
        with conn() as c:
            cursor = c.cursor()
            cursor.execute("""
                INSERT INTO veiculos (placa, cor, tipo_veiculo_id, cliente_id)
                VALUES (?, ?, ?, ?)
            """, (veiculo.placa, veiculo.cor, veiculo.tipo_veiculo_id, veiculo.cliente_id))
            veiculo.id = cursor.lastrowid
        return veiculo.id

    def listar(self):
        with conn() as c:
            cursor = c.cursor()
            cursor.execute("SELECT * FROM veiculos")
            return cursor.fetchall()

    def buscar_ou_criar_tipo(self, nome):
        with conn() as c:
            cursor = c.cursor()
            cursor.execute("SELECT id FROM tipos_veiculos WHERE nome = ?", (nome,))
            row = cursor.fetchone()
            if row:
                return row['id']
            cursor.execute("INSERT INTO tipos_veiculos (nome) VALUES (?)", (nome,))
            return cursor.lastrowid

    def salvar_moto(self, veiculo_id, adequecao, agilidade, cilindrada, carga):
        with conn() as c:
            c.execute("""
                INSERT INTO moto (adequecaoUrbana, agilidade, cilindrada, capacidadeCarga, tipo_veiculo_id)
                VALUES (?, ?, ?, ?, ?)
            """, (adequecao, agilidade, cilindrada, carga, veiculo_id))

    def salvar_carro(self, veiculo_id, adequecao, agilidade, modelo, carga):
        with conn() as c:
            c.execute("""
                INSERT INTO carro (adequecaoUrbana, agilidade, modelo, capacidadeCarga, tipo_veiculo_id)
                VALUES (?, ?, ?, ?, ?)
            """, (adequecao, agilidade, modelo, carga, veiculo_id))