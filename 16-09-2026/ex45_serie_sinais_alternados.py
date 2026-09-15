"""
Exercício 45:
Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 - ... + 15/225
"""

def main():
    soma = 0.0

    for i in range(1, 16):
        termo = i / (i ** 2)
        if i % 2 == 0:
            soma -= termo
        else:
            soma += termo

    print(f"Resultado da série com sinais alternados: {soma:.4f}")

if __name__ == "__main__":
    main()
