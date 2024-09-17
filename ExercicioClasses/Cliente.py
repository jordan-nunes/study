from Dado_Geral import Dado_Geral
from Dado import Dado
import requests

class Cliente(Dado):
    """
    Classe para representar os dados e métodos de um cliente
    
    Atributos
        customer_id (str): ID único do cliente
        customer_zip_code_prefix (int): ZIP code do cliente
        customer_city (str): Cidade do cliente
        customer_state (str): Estado do cliente
    """

    def __init__(self, dados_gerais):
        self.dados_gerais = dados_gerais

    @property
    def customer_id(self):
        return self.dados_gerais.customer_id
    
    @property
    def customer_zip_code_prefix(self):
        return self.dados_gerais.customer_zip_code_prefix
    
    @property
    def customer_city(self):
        return self.dados_gerais.customer_city
    
    @property
    def customer_state(self):
        return self.dados_gerais.customer_state


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

    def pegar_dados_cep(self, cep):
        """
        Verificar se um CEP é válido

        Este método recebe um CEP, faz uma requisição à API ViaCEP e retorna um dicionário com as informações
        correspondentes ao endereço, como logradouro, bairro, cidade e estado. Se o CEP for inválido ou 
        houver um erro na requisição, retorna None.

        Parâmetros
        ----
        cep : int

        Retorna:
        ----
        dict or None

        Um dicionário com os dados do endereço se o CEP for válido, ou None se o CEP for inválido 
        ou se houver um erro na requisição.
        """
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            if 'erro' not in dados:
                return dados
            else:
                return None
        else:
            return None

    def validar_uf_cidade(self, cep, cidade, estado):
        """
        Valida se a cidade e o estado correspondem ao CEP informado.

        Este método utiliza os dados obtidos de uma consulta de CEP para verificar se a cidade (`localidade`) e 
        o estado (`uf`) retornados correspondem aos parâmetros fornecidos. A comparação é feita ignorando diferenças 
        de caixa (maiúsculas/minúsculas). Caso o CEP seja inválido ou a consulta não retorne dados, a função retorna False.

        Parâmetros
        ----------
        cep : str
            O CEP a ser consultado para validação.
        cidade : str
            A cidade a ser comparada com a localidade retornada pela consulta do CEP.
        estado : str
            O estado (UF) a ser comparado com o estado retornado pela consulta do CEP.

        Retorna
        -------
        bool
            Retorna True se a cidade e o estado coincidirem com os dados do CEP, ou False caso contrário 
            (inclusive em caso de erro na consulta do CEP).
        """
        dados = self.pegar_dados_cep(cep)
        if dados is None:
            return False
        elif str(dados['localidade']).lower() == cidade and str(dados['uf']).upper() == estado:            
            return True
        else:
            return False