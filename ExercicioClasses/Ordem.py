from Dado import Dado
from Dado_Geral import Dado_Geral


class Ordem(Dado):
    """
    Classe para representar os dados e métodos de uma ordem de compra

    Atributos
        order_id (str): ID único da ordem
        order_purchase_timestamp (datetime): Data da hora da compra (YY/MM/DD/HH:MM:SS)
        order_approved_at (datetime): Data em que foi aprovada a compra (YY/MM/DD/HH:MM:SS)
    """

    def __init__(self, dados_gerais):
        self.dados_gerais = dados_gerais

    @property
    def order_id(self):
        return self.dados_gerais.order_id
    
    @property
    def order_purchase_timestamp(self):
        return self.dados_gerais.order_purchase_timestamp
    
    @property
    def order_approved_at(self):
        return self.dados_gerais.order_approved_at


    def exibir_dados(self):
        dict_dados = Dado_Geral.dados_para_dict(self)
        for atributo, valor in dict_dados.items():
            print(f"{atributo}: {valor}")
    
    def verificar_vazio(self):
        dict_dados = Dado_Geral.dados_para_dict(self)
        for atributo, valor in dict_dados.items():
                if valor is None or not valor:
                    return False
        return True
    
    def delay_aprovacao(self, horario_inicio, horario_fim):
        """
        Calcula o tempo de atraso entre a submissão e a aprovação de uma ação.

        Este método calcula a diferença entre dois horários, representando o tempo entre o início e o fim de um 
        processo de aprovação.

        Parâmetros
        ----------
        horario_inicio : datetime
            O horário de início do processo.
        horario_fim : datetime
            O horário de término ou aprovação do processo.

        Retorna
        -------
        timedelta
            A diferença de tempo entre o horário de início e o horário de fim, representada como um objeto `timedelta`.
        """
        tempo_aprovacao = horario_fim - horario_inicio
        return tempo_aprovacao