# Variáveis Globais

a = 0
b = 0


def LerValores():

    global a, b

    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))


def VerificarMultiplo():

    global a, b

    if a > b:
        if a % b == 0:
            print("O maior número é múltiplo do menor")
        else:
            print("O maior número não é múltiplo do menor")

    else:
        if b % a == 0:
            print("O maior número é múltiplo do menor")
        else:
            print("O maior número não é múltiplo do menor")


def main():

    LerValores()
    VerificarMultiplo()


if __name__ == "__main__":
    main()