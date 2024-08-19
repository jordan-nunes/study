from abc import ABC, abstractmethod

class Dado(ABC):
    """
    Classe abstrata base para os dados que vêm do Banco de Dados

    Atributos:
        #TODO: definir os atributos
    """
    def __init__(self, id = str):
        self.id = id

    def exibir_dados(self, *args):
        string_dados = ' '.join(map(str, args))
        print(string_dados)