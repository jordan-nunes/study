largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
largura_inicio = largura
altura_inicio = altura
retangulo = ''
retangulo_a = ''
retangulo_b = ''
largura_retangulo_a = largura
largura_retangulo_b = largura - 2

while altura > 0:
    while largura > 1:
        if altura == altura_inicio and largura == largura_inicio:
            while largura_retangulo_a > 0:
                retangulo_a += '#'
                largura_retangulo_a -= 1
            largura -= 1
        elif largura < largura_inicio:
            retangulo_b += '#'
            while largura_retangulo_b > 0:
                retangulo_b += ' '
                largura_retangulo_b -= 1
            retangulo_b += '#'
            largura = 0
    if altura == altura_inicio and altura != 1:
        retangulo += retangulo_a + '\n'
        altura -= 1
    elif altura > 1 and altura < altura_inicio:
        retangulo += retangulo_b + '\n'
        altura -= 1
    elif altura == 1 and largura_inicio != 1:
        retangulo += retangulo_a
        altura -= 1
    elif altura == 1 and largura_inicio == 1:
        retangulo += '#'
        altura = 0
print(retangulo)