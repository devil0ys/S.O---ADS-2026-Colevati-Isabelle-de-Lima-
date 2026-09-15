"""
Exercício 40:
Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.
"""

def main():
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))

    inicio = min(n1, n2)
    fim = max(n1, n2)

    primos = []

    for num in range(inicio, fim + 1):
        if num > 1:
            eh_primo = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    eh_primo = False
                    break
            if eh_primo:
                primos.append(num)

    print(f"Números primos entre {inicio} e {fim}: {primos}")

if __name__ == "__main__":
    main()
