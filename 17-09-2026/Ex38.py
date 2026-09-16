maior = None
menor = None
for i in range(100):
    n = int(input(f"Digite o {i+1}º número positivo: "))
    while n <= 0:
        n = int(input("Digite um valor positivo: "))
    if maior is None or n > maior:
        maior = n
    if menor is None or n < menor:
        menor = n
print("Maior:", maior)
print("Menor:", menor)
