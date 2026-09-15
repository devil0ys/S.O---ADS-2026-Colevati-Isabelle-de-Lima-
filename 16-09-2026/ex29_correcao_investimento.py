"""
Exercício 29:
Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento.
Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%.
"""

def main():
    tipo = int(input("Tipo de investimento (1 = Poupança, 2 = Renda Fixa): "))
    valor = float(input("Valor investido: R$ "))

    if tipo == 1:
        valor_corrigido = valor * 1.03
        print(f"Valor corrigido em 30 dias (Poupança): R$ {valor_corrigido:.2f}")
    elif tipo == 2:
        valor_corrigido = valor * 1.05
        print(f"Valor corrigido em 30 dias (Renda Fixa): R$ {valor_corrigido:.2f}")
    else:
        print("Tipo de investimento inválido.")

if __name__ == "__main__":
    main()
