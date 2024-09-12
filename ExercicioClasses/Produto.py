from Dado import Dado
from Dado_Geral import Dado_Geral

class Produto(Dado):
    """
    Classe para representar os dados e métodos de um produto

    Atributos:
        id (str): ID único do produto
        product_category_name (str): Categoria do produto
        product_weight (float): Peso do produto em gramas (g)
        product_length (float): Comprimento do produto em centímetros (cm)
        product_height (float): Altura do produto em centímetros (cm)
        product_width (float): Largura do produto em centímetros (cm)
    """

    def __init__(self, id=str, product_category_name=str, product_weight_g=float, product_length_cm=float, product_height_cm=float, product_width_cm=float):
        super().__init__(id)
        self.product_category_name = Dado_Geral(product_category_name)
        self.product_weight_g = Dado_Geral(product_weight_g)
        self.product_length_cm = Dado_Geral(product_length_cm)
        self.product_height_cm = Dado_Geral(product_height_cm)
        self.product_width_cm = Dado_Geral(product_width_cm)

    def exibir_dados(self):
        self.exibir_dados(self.id, self.product_category_name, self.product_weight_g, self.product_length_cm, self.product_height_cm, self.product_width_cm)
    
    def verificar_vazio(self):
        #TODO: implementar função que retornará verdadeiro ou falso se houver células com dados vazios
        pass