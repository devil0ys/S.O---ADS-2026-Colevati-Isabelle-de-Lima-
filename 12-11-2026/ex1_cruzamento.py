import threading
import time
import random

# Variável compartilhada alterada pela Thread de cada carro
sentido = ""

# Apenas um carro por vez no cruzamento
cruzamento = threading.Semaphore(1)


class Carro(threading.Thread):
    def __init__(self, nome, direcao):
        super().__init__()
        self.nome = nome
        self.direcao = direcao

    def run(self):
        global sentido
        time.sleep(random.uniform(0, 1))  # chegada ao cruzamento
        cruzamento.acquire()
        try:
            sentido = self.direcao
            print(f"{self.nome} está passando no sentido: {sentido}")
            time.sleep(random.uniform(0.5, 1.5))  # atravessando
            print(f"{self.nome} saiu do cruzamento.")
        finally:
            cruzamento.release()


if __name__ == "__main__":
    carros = [
        Carro("Carro 1", "Cima -> Baixo (seta vermelha)"),
        Carro("Carro 2", "Esquerda -> Direita (seta verde)"),
        Carro("Carro 3", "Direita -> Esquerda (seta azul)"),
        Carro("Carro 4", "Baixo -> Cima (seta amarela)"),
    ]
    for c in carros:
        c.start()
    for c in carros:
        c.join()
