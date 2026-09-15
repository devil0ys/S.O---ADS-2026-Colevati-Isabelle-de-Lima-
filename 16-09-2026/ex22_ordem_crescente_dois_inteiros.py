"""
Exercício 22:
Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
"""

def main():
    n1 = int(input("Digite o primeiro inteiro: "))
    n2 = int(input("Digite o segundo inteiro diferente: "))

    if n1 < n2:
        print(f"Ordem crescente: {n1}, {n2}")
    else:
        print(f"Ordem crescente: {n2}, {n1}")

