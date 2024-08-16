n = int(input("Digite um número inteiro: "))
acumulador = 0

while n > 10:
	acumulador += n % 10
	n = n // 10
acumulador += n

print(acumulador)