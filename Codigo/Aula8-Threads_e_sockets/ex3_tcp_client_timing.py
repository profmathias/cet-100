from socket import socket

TAM_BUFFER = 1000
NUM_REQ = 1000


def requisicao():
    try:
        count = 0
        while count < NUM_REQ:
            sock = socket()
            server_info = ('127.0.0.1', 5000)
            sock.connect(server_info)
            dados_recebidos = sock.recv(TAM_BUFFER)

            print(dados_recebidos)
            sock.close()
            count += 1
    except KeyboardInterrupt:
        print("Interrompido!")


if __name__ == '__main__':
    requisicao()
