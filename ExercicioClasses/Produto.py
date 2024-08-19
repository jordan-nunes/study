from Dado import Dado

class Produto(Dado):
    """
    Classe para representar os dados de um produto

    Atributos:
        id (str): ID único do produto
        product_category (str): Categoria do produto
        product_weight (float): Peso do produto em gramas (g)
        product_length (float): Comprimento do produto em centímetros (cm)
        product_height (float): Altura do produto em centímetros (cm)
        product_width (float): Largura do produto em centímetros (cm)
    """

    def __init__(self, id=str, product_category=str, product_weight_g=float, product_lenght_cm=float, product_height_cm=float, product_width_cm=float):
        super().__init__(id)
        self.product_category = product_category
        self.product_weight_g = product_weight_g
        self.product_lenght_cm = product_lenght_cm
        self.product_height_cm = product_height_cm
        self.product_width_cm = product_width_cm

    def exibir_dados(self):
        return super().exibir_dados(self.id, self.product_category, self.product_weight_g, self.product_lenght_cm, self.product_height_cm, self.product_width_cm)
