import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c
raiz1 = float
raiz2 = float

if(delta >= 0):
	if(delta == 0):
		raiz1 = ( (-1 * b) + math.sqrt(delta) )/ (2 * a)
		print("a raiz desta equação é", raiz1)
	else:
		raiz1 = ( (-1 * b) + math.sqrt(delta) ) / (2 * a)
		raiz2 = ( (-1 * b) - math.sqrt(delta) ) / (2 * a)
		if raiz1 < raiz2:
			print("as raízes da equação são", raiz1, "e", raiz2)
		else:
			print("as raízes da equação são", raiz2, "e", raiz1)

else:
	print("esta equação não possui raízes reais")
