import pandas as pd

class Indicadores:

    def __init__(self):
        self.dados_df = pd.read_csv(r'dados.csv', encoding='latin1')


    def mais_frequente_nome(self, coluna_selecionada):
        mais_frequente = self.dados_df[coluna_selecionada].value_counts()
        return mais_frequente.idxmax()
        #Dúvida: Devo dar "return" só da variável                  ou da variável com funções tipo .idmax() etc

    def mais_frequente_valor(self, coluna_selecionada):
        mais_frequente = self.dados_df[coluna_selecionada].value_counts()
        return mais_frequente.max()

    def mais_frequente_linha(self, coluna_selecionada):
        mais_frequente = self.dados_df[coluna_selecionada].value_counts()
        mais_frequente_nome = mais_frequente.idxmax()
        mais_frequente_valor = mais_frequente.max()
        mais_frequente_linha = pd.Series([mais_frequente_nome, mais_frequente_valor], index=[coluna_selecionada, 'Frequência'])
        return mais_frequente_linha
        #Dúvida: Nesse caso deveria utilizar ARGS?

    #def menos_frequente...

    def maior_bruto(self, coluna_selecionada):
        maior_bruto = self.dados_df[coluna_selecionada]
        return maior_bruto.max()
    
    #def maior_bruto...

    def media_bruto(self, coluna_selecionada):
        media_bruto = self.dados_df[coluna_selecionada]
        return media_bruto.mean()
    
    #...

    def menor_bruto(self, coluna_selecionada):
        menor_bruto = self.dados_df[coluna_selecionada]
        return menor_bruto.min()

    #...

    def maior_soma(self, coluna_selecionada):
        maior_soma = self.dados_df.groupby(coluna_selecionada).sum()
        return maior_soma.max()
    
    def media_soma(self, coluna_selecionada):
        media_soma = self.dados_df.groupby(coluna_selecionada).sum()
        return media_soma.mean()

    def menor_soma(self, coluna_selecionada):
        menor_soma = self.dados_df.groupby(coluna_selecionada).sum()
        return menor_soma.min()



class DadosCliente(Indicadores):

    def __init__(self):
        cliente_quantidade = self.mais_frequente(self.dados_df["Costumer ID"])

    def cliente_comprador(self):
        pass

    def ofertar_fidelidade(self, cliente_quantidade):
        pass

class DadosProduto(Indicadores):

    def __init__(self):
        produto_quantidade = self.mais_frequente(self.dados_df["Product ID"])
        pass

class DadosLoja(Indicadores):

    def __init__(self):
        loja_quantidade = self.mais_frequente(self.dados_df["Postal Code"])
        pass



class AcoesProduto(DadosCliente):

    def __init__(self):
        pass

class AcoesProduto(DadosProduto):

    def __init__(self):
        pass

class AcoesLoja(DadosLoja):
    
    def __init__(self):
        pass