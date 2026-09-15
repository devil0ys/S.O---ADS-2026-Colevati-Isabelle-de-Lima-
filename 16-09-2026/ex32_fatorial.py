"""
Exercício 32:
Receba um número inteiro. Calcule e mostre o seu fatorial.
"""

def main():
    n = int(input("Digite um número inteiro: "))

    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i

    print(f"O fatorial de {n} é: {fatorial}")

if __name__ == "__main__":
    main()
