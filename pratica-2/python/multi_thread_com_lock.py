from threading import Thread, Lock
from random import randint
from time import sleep

x = 10

lock = Lock()


def tarefa(identificador):
    global x
    sleep(randint(1, 6))
    if lock.acquire():
        print(f"Hello from {identificador} - {x}")
        x += 1
    lock.release()


def main():
    processos = list()  # lista para guardar os objetos que
                        # representam cada Thread, não
                        # tem utilidade neste exemplo...
    print("Iniciando o Programa...")
    for i in range(0, 10):
        t = Thread(target=tarefa, args=(i,))
        t.start()
        processos.append(t)


if __name__ == '__main__':
    main()
