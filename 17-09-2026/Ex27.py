voltas = int(input("Número de voltas: "))
extensao = float(input("Extensão do circuito em metros: "))
tempo = float(input("Tempo em minutos: "))
distancia_km = voltas * extensao / 1000
tempo_horas = tempo / 60
velocidade = distancia_km / tempo_horas
print("Velocidade média:", velocidade, "km/h")