from collections import namedtuple

def maior_e_menor_temperatura(lista):
    if not lista:
        return None
    
    TemperaturaInfo = namedtuple('TemperaturaInfo', ['maior', 'diamaior', 'menor', 'diamenor'])

    maior = lista[0]
    menor = lista[0]
    diamaior = 0
    diamenor = 0

    for i, num in enumerate(lista):
        if num >= maior:
            maior = num
            diamaior = i + 1
        if num <= menor:
            menor = num
            diamenor = i + 1

    return TemperaturaInfo(maior, diamaior, menor, diamenor)

temperatura_mes = [22, 18, 25, 20, 23, 19, 21, 17, 11, 26, 16, 27, 18, 22, 15, 25, 19, 21, 23, 15, 24, 28, 17, 20, 22, 26, 29, 21, 19, 25, 20]
info_temperatura = maior_e_menor_temperatura(temperatura_mes)

print("Maior temperatura:", info_temperatura.maior)
print("Dia da maior temperatura:", info_temperatura.diamaior)
print("Menor temperatura:", info_temperatura.menor)
print("Dia da menor temperatura:", info_temperatura.diamenor)
