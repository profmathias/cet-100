import os
from fastapi import FastAPI
from uvicorn import Config, Server
from pydantic import BaseModel

PORT = os.environ.get('PORT') or "8000"
app = FastAPI()


class Operacao(BaseModel):
    operacao: str
    argumetos: dict


class RespostaX(BaseModel):
    nome: str
    url: str


@app.get('/teste')
def test():
    return "ok"


@app.post('/resolver')
def resolver(dados: Operacao) -> RespostaX:
    print(dados.operacao)
    print(dados.argumetos)
    return RespostaX(nome="Mathias", url="http://sdadsa")


def main():
    config = Config(app=app, host='0.0.0.0', port=int(PORT), debug=True)
    server = Server(config=config)
    server.run()


if __name__ == '__main__':
    main()
