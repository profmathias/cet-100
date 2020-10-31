from socket import socket


def escutar():
    socket_bind_info = ('127.0.0.1', 5000)

    sock = socket()
    sock.bind(socket_bind_info)
    sock.listen()

    conexao, origem = sock.accept()
    print(f'Conexão vinda de {conexao}')

    conexao.sendall(b'Oi')

    sock.close()


if __name__ == '__main__':
    escutar()
