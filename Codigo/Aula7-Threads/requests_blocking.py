from urllib import request


def usuarios_request():
    resposta = request.urlopen('http://127.0.0.1:5000/usuarios', timeout=10)
    print(resposta.read().decode())


if __name__ == '__main__':
    print('------- Enviando Requisição')
    usuarios_request()
    print('------- Finalizado!')
