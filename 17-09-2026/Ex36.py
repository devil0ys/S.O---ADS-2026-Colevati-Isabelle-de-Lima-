n = int(input("Digite N: "))
soma = 1
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
    soma += 1 / fatorial
print("Resultado:", soma)
