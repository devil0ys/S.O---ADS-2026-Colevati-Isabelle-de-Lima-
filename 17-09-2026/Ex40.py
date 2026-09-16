a = int(input("Digite o primeiro limite: "))
b = int(input("Digite o segundo limite: "))
inicio = min(a, b)
fim = max(a, b)

for n in range(max(2, inicio), fim + 1):
    primo = True
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            primo = False
            break
    if primo:
        print(n, end=" ")
print()
