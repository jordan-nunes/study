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

def maior_primo(y):
	if primo(y) == True:
		return(y)
	else:	
		while primo(y) == False:
			y -= 1
		return (y)