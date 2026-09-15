"""
Exercício 20:
Receba 3 coeficientes A, B, e C de uma equação do 2º grau (AX² + BX + C = 0).
Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
"""

import math

def main():
    a = float(input("Digite o coeficiente A: "))
    b = float(input("Digite o coeficiente B: "))
    c = float(input("Digite o coeficiente C: "))

    if a == 0:
        print("Não é uma equação do 2º grau.")
    else:
        delta = (b ** 2) - (4 * a * c)
        if delta < 0:
            print("A equação não possui raízes reais.")
        elif delta == 0:
            x = -b / (2 * a)
            print(f"Possui uma raiz real: x = {x:.2f}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print(f"Possui duas raízes reais: x1 = {x1:.2f} e x2 = {x2:.2f}")

if __name__ == "__main__":
    main()
