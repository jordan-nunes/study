numero = int(input("Digite um número inteiro: "))
contador = numero
i = numero - 1
primo = True

while contador > 0:	
	if(numero == 1):
		primo = False
		contador = 0
	if(primo == True):
		if(numero != 2):
			if(i > 1 and numero % i == 0):
				print(i)
				primo = False
				contador = 0
	i -= 1	
	contador -= 1	

if primo == True:
	print("primo")
else:
	print("não é primo")
