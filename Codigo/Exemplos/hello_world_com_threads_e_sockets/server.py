from time import sleep
from socket import socket
from threading import Thread


def processar(conexao):
    print("Processando Requisição...")
    sleep(10)
    conexao.sendall(b"Hello World!")
    conexao.close()
    print("Processamento Encerrado!")


def escutar():
    print("Iniciando Servidor...")
    socket_bind_info = ('127.0.0.1', 3001)
    sck = socket()
    sck.bind(socket_bind_info)
    sck.listen()
    print("Servidor Iniciado!")

    while True:
        try:
            conexao, origem = sck.accept()
            print("Nova conexão estabelecida...")
            thread = Thread(target=processar, args=(conexao,))
            thread.start()
            print(f"Thread iniciada - {thread}")

        except KeyboardInterrupt:
            sck.close()
            print("Programa Encerrado!")


if __name__ == '__main__':
    escutar()
