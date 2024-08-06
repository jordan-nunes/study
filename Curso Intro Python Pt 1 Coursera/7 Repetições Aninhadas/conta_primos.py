def n_primos(numero):
    primo = 0
    fim = False
    while fim == False:
        while numero > 0:
            isprimo = True
            contador = 1
            while contador != numero - 1 and numero != 1:
                if numero % (contador + 1) != 0:
                    contador += 1
                else:
                    contador = numero - 1 
                    isprimo = False
            if isprimo == True:
                primo += 1
            numero -= 1
        fim = True
    return primo - 1