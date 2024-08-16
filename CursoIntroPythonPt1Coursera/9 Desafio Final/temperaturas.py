def maior_e_menor_temperatura(lista):
    if not temperatura_mes:
        return None  # Retorna None se a lista estiver vazia
    
    maior = temperatura_mes[0]  # Suponha que o primeiro número seja o maior inicialmente
    menor = temperatura_mes[0]
    diamaior = 0
    ciclo = 0
    for num in temperatura_mes:
        if num > maior:
            maior = num  # Se encontrarmos um número maior, atualizamos o valor de 'maior'
            diamaior = ciclo + 1 
        elif num < menor:
            menor = num
            diamenor = ciclo + 1
        ciclo += 1
    return maior, diamaior, menor, diamenor

                # [01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
                # [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,]
temperatura_mes = [22, 18, 25, 20, 23, 19, 21, 17, 11, 26, 16, 27, 18, 22, 15, 25, 19, 21, 23, 15, 24, 28, 17, 20, 22, 26, 29, 21, 19, 25, 20]
maior, diamaior, menor, diamenor = maior_e_menor_temperatura(temperatura_mes)
print(maior, diamaior)
print(menor, diamenor)