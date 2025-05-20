from db import conn
from model.forma_pagamento import FormaPagamento, Pix, CartaoCredito, Boleto #
from datetime import datetime

class FormaPagamentoRepository:
    def salvar(self, forma_pagamento: FormaPagamento) -> int | None: #
        """
        Salva uma nova forma de pagamento no banco de dados.
        Retorna o ID se salvar, ou None se der erro.
        """
        banco = conn() 
        cursor = banco.cursor()

        tipo = forma_pagamento.tipo #
        data_cadastro_obj = forma_pagamento.data_cadastro #
        if isinstance(data_cadastro_obj, str):
            try:
                data_cadastro_obj = datetime.fromisoformat(data_cadastro_obj)
            except ValueError:
                print(f"Alerta: Formato de data_cadastro string inválido ('{data_cadastro_obj}'). Usando data atual para o repositório.")
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

        detalhes = forma_pagamento.obter_detalhes_para_salvar() #

        if isinstance(forma_pagamento, Pix): #
            chave_pix = detalhes.get("chave_pix")
        elif isinstance(forma_pagamento, CartaoCredito): #
            ultimos_digitos_cartao = detalhes.get("ultimos_digitos")
            nome_titular_cartao = detalhes.get("nome_titular")
            data_validade_cartao = detalhes.get("data_validade_cartao")
        elif isinstance(forma_pagamento, Boleto): #
            codigo_barras_boleto = detalhes.get("codigo_barras")

        try:
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
            return id_gerado
        except Exception as e:
            print(f"Ops! Algum erro ocorreu ao salvar a forma de pagamento: {e}")
            banco.rollback()
            return None
        finally:
            banco.close() 

    def listar(self) -> list[FormaPagamento]: #
        """
        Pega todas as formas de pagamento do banco.
        """
        banco = conn()
        cursor = banco.cursor()
        lista_de_formas_pagamento = []

        try:
            cursor.execute("SELECT * FROM forma_pagamento")
            registros = cursor.fetchall() 

            for registro in registros:
                id_fp = registro["id"]
                tipo_fp = registro["tipo"]
                data_cadastro_fp_str = registro["data_cadastro"]
                data_cadastro_fp = datetime.fromisoformat(data_cadastro_fp_str) if data_cadastro_fp_str else datetime.now()


                if tipo_fp == "Pix":
                    forma = Pix(id_forma_pagamento=id_fp, chave_pix=registro["chave_pix"], data_cadastro=data_cadastro_fp) #
                elif tipo_fp == "CartaoCredito":
                    forma = CartaoCredito(
                        id_forma_pagamento=id_fp, 
                        numero_cartao="**** **** **** " + (registro["ultimos_digitos_cartao"] or "****"), #
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

            return lista_de_formas_pagamento
        except Exception as e:
            print(f"Ops! Algum erro ocorreu ao listar as formas de pagamento: {e}")
            return [] 
        finally:
            banco.close()

    def buscar_por_id(self, id_para_buscar: int) -> FormaPagamento | None: #
        """
        Busca uma forma de pagamento específica pelo seu ID.
        """
        banco = conn()
        cursor = banco.cursor()

        try:
            cursor.execute("SELECT * FROM forma_pagamento WHERE id = ?", (id_para_buscar,))
            registro = cursor.fetchone() 

            if registro:
                id_fp = registro["id"]
                tipo_fp = registro["tipo"]
                data_cadastro_fp_str = registro["data_cadastro"]
                data_cadastro_fp = datetime.fromisoformat(data_cadastro_fp_str) if data_cadastro_fp_str else datetime.now()

                if tipo_fp == "Pix":
                    return Pix(id_forma_pagamento=id_fp, chave_pix=registro["chave_pix"], data_cadastro=data_cadastro_fp) 
                elif tipo_fp == "CartaoCredito":
                    return CartaoCredito(
                        id_forma_pagamento=id_fp, 
                        numero_cartao="**** **** **** " + (registro["ultimos_digitos_cartao"] or "****"), 
                        nome_titular=registro["nome_titular_cartao"], 
                        data_validade=registro["data_validade_cartao"], 
                        codigo_seguranca="***",
                        data_cadastro=data_cadastro_fp
                    )
                elif tipo_fp == "Boleto":
                    return Boleto(id_forma_pagamento=id_fp, codigo_barras=registro["codigo_barras_boleto"], data_cadastro=data_cadastro_fp) 
                else:
                    print(f"Atenção: Tipo '{tipo_fp}' não é conhecido. Retornando como FormaPagamento genérica.")
                    return FormaPagamento(id_forma_pagamento=id_fp, tipo=tipo_fp, data_cadastro=data_cadastro_fp) 
            else:
                return None
        except Exception as e:
            print(f"Ops! Algum erro ocorreu ao buscar a forma de pagamento: {e}")
            return None
        finally:
            banco.close()