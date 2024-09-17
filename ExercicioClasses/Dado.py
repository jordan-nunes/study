from abc import ABC, abstractmethod

class Dado(ABC):
    """
    Classe abstrata base para os dados que vêm do Banco de Dados
    """

    def __init__(self):
        pass

    @abstractmethod
    def exibir_dados(self):
        """
        Exibe as propriedades e valores públicos do objeto.

        Este método percorre todos os atributos e propriedades públicas que não começam com um caractere de 
        sublinhado ('_') e não são métodos (funções) cujo valor seja do tipo int, str, float ou datetime. 
        Em seguida, exibe o nome e o valor de cada um desses atributos.
        """
        pass

    @abstractmethod
    def verificar_vazio(self) -> bool:
        """
        Verifica se todos os atributos e propriedades públicas do objeto estão preenchidos.

        Este método percorre todos os atributos e propriedades públicas que não começam com um caractere de 
        sublinhado ('_') e não são métodos (funções) cujo valor seja do tipo int, str, float ou datetime.
        Em seguida, retorna True se todos os atributos estão preenchidos e False caso contrário.

        Retorna
        ----
        bool: True se todos os atributos estão preenchidos, False caso contrário
        """
        pass