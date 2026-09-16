a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
inicio = min(a, b)
fim = max(a, b)
soma = 0
for i in range(inicio, fim + 1):
    if i % 2 != 0:
        soma += i
print("Soma dos ímpares:", soma)