months = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

temperatures = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]

sum_temperatures = 0
for temperature in temperatures:
    sum_temperatures += temperature
avg_temperature = sum_temperatures / len(temperatures)

print("Lower than averange temperature months:")
for i, temperature in enumerate(temperatures):
    if temperature < avg_temperature:
        print(months[i])