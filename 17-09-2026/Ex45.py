soma = 0
for n in range(1, 16):
    termo = n / (n**2)
    if n % 2 == 0:
        soma -= termo
    else:
        soma += termo
print("Resultado:", soma)