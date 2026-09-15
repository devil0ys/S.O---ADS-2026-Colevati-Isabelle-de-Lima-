"""
Exercício 18:
Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.
"""

def main():
    a = int(input("Digite o primeiro número inteiro: "))
    b = int(input("Digite o segundo número inteiro: "))

    if a > b:
        diferenca = a - b
    else:
        diferenca = b - a

    print(f"A diferença do maior pelo menor é: {diferenca}")

if __name__ == "__main__":
    main()
