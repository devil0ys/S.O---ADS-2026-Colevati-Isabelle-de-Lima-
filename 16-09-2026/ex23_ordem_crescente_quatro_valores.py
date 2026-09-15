"""
Exercício 23:
Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem.
Mostre os 4 números em ordem crescente.
"""

def main():
    a = int(input("Digite o 1º número (menor): "))
    b = int(input("Digite o 2º número (médio): "))
    c = int(input("Digite o 3º número (maior): "))
    d = int(input("Digite o 4º número qualquer: "))

    if d >= c:
        print(f"Ordem crescente: {a}, {b}, {c}, {d}")
    elif d >= b:
        print(f"Ordem crescente: {a}, {b}, {d}, {c}")
    elif d >= a:
        print(f"Ordem crescente: {a}, {d}, {b}, {c}")
    else:
        print(f"Ordem crescente: {d}, {a}, {b}, {c}")

if __name__ == "__main__":
    main()
