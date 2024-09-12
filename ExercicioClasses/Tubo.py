import pandas as pd

class Tubo:
    """
    Classe para manipular os métodos da pilha

    Atributos:
        dados (pandas.Series): Dataframe de dados pandas
    """
    
    def __init__(self, dados=pd.Series):
        self.dados = dados

    def separar_dado_lifo(self):
        
        return self.dados.iloc[-1]

    def remover_dado_dataframe(self):
        return self.dados.drop(self.dados.index[-1], inplace=True)