def CalcularPreco(preco, venda):

    PrecoNovo = preco

    if venda < 500 and preco < 30:
        PrecoNovo = preco + (preco * 10 / 100)

    elif venda >= 500 and venda < 1000 and preco >= 30 and preco < 80:
        PrecoNovo = preco + (preco * 15 / 100)

    elif venda >= 1000 and preco >= 80:
        PrecoNovo = preco - (preco * 5 / 100)

    print("O novo preço é:", PrecoNovo)


def main():

    Preco = float(input("Digite o preço atual: "))
    Venda = int(input("Digite a média mensal de vendas: "))

    CalcularPreco(Preco, Venda)


if __name__ == "__main__":
    main()