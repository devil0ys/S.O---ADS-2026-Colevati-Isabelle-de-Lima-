import threading
import time
import random

# Apenas 1 pessoa pode cruzar a porta por vez
porta = threading.Semaphore(1)

DISTANCIA_CORREDOR = 200  # metros


class Pessoa(threading.Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def run(self):
        velocidade = random.randint(4, 6)  # m/s
        percorrido = 0
        print(f"{self.nome} começou a caminhar a {velocidade} m/s.")
        while percorrido < DISTANCIA_CORREDOR:
            time.sleep(0.2)
            percorrido = min(percorrido + velocidade * 2, DISTANCIA_CORREDOR)  # 0,2s simulados = 2s reais
            print(f"{self.nome} percorreu {percorrido} m.")

        print(f"{self.nome} chegou à porta e aguarda para cruzar.")
        porta.acquire()
        try:
            print(f"{self.nome} está abrindo e cruzando a porta.")
            time.sleep(random.uniform(1, 2))
            print(f"{self.nome} cruzou a porta.")
        finally:
            porta.release()


if __name__ == "__main__":
    pessoas = [Pessoa(f"Pessoa {i}") for i in range(1, 5)]
    for p in pessoas:
        p.start()
    for p in pessoas:
        p.join()
    print("Todas as pessoas cruzaram a porta.")
