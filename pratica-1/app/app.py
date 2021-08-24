import os
from fastapi import FastAPI
from uvicorn import Config, Server

PORT = int(os.environ.get('PORT')) or 8000
app = FastAPI()


@app.get('/hello')
def app_get(name=None):
    if name:
        return f'Hello {name}!'
    else:
        return 'Hello World!'


@app.get('/clientes')
def app_clientes_get():
    return ['Mathias', 'José', 'Thiago']


@app.post('/')
def app_post():
    return 'Hello Post!'


def main():
    config = Config(app=app, host='0.0.0.0', port=PORT, debug=True)
    server = Server(config=config)
    server.run()


if __name__ == '__main__':
    main()
