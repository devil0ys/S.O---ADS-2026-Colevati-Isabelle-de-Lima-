"""
Exercício 44:
Receba o número da base e do expoente. Calcule e mostre o valor da potência.
"""

def main():
    base = float(input("Digite a base: "))
    expoente = int(input("Digite o expoente (inteiro): "))

    resultado = 1.0
    if expoente >= 0:
        for _ in range(expoente):
            resultado *= base
    else:
        for _ in range(abs(expoente)):
            resultado *= base
        resultado = 1 / resultado

    print(f"{base}^{expoente} = {resultado}")

if __name__ == "__main__":
    main()
