import random
import threading
import time


def soma_linha(parametros):
    id_linha = parametros[0]
    valores = parametros[1]
    soma = 0
    for v in valores:
        soma += v
        time.sleep(0.2)
    print(f"Linha {id_linha}: valores {valores} -> soma = {soma}")


if __name__ == "__main__":
    id = 0
    threads = []

    for _ in range(3):
        id += 1
        v1 = random.randint(1, 100)
        v2 = random.randint(1, 100)
        v3 = random.randint(1, 100)
        v4 = random.randint(1, 100)
        v5 = random.randint(1, 100)

        # vetor de parâmetros: id como 1º parâmetro e vetor com os 5 valores
        parametros = [id, [v1, v2, v3, v4, v5]]

        t = threading.Thread(target=soma_linha, args=(parametros,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
