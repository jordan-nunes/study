from abc import ABC, abstractmethod

class Dado(ABC):
    """
    Classe abstrata base para os dados que vêm do Banco de Dados
    """

    def __init__(self, id=str):
        self.id = id

    @abstractmethod
    def exibir_dados(self, *args):
        pass

    @abstractmethod
    #TODO: melhorar a implantação desse método nas classes usando vars()
    def verificar_vazio(self, *args) -> bool:
        pass