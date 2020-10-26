from multiprocessing import Process
from urllib import request


def usuarios_request(i):
    print(f'***requisicao {i}***')
    resposta = request.urlopen('http://127.0.0.1:5000/usuarios', timeout=10)
    print(resposta.read().decode())
    print('*******')


if __name__ == '__main__':
    print('------- Enviando Requisição')
    for i in range(1000):
        t = Process(target=usuarios_request, args=(i,))
        t.start()
    print('------- Finalizado!')
