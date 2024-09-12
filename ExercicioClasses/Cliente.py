from Dado_Geral import Dado_Geral
from Dado import Dado

class Cliente(Dado):
    """
    Classe para representar os dados e métodos de um cliente
    
    Atributos:
        id (str): ID único do cliente
        customer_zip_code (int): ZIP code do cliente
        customer_city (str): Cidade do cliente
        customer_state (str): Estado do cliente
    """

    def __init__(self, id=str, customer_zip_code_prefix=int, customer_city=str, customer_state=str):
        super().__init__(id)
        self.customer_zip_code_prefix = Dado_Geral(customer_zip_code_prefix)
        self.customer_city = Dado_Geral(customer_city)
        self.customer_state = Dado_Geral(customer_state)

    def exibir_dados(self):
        self.exibir_dados(self.id, self.customer_zip_code_prefix, self.customer_city, self.customer_state)
    
    def verificar_vazio(self):
        #TODO: implementar função que retornará verdadeiro ou falso se houver células com dados vazios
        pass


    def validar_ZIP(self):
        #TODO: implementar função que retornará se o zip é válido para a cidade do cliente
        pass

    def localização(self):
        #TODO: implementar função que retornará todos os dados geográficos de cliente
        pass