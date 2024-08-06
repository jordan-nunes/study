import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))               # Numero de palavras diferentes
    hlr = float(input("Entre a Razão Hapax Legomana:"))             # Numero de palavras diferentes sobre numero total de palavras
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


#----------------------------------------------------------------A partir desse ponto a implementação foi feita por mim--------------------------------------------------------

def transforma_texto_em_sequencial(texto):
    texto_sequencial = re.split(r'[.?!,;: ]+', texto)
    texto_sequencial = [palavra for palavra in texto_sequencial if palavra]         # Remove espaços vazios
    '''sentencas = separa_sentencas(texto)                 # Lista de sentencas até o ( . )
    for frases in sentencas:                             
        frase = separa_frases(frases)                      # Lista de frases até ( :,; )
        for palavras in frase:                       
            palavra = separa_palavras(palavras)            # Lista de palavras até ( espaço )
            for elemento in palavra:
                texto_sequencial.append(elemento)'''

    return texto_sequencial

def calcula_wal(texto_sequencial):
    '''Essa funcao recebe um texto sequencial e retorna o tamanho médio de palavras dentro desse texto'''
    acumulador = 0
    for i, palavra in enumerate(texto_sequencial):
        acumulador += len(texto_sequencial[i])
    wal = acumulador / len(texto_sequencial)

    return wal

def calcula_ttr(texto_sequencial):
    ttr = n_palavras_diferentes(texto_sequencial) / len(texto_sequencial)

    return ttr

def calcula_hlr(texto_sequencial):
    hlr = n_palavras_unicas(texto_sequencial) / len(texto_sequencial)

    return hlr

def calcula_sal(texto):
    n_caracteres = 0
    n_sentencas = 0
    sentencas = separa_sentencas(texto)                 # Lista de sentencas até o ( . )
    for frases in sentencas:
        for caracteres in frases:                             
            n_caracteres += 1
        n_sentencas += 1
    sal = n_caracteres / n_sentencas

    return sal

def calcula_sac(texto):
    n_frases = 0
    sentencas = separa_sentencas(texto)
    for frases in sentencas:
        frase = separa_frases(frases)
        n_frases += len(frase)
    sac = n_frases / len(sentencas)

    return sac

def calcula_pal(texto):
    n_caracteres = 0
    n_frases = 0
    sentencas = separa_sentencas(texto)                 # Lista de sentencas até o ( . )
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:                             
            for caractere in frase:
                n_caracteres += 1
        n_frases += len(frases)
    pal = n_caracteres / n_frases

    return pal

def calcula_media_palavras_unicas_ou_diferentes(num_palavras_unicas):
    acumulador = 0
    for num in num_palavras_unicas:
        acumulador += num
    media = acumulador / len(num_palavras_unicas)

    return media

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    texto_sequencial = transforma_texto_em_sequencial(texto)
    wal = calcula_wal(texto_sequencial)
    ttr = calcula_ttr(texto_sequencial)
    hlr = calcula_hlr(texto_sequencial)
    sal = calcula_sal(texto)
    sac = calcula_sac(texto)
    pal = calcula_pal(texto)
    assinatura = [wal, ttr, hlr, sal, sac, pal]

    return assinatura

def compara_assinatura(as_a, as_b):
    assinatura = 0
    for i in range(len(as_a)):
        assinatura = assinatura + abs((as_a[i] - as_b[i]))
    assinatura = assinatura / 6

    return assinatura

def avalia_textos(textos, ass_cp):
    assinaturas = []
    comparacao = []
    ass_maior = float
    i_texto = 0
    texto_mais_parecido = 1
    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))
    for assinatura in assinaturas:
        comparacao.append(compara_assinatura(assinatura, ass_cp))
    ass_menor = comparacao[0]
    for ass_texto in comparacao:
        if ass_texto < ass_menor:
            ass_menor = ass_texto
            texto_mais_parecido = i_texto + 1
        i_texto += 1

    return texto_mais_parecido

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    texto_mais_parecido = avalia_textos(textos, ass_cp)
    print('O autor do texto', texto_mais_parecido, 'está infectado com COH-PIAH')

main()