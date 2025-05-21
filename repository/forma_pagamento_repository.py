from db import conn
from model.forma_pagamento import FormaPagamento, Pix, CartaoCredito, Boleto
from datetime import datetime

class FormaPagamentoRepository:
    def salvar(self, forma_pagamento: FormaPagamento): 

        banco = conn()
        cursor = banco.cursor()

        tipo = forma_pagamento.tipo
        data_cadastro_obj = forma_pagamento.data_cadastro 

        if isinstance(data_cadastro_obj, str):
            print(f"Alerta: data_cadastro_obj é uma string ('{data_cadastro_obj}') no repositório. Espera-se datetime.")
            data_cadastro_obj = datetime.now() 
        elif not isinstance(data_cadastro_obj, datetime):
            print(f"Alerta: data_cadastro com tipo inesperado ('{type(data_cadastro_obj)}'). Usando data atual para o repositório.")
            data_cadastro_obj = datetime.now()
        
        data_cadastro_str = data_cadastro_obj.isoformat()


        chave_pix = None
        ultimos_digitos_cartao = None
        nome_titular_cartao = None
        data_validade_cartao = None
        codigo_barras_boleto = None

        detalhes = forma_pagamento.obter_detalhes_para_salvar() 

        if isinstance(forma_pagamento, Pix): 
            chave_pix = detalhes.get("chave_pix")
        elif isinstance(forma_pagamento, CartaoCredito): 
            ultimos_digitos_cartao = detalhes.get("ultimos_digitos")
            nome_titular_cartao = detalhes.get("nome_titular")
            data_validade_cartao = detalhes.get("data_validade_cartao")
        elif isinstance(forma_pagamento, Boleto): 
            codigo_barras_boleto = detalhes.get("codigo_barras")

        sql = """
            INSERT INTO forma_pagamento
                (tipo, data_cadastro, chave_pix, ultimos_digitos_cartao,
                 nome_titular_cartao, data_validade_cartao, codigo_barras_boleto)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (
            tipo, data_cadastro_str, chave_pix, ultimos_digitos_cartao,
            nome_titular_cartao, data_validade_cartao, codigo_barras_boleto
        ))
        banco.commit()
        id_gerado = cursor.lastrowid
        forma_pagamento.id_forma_pagamento = id_gerado 
        
        banco.close() 
        return id_gerado


    def listar(self): 

        banco = conn()
        cursor = banco.cursor()
        lista_de_formas_pagamento = []

        cursor.execute("SELECT * FROM forma_pagamento")
        registros = cursor.fetchall()

        for registro in registros:
            id_fp = registro["id"]
            tipo_fp = registro["tipo"]
            data_cadastro_fp_str = registro["data_cadastro"]

            data_cadastro_fp = datetime.fromisoformat(data_cadastro_fp_str) if data_cadastro_fp_str else datetime.now()


            if tipo_fp == "Pix":
                forma = Pix(id_forma_pagamento=id_fp, chave_pix=registro["chave_pix"], data_cadastro=data_cadastro_fp) 
            elif tipo_fp == "CartaoCredito":
                forma = CartaoCredito( 
                    id_forma_pagamento=id_fp,
                    numero_cartao="**** **** **** " + (registro["ultimos_digitos_cartao"] or "****"),
                    nome_titular=registro["nome_titular_cartao"],
                    data_validade=registro["data_validade_cartao"],
                    codigo_seguranca="***",
                    data_cadastro=data_cadastro_fp
                )
            elif tipo_fp == "Boleto":
                forma = Boleto(id_forma_pagamento=id_fp, codigo_barras=registro["codigo_barras_boleto"], data_cadastro=data_cadastro_fp) #
            else:
                print(f"Atenção: Tipo '{tipo_fp}' não é conhecido. Criando como FormaPagamento genérica.")
                forma = FormaPagamento(id_forma_pagamento=id_fp, tipo=tipo_fp, data_cadastro=data_cadastro_fp) #

            lista_de_formas_pagamento.append(forma)
        
        banco.close() 
        return lista_de_formas_pagamento



    def buscar_por_id(self, id_para_buscar: int): 
        banco = conn()
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM forma_pagamento WHERE id = ?", (id_para_buscar,))
        registro = cursor.fetchone()
        
        forma_encontrada = None 
        if registro:
            id_fp = registro["id"]
            tipo_fp = registro["tipo"]
            data_cadastro_fp_str = registro["data_cadastro"]
            data_cadastro_fp = datetime.fromisoformat(data_cadastro_fp_str) if data_cadastro_fp_str else datetime.now()

            if tipo_fp == "Pix":
                forma_encontrada = Pix(id_forma_pagamento=id_fp, chave_pix=registro["chave_pix"], data_cadastro=data_cadastro_fp) #
            elif tipo_fp == "CartaoCredito":
                forma_encontrada = CartaoCredito( 
                    id_forma_pagamento=id_fp,
                    numero_cartao="**** **** **** " + (registro["ultimos_digitos_cartao"] or "****"),
                    nome_titular=registro["nome_titular_cartao"],
                    data_validade=registro["data_validade_cartao"],
                    codigo_seguranca="***",
                    data_cadastro=data_cadastro_fp
                )
            elif tipo_fp == "Boleto":
                forma_encontrada = Boleto(id_forma_pagamento=id_fp, codigo_barras=registro["codigo_barras_boleto"], data_cadastro=data_cadastro_fp) 
            else:
                print(f"Atenção: Tipo '{tipo_fp}' não é conhecido. Retornando como FormaPagamento genérica.")
                forma_encontrada = FormaPagamento(id_forma_pagamento=id_fp, tipo=tipo_fp, data_cadastro=data_cadastro_fp) 
        
        banco.close() 
        return forma_encontrada 