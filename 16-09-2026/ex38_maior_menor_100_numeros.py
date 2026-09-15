"""
Exercício 38:
Receba 100 números inteiros reais positivos. Verifique e mostre o maior e o menor valor.
"""

def main():
    maior = -1.0
    menor = float('inf')

    print("Digite 100 valores positivos:")
    for i in range(1, 101):
        valor = float(input(f"Valor {i}: "))
        while valor < 0:
            valor = float(input(f"Valor inválido. Digite um valor positivo ({i}): "))
        
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")

if __name__ == "__main__":
    main()
