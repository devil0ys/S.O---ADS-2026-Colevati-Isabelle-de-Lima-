import threading
import time
import random

NUM_SAPOS = 5
DISTANCIA_MAXIMA = 100  # cm
PULO_MAXIMO = 5         # cm

# Protege a variável de colocação (e a impressão da chegada)
mutex_chegada = threading.Semaphore(1)
colocacao = 0


class Sapo(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self.numero = numero
        self.percorrido = 0

    def run(self):
        global colocacao
        while self.percorrido < DISTANCIA_MAXIMA:
            pulo = random.randint(0, PULO_MAXIMO)
            self.percorrido = min(self.percorrido + pulo, DISTANCIA_MAXIMA)
            print(f"Sapo {self.numero}: pulou {pulo} cm e já percorreu {self.percorrido} cm.")
            time.sleep(random.uniform(0.01, 0.05))

        mutex_chegada.acquire()
        try:
            colocacao += 1
            print(f">>> Sapo {self.numero} chegou em {colocacao}º lugar!")
        finally:
            mutex_chegada.release()


if __name__ == "__main__":
    sapos = [Sapo(i) for i in range(1, NUM_SAPOS + 1)]
    for s in sapos:
        s.start()
    for s in sapos:
        s.join()
    print("Corrida finalizada.")
