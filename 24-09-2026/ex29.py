def CalcularInvestimento(tipo, valor):

    if tipo == 1:
        ValorCorrigido = valor + (valor * 3 / 100)
        print("O valor corrigido é:", ValorCorrigido)

    elif tipo == 2:
        ValorCorrigido = valor + (valor * 5 / 100)
        print("O valor corrigido é:", ValorCorrigido)

    else:
        print("Tipo de investimento inválido")


def main():

    Tipo = int(input("Digite o tipo de investimento (1 ou 2): "))
    Valor = float(input("Digite o valor do investimento: "))

    CalcularInvestimento(Tipo, Valor)


if __name__ == "__main__":
    main()