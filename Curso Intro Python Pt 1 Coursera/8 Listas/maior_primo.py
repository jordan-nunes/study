#primeiro eu vou testar se o número em si é primo
#depois se x numero antes dele é primo
#o primeiro x numero primo antes dele eu retorno


def primo(numero_primo):
    if numero_primo >= 2:
        anterior = numero_primo - 1
        isprimo = True
        while isprimo == True and anterior > 1:
            if numero_primo % anterior != 0:
                anterior -= 1
            else:
                isprimo = False
        if isprimo == True:
            return (isprimo)
        else:
            return (isprimo)
    #aqui ele testa se o número em si é primo, se for ele retorna True


def maior_primo(y):
	if primo(y) == True:
		return(y)
	else:	
		while primo(y) == False:
			y -= 1
		return (y)


print(maior_primo(88))
