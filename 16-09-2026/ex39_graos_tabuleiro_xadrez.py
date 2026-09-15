"""
Exercício 39:
Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
Casa: 1 2 3 4 ... 64
Qdte: 1 2 4 8 ... N
"""

def main():
    total_graos = 0
    for casa in range(64):
        total_graos += 2 ** casa

    print(f"Quantidade total de grãos no tabuleiro: {total_graos}")

if __name__ == "__main__":
    main()
