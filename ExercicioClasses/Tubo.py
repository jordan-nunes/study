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
        """
        Separa um linha de dados do dataframe

        Este método recebe um dataframe do tipo pd.Series e retorna a última linha.

        Retorna:
        ----------
        pandas.core.frame.DataFrame
            A linha de dados do dataframe
        """
        return self.dados.iloc[-1].copy()

    def remover_dado_dataframe(self):
        """
        Este método remove a última linha de dados do dataframe

        Retorna:
        ----------
        pd.Series
            O dataframe sem a última linha
        """
        self.dados = self.dados.drop(self.dados.index[-1])
        return self.dados