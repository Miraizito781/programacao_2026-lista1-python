print("Digite a quantidade de segundos")
segundosTempo = int(input())

horas = segundosTempo // 3600
minutos = (segundosTempo % 3600) // 60
segundos = segundosTempo % 60

print(f"O horário exato é de: {horas:02d} : {minutos:02d} {segundos:02d}")
