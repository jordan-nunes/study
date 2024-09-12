from datetime import datetime

class Dado_Geral:
    """
    Classe genérica que engloba todos os dados e seus respectivos tipos

    Atributos:
        customer_id (str): ID único do cliente
        customer_zip_code (int): ZIP code do cliente
        customer_city (str): Cidade do cliente
        customer_state (str): Estado do cliente
        order_id (str): ID único da ordem
        order_purchase_timestamp (datetime): Data da hora da ordem (YY/MM/DD/HH:MM:SS)
        order_approved_at (datetime): Data em que foi aprovada a ordem (YY/MM/DD/HH:MM:SS)
        product_id (str): ID único do produto
        product_category_name (str): Categoria do produto
        product_weight (float): Peso do produto em gramas (g)
        product_length (float): Comprimento do produto em centímetros (cm)
        product_height (float): Altura do produto em centímetros (cm)
        product_width (float): Largura do produto em centímetros (cm)
    """

    def __init__(self, customer_id=str, customer_zip_code_prefix=int, customer_city=str, customer_state=str, order_id=str, order_purchase_timestamp=datetime, order_approved_at=datetime, product_id=str, product_category_name=str, product_weight_g=float, product_length_cm=float, product_height_cm=float, product_width_cm=float):
        self.customer_id = customer_id
        self.customer_zip_code_prefix = customer_zip_code_prefix
        self.customer_city = customer_city
        self.customer_state = customer_state
        self.order_id = order_id
        self.order_purchase_timestamp = order_purchase_timestamp
        self.order_approved_at = order_approved_at
        self.product_id = product_id
        self.product_category_name = product_category_name
        self.product_weight_g = product_weight_g
        self.product_length_cm = product_length_cm
        self.product_height_cm = product_height_cm
        self.product_width_cm = product_width_cm