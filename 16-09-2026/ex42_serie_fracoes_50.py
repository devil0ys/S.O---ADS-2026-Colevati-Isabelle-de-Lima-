"""
Exercício 42:
Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99
"""

def main():
    soma = 0.0
    numerador = 1
    denominador = 1

    for _ in range(50):
        soma += numerador / denominador
        numerador += 1
        denominador += 2

    print(f"Resultado da série: {soma:.4f}")

if __name__ == "__main__":
    main()
