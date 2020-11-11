import time
from socket import socket
from threading import Thread

MEDIR_TEMPO_A_CADA = 10


def processar(conexao):
    time.sleep(1)
    conexao.sendall(b'oi')
    conexao.close()


def escutar():
    socket_bind_info = ('0.0.0.0', 5000)

    sock = socket()
    sock.bind(socket_bind_info)
    sock.listen()

    start = None
    try:
        count = 0
        while count < MEDIR_TEMPO_A_CADA:
            conexao, origem = sock.accept()

            if count == 0:
                start = time.time()

            th = Thread(target=processar, args=(conexao,))
            th.start()

            count += 1
            if count == MEDIR_TEMPO_A_CADA:
                print(f'{MEDIR_TEMPO_A_CADA} requisições atendidas em {time.time() - start}')
                count = 0

    except KeyboardInterrupt:
        print('Finalizado!')
    finally:
        sock.close()


def main():
    print('Escutando por requisições...')
    escutar()


if __name__ == '__main__':
    main()
