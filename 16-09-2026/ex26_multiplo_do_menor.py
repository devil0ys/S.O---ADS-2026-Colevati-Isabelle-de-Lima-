"""
Exercício 26:
Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor.
"""

def main():
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))

    maior = max(n1, n2)
    menor = min(n1, n2)

    if menor != 0 and maior % menor == 0:
        print(f"{maior} é múltiplo de {menor}.")
    else:
        print(f"{maior} NÃO é múltiplo de {menor}.")

if __name__ == "__main__":
    main()
