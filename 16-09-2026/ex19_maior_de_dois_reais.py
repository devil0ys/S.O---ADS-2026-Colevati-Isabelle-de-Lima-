"""
Exercício 19:
Receba 2 valores reais. Calcule e mostre o maior deles.
"""

def main():
    num1 = float(input("Digite o primeiro número real: "))
    num2 = float(input("Digite o segundo número real: "))

    if num1 > num2:
        print(f"O maior número é: {num1}")
    elif num2 > num1:
        print(f"O maior número é: {num2}")
    else:
        print("Os dois números são iguais.")

if __name__ == "__main__":
    main()
