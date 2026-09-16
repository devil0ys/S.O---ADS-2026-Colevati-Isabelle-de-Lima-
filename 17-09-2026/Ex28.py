preco_atual = float(input("Preço atual: "))
venda_mensal = int(input("Média mensal de vendas: "))
preco_novo = preco_atual

if venda_mensal < 500 and preco_atual < 30:
    preco_novo = preco_atual * 1.10
elif 500 <= venda_mensal < 1000 and 30 <= preco_atual < 80:
    preco_novo = preco_atual * 1.15
elif venda_mensal >= 1000 and preco_atual >= 80:
    preco_novo = preco_atual * 0.95

print("Novo preço:", preco_novo)