from multiprocessing import Process
from random import randint
from time import sleep


def tarefa(identificador):
    sleep(randint(1, 6))
    print(f"Hello from {identificador}")


def main():
    processos = list()  # lista para guardar os objetos que
                        # representam cada processo, não
                        # tem utilidade neste exemplo...
    print("Iniciando o Programa...")
    for i in range(0, 10):
        p = Process(target=tarefa, args=(i,))
        p.start()
        processos.append(p)


if __name__ == '__main__':
    main()
