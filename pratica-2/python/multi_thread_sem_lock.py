from threading import Thread, Lock
from random import randint
from time import sleep


def tarefa(identificador):
    sleep(randint(1, 6))
    print(f"Hello from {identificador}")


def main():
    threads = list()  # lista para guardar os objetos que
                      # representam cada Thread, não
                      # tem utilidade neste exemplo...
    print("Iniciando o Programa...")
    for i in range(0, 10):
        t = Thread(target=tarefa, args=(i,))
        t.start()
        threads.append(t)


if __name__ == '__main__':
    main()
