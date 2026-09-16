base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1

for i in range(abs(expoente)):
    resultado *= base

if expoente < 0:
    resultado = 1 / resultado

print("Potência:", resultado)