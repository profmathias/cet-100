from typing import Any

from datetime import datetime
from pydantic import BaseModel
from pydantic.types import StrictStr


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


class ResourceAccessInfo(BaseModel):
    codigo_de_acesso: StrictStr
    validade: datetime


class ResourceAccessKey(BaseModel):
    codigo_de_acesso: StrictStr


class ResourceData(BaseModel):
    valor: Any


class ResourceSetValueRequest(BaseModel):
    codigo_de_acesso: StrictStr
    valor: Any