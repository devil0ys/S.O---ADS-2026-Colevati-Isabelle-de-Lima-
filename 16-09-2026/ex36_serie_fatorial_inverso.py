"""
Exercício 36:
Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
"""

import math

def main():
    n = int(input("Digite o valor de N: "))

    soma = 1.0
    for i in range(1, n + 1):
        soma += 1 / math.factorial(i)

    print(f"Resultado da série: {soma:.6f}")

if __name__ == "__main__":
    main()
