tipo = int(input("Tipo de investimento (1-poupança / 2-renda fixa): "))
valor = float(input("Valor investido: "))

if tipo == 1:
    corrigido = valor * 1.03
    print("Valor corrigido:", corrigido)
elif tipo == 2:
    corrigido = valor * 1.05
    print("Valor corrigido:", corrigido)
else:
    print("Tipo de investimento inválido.")