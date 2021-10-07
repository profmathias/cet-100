from pydantic import BaseModel


class ServerInfo(BaseModel):
    server_name: str
    server_endpoint: str
    descricao: str
    versao: str
    status: str
    tipo_de_eleicao_ativa: str


class ServerEndpoint(BaseModel):
    id: str
    nome: str
    url: str
