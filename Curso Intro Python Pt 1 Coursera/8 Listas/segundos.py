segundosInput = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundosInput // 86400
horas = (segundosInput - (dias * 86400)) // 3600
minutos = (segundosInput - (dias * 86400) - (horas * 3600)) // 60
segundos = (segundosInput - (dias * 86400) - (horas * 3600) - (minutos * 60))

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")
