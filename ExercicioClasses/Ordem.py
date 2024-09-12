from Dado import Dado
from Dado_Geral import Dado_Geral
from datetime import datetime

class Ordem(Dado):
    """
    Classe para representar os dados e métodos de uma ordem de compra

    Atributos:
        id (str): ID único da ordem
        purchase_timestamp (datetime): Data da hora da compra (YY/MM/DD/HH:MM:SS)
        approved_at (datetime): Data em que foi aprovada a compra (YY/MM/DD/HH:MM:SS)
    """

    def __init__(self, id=str, order_purchase_timestamp=datetime, order_approved_at=datetime):
        super().__init__(id)
        self.order_purchase_timestamp = Dado_Geral(order_purchase_timestamp)
        self.order_approved_at = Dado_Geral(order_approved_at)

    def exibir_dados(self):
        print(self.id, self.order_purchase_timestamp, self.order_approved_at)
    
    def verificar_vazio(self):
        #TODO: implementar
        pass