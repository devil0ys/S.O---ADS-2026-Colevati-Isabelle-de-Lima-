# Variáveis Globais

HoraInício = 0
MinutoInício = 0
HoraFim = 0
MinutoFim = 0
Minu = 0
Horas = 0
Minutos = 0


def LerHoraseMinutos():

    global HoraInício, MinutoInício, HoraFim, MinutoFim, Minu

    HoraInício = int(input("Digite a hora de inicio: "))
    MinutoInício = int(input("Digite os minutos de inicio: "))

    HoraFim = int(input("Digite a hora de fim: "))
    MinutoFim = int(input("Digite os minutos de fim: "))


def CalcularTempo():

    global HoraInício, MinutoInício, HoraFim, MinutoFim, Minu, Horas, Minutos

    if HoraInício > HoraFim:
        HoraFim = HoraFim + 24

    if MinutoInício > MinutoFim:
        MinutoFim = MinutoFim + 60
        HoraFim = HoraFim - 1

    Minu = (HoraFim - HoraInício) * 60 + (MinutoFim - MinutoInício)

    Horas = Minu // 60
    Minutos = Minu % 60

    print("O tempo total de jogo foi de:", Horas, "horas e", Minutos, "minutos")


def main():

    LerHoraseMinutos()
    CalcularTempo()


if __name__ == "__main__":
    main()

