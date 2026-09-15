"""
Exercício 34:
Receba um número. Calcule e mostre os resultados da tabuada desse número.
"""

def main():
    num = int(input("Digite um número para ver a tabuada: "))

    for i in range(1, 11):
        print(f"{num} x {i:2d} = {num * i}")

if __name__ == "__main__":
    main()
