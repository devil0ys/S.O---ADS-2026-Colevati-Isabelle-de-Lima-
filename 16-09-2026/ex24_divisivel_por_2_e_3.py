"""
Exercício 24:
Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.
"""

def main():
    num = int(input("Digite um número inteiro: "))

    if num % 2 == 0 and num % 3 == 0:
        print(f"O número {num} é divisível por 2 e por 3.")
    else:
        print(f"O número {num} NÃO é divisível simultaneamente por 2 e por 3.")

