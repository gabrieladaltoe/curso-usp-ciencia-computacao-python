
segundosInput = int(input("Por favor, entre com o número de segundos que deseja converter:"))


dias = segundosInput // 86400
restoDia = segundosInput % 86400

horas = restoDia // 3600
restoHoras = restoDia % 3600

minutos = restoHoras // 60
restoMinutos = restoHoras % 60

segundos = restoMinutos 


print(str(dias) + " dias, " + str(horas) + " horas," + str(minutos) + " minutos e " + str(segundos) + " segundos.")