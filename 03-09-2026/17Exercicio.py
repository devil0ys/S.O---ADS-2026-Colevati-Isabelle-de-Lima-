tempo = float(input("Digite o tempo de percurso em horas: "))
velocidade = float(input("Digite a velocidade média em km/h: "))

distancia = tempo * velocidade
litros = distancia / 12

print("A distância percorrida foi:", distancia, "km")
print("A quantidade de litros gastos foi:", litros, "L")