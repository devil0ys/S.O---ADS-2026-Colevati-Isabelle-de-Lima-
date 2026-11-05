import random
import threading
import time

DISTANCIA_MAXIMA = 100   # cm
PULO_MAXIMO = 5          # cm

lock = threading.Lock()
colocacao = []


def sapo(numero):
    percorrido = 0
    while percorrido < DISTANCIA_MAXIMA:
        pulo = random.randint(1, PULO_MAXIMO)
        percorrido += pulo
        if percorrido > DISTANCIA_MAXIMA:
            percorrido = DISTANCIA_MAXIMA

        with lock:
            print(f"Sapo {numero} pulou {pulo} cm e já percorreu {percorrido} cm")

        time.sleep(random.uniform(0.1, 0.5))

    with lock:
        colocacao.append(numero)
        print(f">>> Sapo {numero} CHEGOU! Posição: {len(colocacao)}º lugar")


if __name__ == "__main__":
    print("A corrida de sapos vai começar!\n")
    threads = []
    for i in range(1, 6):
        t = threading.Thread(target=sapo, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n=== Resultado final ===")
    for pos, s in enumerate(colocacao, start=1):
        print(f"{pos}º lugar: Sapo {s}")
