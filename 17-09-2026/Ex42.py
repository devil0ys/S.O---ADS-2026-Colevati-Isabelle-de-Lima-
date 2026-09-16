soma = 0
for numerador in range(1, 51):
    denominador = 2 * numerador - 1
    soma += numerador / denominador
print("Resultado:", soma)
