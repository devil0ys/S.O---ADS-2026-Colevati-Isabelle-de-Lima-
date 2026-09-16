a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
maior = max(a, b)
menor = min(a, b)
if menor != 0 and maior % menor == 0:
    print("O maior é múltiplo do menor.")
else:
    print("O maior não é múltiplo do menor.")
