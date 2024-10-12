from datetime import datetime
import pandas as pd
import numpy as np

class Dado_Geral:
    """

    """

    def __init__(self, 
                servico_cod=str, 
                funcionario_id=int,
                funcionario_estado_civil=str,
                funcionario_nome_completo=str,
                funcionario_salario=float,
                funcionario_imposto=float,
                funcionario_beneficios=float,
                funcionario_vt=float,
                funcionario_vr=float,
                funcionario_cargo=str,
                funcionario_area=str,
                cliente_id=int, 
                cliente_nome=str, 
                contrato_tempo=int, 
                contrato_mensalidade=int):
        self.servico_cod = servico_cod
        self.funcionario_id = funcionario_id
        self.funcionario_estado_civil = funcionario_estado_civil
        self.funcionario_nome_completo = funcionario_nome_completo
        self.funcionario_salario = funcionario_salario
        self.funcionario_imposto = funcionario_imposto
        self.funcionario_beneficios = funcionario_beneficios
        self.funcionario_cargo = funcionario_cargo
        self.funcionario_vr = funcionario_vr
        self.funcionario_area = funcionario_area
        self.funcionario_vt = funcionario_vt
        self.cliente_id = cliente_id
        self.cliente_nome = cliente_nome
        self.contrato_tempo = contrato_tempo
        self.contrato_mensalidade = contrato_mensalidade


    def dados_para_dict(self):
        """
        Converte os atributos da instância em um dicionário.

        Este método percorre todos os atributos públicos da instância que não são métodos e os adiciona a um 
        dicionário, desde que sejam do tipo `int`, `str`, `float` ou `datetime`. Atributos privados e métodos são 
        ignorados.

        Retorna
        -------
        dict
            Um dicionário contendo os atributos da instância como chaves e seus respectivos valores, 
            limitado a tipos simples (`int`, `str`, `float`, `datetime`).
        """
        dict_dados = {}
        for atributo in dir(self):
            if not atributo.startswith('_') and not callable(getattr(self, atributo)):
                valor = getattr(self, atributo)
                if isinstance(valor, (int, str, float, datetime)):
                        dict_dados.update({atributo: valor})
        return dict_dados
    
    def filtar_valor(chave):
        valores_int = ['customer_zip_code_prefix']
        valores_datetime = ['order_purchase_timestamp', 'order_approved_at']
        valores_float = ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
        if chave in valores_int:
            return int(0)
        elif chave in valores_datetime:
            data_padrao = datetime(2000, 1, 1, 0, 0, 0)
            return data_padrao.strftime('%Y-%m-%d %H:%M:%S')
        elif chave in valores_float:
            return 0.0
        else:
            return ''
    
    def substituir_valor_coluna(linha):
        for coluna, valor in linha.items():
            if (
                valor is None or
                valor == '' or
                (isinstance(valor, list) and len(valor) == 0) or
                (isinstance(valor, dict) and len(valor) == 0) or
                (isinstance(valor, np.ndarray) and valor.size == 0) or
                valor == 0 or
                valor is False or
                (isinstance(valor, float) and pd.isna(valor))
            ):
                substituicao = Dado_Geral.filtar_valor(coluna)
                linha.loc[coluna] = substituicao
                return linha
            else:
                pass
        return linha