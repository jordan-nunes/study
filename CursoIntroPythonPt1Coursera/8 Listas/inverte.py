def invert(lista):
    lista2 = []
    for x in range(len(lista)):
        lista2.append(lista[-1-x])
    return lista2

numero = int
lista = []
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero != 0:
        lista.append(numero)
lista = invert(lista[:])
for x in lista:
    print(x)