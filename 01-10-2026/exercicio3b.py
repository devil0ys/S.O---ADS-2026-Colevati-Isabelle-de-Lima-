def fatorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado = resultado * i

    return resultado


def dividir(a, b):
    return a / b


def main():
    n = int(input("Digite o valor de N: "))

    soma = 1

    for i in range(1, n + 1):
        fat = fatorial(i)
        resultado = dividir(1, fat)
        soma = soma + resultado

    print("Resultado:", soma)


main()