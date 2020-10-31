import time
from datetime import datetime
from socket import socket
from threading import Thread

MAX_REQ = 100


def processar(conexao):
    time.sleep(1)
    conexao.sendall(b'oi')
    conexao.close()


def escutar():
    socket_bind_info = ('127.0.0.1', 5000)

    sock = socket()
    sock.bind(socket_bind_info)
    sock.listen()

    start = None
    try:
        count = 0
        while count < MAX_REQ:
            conexao, origem = sock.accept()

            if start is None:
                start = datetime.now()

            th = Thread(target=processar, args=(conexao,))
            th.start()

            count += 1
    except KeyboardInterrupt:
        print('Finalizado!')
    finally:
        sock.close()
    tempo_total = datetime.now() - start

    print(f'O servidor levou {tempo_total} para processar as requisições!')


if __name__ == '__main__':
    escutar()
