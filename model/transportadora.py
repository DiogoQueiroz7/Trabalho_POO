class Transportadora:
    def __init__(self, razao_social, cnpj, endereco):
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.endereco = endereco

    def __repr__(self):
        return f"Transportadora(nome='{self.razao_social}', cnpj='{self.cnpj}', endereco='{self.endereco}')"