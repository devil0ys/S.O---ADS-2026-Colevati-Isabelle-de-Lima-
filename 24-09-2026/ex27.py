def CalcularVelocidade(voltas, extensao, tempo):

    Distancia = voltas * extensao
    Distancia = Distancia / 1000

    Tempo = tempo / 60

    Velocidade = Distancia / Tempo

    print("A velocidade média é:", Velocidade, "km/h")


def main():

    Voltas = int(input("Digite o número de voltas: "))
    Extensao = float(input("Digite a extensão do circuito em metros: "))
    Tempo = float(input("Digite o tempo de duração em minutos: "))

    CalcularVelocidade(Voltas, Extensao, Tempo)


if __name__ == "__main__":
    main()