from datetime import datetime
from socket import socket

MAX_REQ = 1000


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

            conexao.sendall(b'Oi')
            conexao.close()
            count += 1
    except KeyboardInterrupt:
        print('Finalizado!')
    finally:
        sock.close()
    tempo_total = datetime.now() - start

    print(f'O servidor levou {tempo_total} para processar as requisições!')


if __name__ == '__main__':
    escutar()
