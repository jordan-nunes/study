from Dado import Dado
from Cliente import Cliente
from datetime import datetime

class Ordem(Dado):
    """
    Classe para representar os dados de uma ordem de compra

    Atributos:
        id (str): ID único da ordem
        costumer_id (str): ID único do cliente que solicitou a ordem
        purchase_timestamp (datetime): Data da hora da compra (YY/MM/DD/HH:MM:SS)
        approved_at (datetime): Data em que foi aprovada a compra (YY/MM/DD/HH:MM:SS)
    """

    def __init__(self, id=str, costumer_id=str, purchase_timestamp=datetime, approved_at=datetime):
        super().__init__(id)
        self.costumer_id = costumer_id
        #Dúvida: o id do cliente tá no init, como que eu peego?
        self.purchase_timestamp = purchase_timestamp
        self.approved_at = approved_at

    def exibir_dados(self):
        return super().exibir_dados(self.costumer_id, self.purchase_timestamp, self.approved_at)