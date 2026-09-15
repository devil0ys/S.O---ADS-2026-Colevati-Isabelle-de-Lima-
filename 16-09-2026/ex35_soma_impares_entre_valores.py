"""
Exercício 35:
Receba 2 números inteiros, verifique qual o maior entre eles.
Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.
"""

def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    maior = max(n1, n2)
    menor = min(n1, n2)

    soma_impares = 0
    for i in range(menor + 1, maior):
        if i % 2 != 0:
            soma_impares += i

    print(f"Soma dos ímpares entre {menor} e {maior}: {soma_impares}")

if __name__ == "__main__":
    main()
