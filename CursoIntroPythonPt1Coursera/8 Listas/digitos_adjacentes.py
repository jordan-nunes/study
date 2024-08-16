numero = int(input("Digite um número inteiro: "))
numerolen = numero
numeroab = numero
numeroa = 0
numerob = 0
iguais = False
i = 1 

while (numerolen // 10 != 0):	
	numerolen = numerolen // 10
	i += 1

while (i > 0 and iguais == False):
	numeroab = numero % 100
	numeroa = numeroab % 10
	numerob = numeroab // 10
	if(numeroa == numerob):
		print("sim")
		iguais = True		
	else:
		i -= 1
		numero = numero // 10
if (iguais == False):
	print("não")
