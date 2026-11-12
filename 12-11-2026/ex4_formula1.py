import threading
import time
import random

NUM_EQUIPES = 7
CARROS_POR_EQUIPE = 2
MAX_NA_PISTA = 5
VOLTAS = 3

# No máximo 5 carros na pista ao mesmo tempo
pista = threading.Semaphore(MAX_NA_PISTA)
# Um semáforo por equipe: só 1 carro da equipe na pista
equipes = [threading.Semaphore(1) for _ in range(NUM_EQUIPES)]


class Carro(threading.Thread):
    def __init__(self, equipe, numero):
        super().__init__()
        self.equipe = equipe
        self.numero = numero
        self.nome = f"Equipe {equipe + 1} - Carro {numero}"

    def run(self):
        # Primeiro garante a vaga da equipe, depois a vaga na pista
        # (evita ocupar vaga na pista sem poder entrar)
        equipes[self.equipe].acquire()
        pista.acquire()
        try:
            print(f"{self.nome} entrou na pista.")
            for volta in range(1, VOLTAS + 1):
                inicio = time.time()
                time.sleep(random.uniform(0.5, 1.5))
                tempo = time.time() - inicio
                print(f"{self.nome} - volta {volta}: {tempo:.3f} s")
            print(f"{self.nome} saiu da pista.")
        finally:
            pista.release()
            equipes[self.equipe].release()


if __name__ == "__main__":
    carros = [Carro(e, n) for e in range(NUM_EQUIPES) for n in range(1, CARROS_POR_EQUIPE + 1)]
    random.shuffle(carros)
    for c in carros:
        c.start()
    for c in carros:
        c.join()
    print("Treino finalizado.")
