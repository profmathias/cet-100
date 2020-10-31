from socket import socket


def escutar():
    socket_bind_info = ('127.0.0.1', 5000)

    sock = socket()
    sock.bind(socket_bind_info)
    sock.listen()

    try:
        while True:
            conexao, origem = sock.accept()
            conexao.sendall(b'Oi')
            conexao.close()
    except KeyboardInterrupt:
        print('Finalizado!')
    finally:
        sock.close()


if __name__ == '__main__':
    escutar()
