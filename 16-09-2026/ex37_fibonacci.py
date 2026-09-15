"""
Exercício 37:
Receba um número inteiro N. Calcule e mostre a série de Fibonacci até o seu N-ésimo termo.
"""

def main():
    n = int(input("Digite a quantidade de termos da série de Fibonacci: "))

    t1, t2 = 0, 1
    if n <= 0:
        print("Por favor, digite um número maior que 0.")
    elif n == 1:
        print(f"Série: {t1}")
    else:
        termos = []
        for _ in range(n):
            termos.append(str(t1))
            t1, t2 = t2, t1 + t2
        print("Série de Fibonacci:", ", ".join(termos))

if __name__ == "__main__":
    main()
