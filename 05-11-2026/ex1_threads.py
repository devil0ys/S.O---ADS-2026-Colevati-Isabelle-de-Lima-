import threading
import time


def tarefa(id):
    time.sleep(0.5)
    print("Thread #" + str(id))


if __name__ == "__main__":
    threads = []
    for i in range(1, 6):
        t = threading.Thread(target=tarefa, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
