"""
Exercício 27:
Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos).
Calcule e mostre a velocidade média em km/h.
"""

def main():
    voltas = int(input("Número de voltas: "))
    extensao_metros = float(input("Extensão do circuito (em metros): "))
    tempo_minutos = float(input("Tempo de duração (em minutos): "))

    distancia_total_km = (voltas * extensao_metros) / 1000
    tempo_horas = tempo_minutos / 60

    velocidade_media = distancia_total_km / tempo_horas
    print(f"Velocidade média: {velocidade_media:.2f} km/h")

if __name__ == "__main__":
    main()
