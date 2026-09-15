"""
Exercício 33:
Receba um número N. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
"""

def main():
    n = int(input("Digite o valor de N: "))

    soma = 0.0
    for i in range(1, n + 1):
        soma += 1 / i

    print(f"Resultado da série: {soma:.4f}")

if __name__ == "__main__":
    main()
