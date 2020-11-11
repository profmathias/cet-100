from socket import socket
from multiprocessing import Process

TAM_BUFFER = 1000
NUM_REQ = 10


def enviar():
    sock = socket()
    server_info = ('127.0.0.1', 5000)
    sock.connect(server_info)
    dados_recebidos = sock.recv(TAM_BUFFER)
    print(dados_recebidos, flush=True)
    sock.close()


def requisicoes():
    try:
        count = 0
        while count < NUM_REQ:
            count += 1
            th = Process(target=enviar)
            th.start()
    except KeyboardInterrupt:
        print("Interrompido!")


def main():
    requisicoes()


if __name__ == '__main__':
    main()
