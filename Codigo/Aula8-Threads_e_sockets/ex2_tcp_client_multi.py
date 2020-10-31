import time
from socket import socket

TAM_BUFFER = 1000


def requisicao():

    try:
        while True:
            time.sleep(1)
            sock = socket()
            server_info = ('127.0.0.1', 5000)
            sock.connect(server_info)
            dados_recebidos = sock.recv(TAM_BUFFER)
            print(dados_recebidos)
    except KeyboardInterrupt:
        print("Interrompido!")
    finally:
        sock.close()


if __name__ == '__main__':
    requisicao()

