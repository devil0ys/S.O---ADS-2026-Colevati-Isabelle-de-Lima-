"""
Exercício 28:
Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço.
"""

def main():
    preco_atual = float(input("Digite o preço atual: R$ "))
    venda_mensal = float(input("Digite a média de venda mensal: "))

    if venda_mensal < 500 and preco_atual < 30.00:
        preco_novo = preco_atual * 1.10
    elif 500 <= venda_mensal < 1000 and 30.00 <= preco_atual < 80.00:
        preco_novo = preco_atual * 1.15
    elif venda_mensal >= 1000 and preco_atual >= 80.00:
        preco_novo = preco_atual * 0.95
    else:
        preco_novo = preco_atual

    print(f"O novo preço é: R$ {preco_novo:.2f}")

if __name__ == "__main__":
    main()
