from multiprocessing import Pool
from time import sleep
from random import randint


def tarefa(identificador):
    sleep(randint(1, 6))
    print(f"Hello from {identificador}")


def main(requisoes):
    with Pool(4) as pool:
        pool.map(tarefa, requisoes)


if __name__ == '__main__':
    main([1, 2, 3, 4, 5, 6, 7, 8, 9])
