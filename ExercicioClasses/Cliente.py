from Dado import Dado

class Cliente(Dado):
    """
    Classe para representar os dados de um cliente
    
    Atributos:
        id (str): ID único do cliente
        costumer_zip_code (int): ZIP code do cliente
        costumer_city (str): Cidade do cliente
        costumer_state (str): Estado do cliente
    """

    def __init__(self, id=str, customer_zip_code=int, customer_city=str, customer_state=str):
        super().__init__(id)
        self.customer_zip_code = customer_zip_code
        self.customer_city = customer_city
        self.customer_state = customer_state

    def exibir_dados(self):
        return super().exibir_dados(self.id, self.customer_zip_code, self.customer_city, self.customer_state)