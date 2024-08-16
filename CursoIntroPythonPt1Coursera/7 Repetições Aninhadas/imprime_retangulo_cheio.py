largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
retangulo = ''
largura_retangulo = '#'
while altura > 0:
    while largura > 1:
        largura_retangulo += '#'
        largura -= 1
    if altura > 1:
        retangulo += largura_retangulo + '\n'
        altura -= 1
    else:
        retangulo += largura_retangulo
        altura -= 1
print(retangulo)