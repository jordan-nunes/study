from Dado_Geral import Dado_Geral
from Dado import Dado

class Produto(Dado):
    """
    Classe para representar os dados e métodos de um produto

    Atributos
        order_id (str): ID único do produto
        product_category_name (str): Categoria do produto
        product_weight_g (float): Peso do produto em gramas (g)
        product_length_cm (float): Comprimento do produto em centímetros (cm)
        product_height_cm (float): Altura do produto em centímetros (cm)
        product_width_cm (float): Largura do produto em centímetros (cm)
    """

    def __init__(self, dados_gerais):
        self.dados_gerais = dados_gerais

    @property
    def product_id(self):
        return self.dados_gerais.product_id
    
    @property
    def product_category_name(self):
        return self.dados_gerais.product_category_name
    
    @property
    def product_weight_g(self):
        return self.dados_gerais.product_weight_g
    
    @property
    def product_length_cm(self):
        return self.dados_gerais.product_length_cm
    
    @property
    def product_height_cm(self):
        return self.dados_gerais.product_height_cm
    
    @property
    def product_width_cm(self):
        return self.dados_gerais.product_width_cm

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
    
    def cubagem(self, medida_1, medida_2, medida_3):
        """
        Calcula o volume cúbico a partir de três medidas.

        Este método calcula a cubagem (volume) de um objeto ou espaço tridimensional multiplicando três medidas fornecidas.

        Parâmetros
        ----------
        medida_1 : float
            A primeira medida (comprimento).
        medida_2 : float
            A segunda medida (largura).
        medida_3 : float
            A terceira medida (altura).

        Retorna
        -------
        float
            O volume resultante da multiplicação das três medidas.
        """
        return medida_1 * medida_2 * medida_3