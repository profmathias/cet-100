from socket import socket


def requisicao():
    sck = socket()

    server_info = ('127.0.0.1', 3001)
    sck.connect(server_info)
    print("Conexao com o servidor foi aceita!")

    print("Aguardando dados...")
    dados_recebidos = sck.recv(1000)

    print(f"Dado recebido {dados_recebidos}")
    sck.close()


if __name__ == '__main__':
    requisicao()
