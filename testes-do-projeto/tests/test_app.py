import random
import sys
import time

import pytest
import requests
from pydantic import ValidationError

from app.models import ServerInfo, ServerEndpoint, ResourceAccessKey, ResourceAccessInfo, ResourceData, \
    ResourceSetValueRequest

server_test_data = [
        (
            "201720295",
            "allana",
            "https://sd-ascampos-20212.herokuapp.com/",
        ),
        (
            "201512136",
            "annya",
            "https://sd-annyaourives-20212.herokuapp.com/"
        ),
        (
            "201512137",
            "daniel",
            None
        ),
        (
            "201710375",
            "emmanuel",
            "https://sd-emmanuel.herokuapp.com/"
        ),
        (
            "201420373",
            "gabriel",
            None
        ),
        (
            "201710376",
            "guilherme",
            "https://nodejs-sd-guilhermesenna.herokuapp.com/"
        ),
        (
            "201710377",
            "hiago",
            "https://sd-api-uesc.herokuapp.com/"
        ),
        (
            "201810665",
            "jenilson",
            "https://sd-jenilsonramos-20212.herokuapp.com/"
        ),
        (
            "201610327",
            "joao",
            "https://sd-joaopedrop-20212.herokuapp.com/"
        ),
        (
            "201610337",
            "luis",
            "https://sd-20212-luiscarlos.herokuapp.com/"
        ),
        (
            "201620181",
            "matheus",
            None
        ),
        (
            "201620400",
            "nassim",
            "https://sd-nassimrihan-2021-2.herokuapp.com/"
        ),
        (
            "201710396",
            "robert",
            "https://pratica-sd.herokuapp.com/"
        ),
        (
            "201720308",
            "victor",
            "https://sd-victor-20212.herokuapp.com/"
        )
    ]


@pytest.fixture(scope="function", autouse=True)
def check_test_peers(request, endpoint):
    # Remove o peer de teste se existir.
    url = request.node.callspec.params.get("url")
    resp = requests.delete(f'{url}peers/{endpoint.id}')
    if resp.status_code not in [200, 201, 404]:
        pytest.fail(f"Não posso prosseguir, problemas removendo peer de teste. "
                    f"Implemente o DELETE peer. ({resp.status_code} retornado esperando 200, 201 ou 404)")


@pytest.fixture()
def endpoint():
    return ServerEndpoint(id='test_id', nome='test_endpoint',
                          url='https://example.com')


@pytest.fixture()
def bad_endpoint():
    return {"id": 1000, "nome": 5001, "url": 2111}


class TestInfoAndPeers:

    @pytest.mark.parametrize('id, nome, url',  server_test_data)
    def test_get_info(self, id, nome, url):
        """Test response codes."""
        resp = requests.get(f'{url}info/')
        assert resp.status_code == 200

    @pytest.mark.parametrize('id, nome, url', server_test_data)
    def test_get_info_esquema(self, id, nome, url):
        try:
            resp = requests.get(f'{url}info/')
            ServerInfo.validate(resp.json())
        except ValidationError():
            pytest.fail("A resposta tem um esquema inválido!")

    @pytest.mark.skip
    def test_put_info(self):
        pytest.fail()

    @pytest.mark.parametrize('id, nome, url',  server_test_data)
    def test_get_peers(self, id, nome, url):
        resp = requests.get(f'{url}peers/')
        assert resp.status_code == 200

    @pytest.mark.parametrize('id, nome, url',  server_test_data)
    def test_get_peers_schema(self, id, nome, url):
        resp = requests.get(f'{url}peers/')

        resp_data = resp.json()
        assert type(resp_data) is list
        assert len(resp_data) > 0
        for item in resp_data:
            try:
                ServerEndpoint.validate(item)
            except ValidationError:
                pytest.fail("A lista de peers contém items com o esquema inválido!")

    @pytest.mark.parametrize('id, nome, url',  server_test_data)
    def test_post_peers(self, id, nome, url, endpoint):
        resp = requests.post(f'{url}peers/', json=endpoint.dict())
        # Esperado 200: Tentativa de adicionar peer com dados corretos
        assert resp.status_code == 200

        resp = requests.post(f'{url}peers/', json=endpoint.dict())
        # Esperado 409: Tentativa de adicionar peer existente
        assert resp.status_code == 409

    @pytest.mark.parametrize('id, nome, url',  server_test_data)
    def test_post_peers_com_dados_malformados(self, id, nome, url, bad_endpoint):
        resp = requests.post(f'{url}peers/', json=bad_endpoint)
        # Esperado 400: Tentativa de adicionar peer com dados incorretos e fora do esquema.
        assert resp.status_code == 400

    @pytest.mark.parametrize('id, nome, url',  server_test_data)
    def test_put_peer(self, id, nome, url, endpoint):
        resp = requests.post(f'{url}peers/', json=endpoint.dict())
        assert resp.status_code == 200

        endpoint.nome = 'novo_nome'
        resp = requests.put(f'{url}peers/{endpoint.id}', json=endpoint.dict())

        assert resp.status_code == 200
        assert ServerEndpoint(**resp.json()) == endpoint

    @pytest.mark.skip
    @pytest.mark.parametrize('id, nome, url',  server_test_data)
    def test_put_peer_inexistent(self, id, nome, url, endpoint):
        resp = requests.post(f'{url}peers/', json=endpoint.dict())
        assert resp.status_code == 200

        resp = requests.delete(f'{url}peers/{endpoint.id}')
        assert resp.status_code == 200

        resp = requests.put(f'{url}peers/{endpoint.id}', json=endpoint.dict())
        assert resp.status_code == 404

    @pytest.mark.skip
    @pytest.mark.parametrize('id, nome, url',  server_test_data)
    def test_put_peer_dados_malformatados(self, id, nome, url, endpoint, bad_endpoint):
        resp = requests.post(f'{url}peers/', json=endpoint.dict())
        assert resp.status_code == 200

        resp = requests.put(f'{url}peers/', json=bad_endpoint)
        assert resp.status_code == 400

    @pytest.mark.parametrize('id, nome, url',  server_test_data)
    def test_get_peer_pelo_id(self, id, nome, url, endpoint):
        resp = requests.post(f'{url}peers/', json=endpoint.dict())
        assert resp.status_code == 200

        resp = requests.get(f'{url}peers/{endpoint.id}')
        assert resp.status_code == 200

    @pytest.mark.parametrize('id, nome, url',  server_test_data)
    def test_get_peer_pelo_id_verificacao_de_esquema(self, id, nome, url, endpoint):
        resp = requests.post(f'{url}peers/', json=endpoint.dict())
        assert resp.status_code == 200

        resp = requests.get(f'{url}peers/{endpoint.id}')
        assert resp.status_code == 200

        try:
            ServerEndpoint.validate(resp.json())
        except ValidationError:
            pytest.fail("Esquema do peer inválido!")

    @pytest.mark.parametrize('id, nome, url',  server_test_data)
    def test_get_peer_id_inexistente(self, id, nome, url, endpoint):
        resp = requests.post(f'{url}peers/', json=endpoint.dict())
        assert resp.status_code == 200

        resp = requests.delete(f'{url}peers/{endpoint.id}')
        assert resp.status_code == 200

        resp = requests.get(f'{url}peers/{endpoint.id}')
        assert resp.status_code == 404

    @pytest.mark.parametrize('id, nome, url',  server_test_data)
    def test_delete_peer(self, id, nome, url, endpoint):
        resp = requests.post(f'{url}peers/', json=endpoint.dict())
        assert resp.status_code == 200

        resp = requests.delete(f'{url}peers/{endpoint.id}')
        assert resp.status_code == 200

    @pytest.mark.parametrize('id, nome, url', server_test_data)
    def test_delete_peer_inexistente(self, id, nome, url, endpoint):
        resp = requests.post(f'{url}peers/', json=endpoint.dict())
        assert resp.status_code == 200

        resp = requests.delete(f'{url}peers/{endpoint.id}')
        assert resp.status_code == 200

        resp = requests.delete(f'{url}peers/{endpoint.id}')
        assert resp.status_code == 404


class TestRecurso:

    TEMPO_DE_ACESSO_AO_RECURSO = 10

    @pytest.mark.parametrize('id, nome, url', server_test_data)
    def test_get_recurso_com_chave_invalida(self, id, nome, url):

        # Tentativa de Acesso com chave inválida
        chave = ResourceAccessKey('chave_invalida')
        resp = requests.get(f'{url}/recurso', json=chave.dict())
        assert resp.status_code == 401

    @pytest.mark.parametrize('id, nome, url', server_test_data)
    def test_post_recurso_e_get_valor_com_chave_valida(self, id, nome, url):

        # Obter acesso ao recurso
        resp = requests.post(f'{url}/recurso/')
        assert resp.status_code == 200

        info_de_acesso = ResourceAccessInfo(**resp.json())
        key_access = ResourceAccessKey(codigo_de_acesso=info_de_acesso.codigo_de_acesso)

        # Tenta acessar o recurso com a chave obtida
        resp = requests.get(f'{url}/recurso/', json=key_access.dict())

        assert resp.status_code == 200

    @pytest.mark.parametrize('id, nome, url', server_test_data)
    def test_get_valor_com_chave_expirada(self, id, nome, url):
        # Dorme por um tempo por segurança
        # Isto deve evitar que o recurso esteja ocupado
        # devido ao teste anterior
        time.sleep(TestRecurso.TEMPO_DE_ACESSO_AO_RECURSO)

        # Obtém o recurso
        resp = requests.post(f'{url}/recurso/')
        assert resp.status_code == 200

        info_de_acesso = ResourceAccessInfo(**resp.json())

        # Aguarda o código de acesso expirar
        time.sleep(TestRecurso.TEMPO_DE_ACESSO_AO_RECURSO)

        # Tenta acessar o recurso com a chave expirada
        key_access = ResourceAccessKey(codigo_de_acesso=info_de_acesso.codigo_de_acesso)
        resp = requests.get(f'{url}/recurso/', json=key_access.dict())
        assert resp.status_code == 401

    @pytest.mark.parametrize('id, nome, url', server_test_data)
    def test_acesso_concorrente_ao_recurso(self, id, nome, url):
        # Obtém o recurso
        resp = requests.post(f'{url}/recurso/')
        assert resp.status_code == 200
        info_de_acesso = ResourceAccessInfo(**resp.json())
        chave_de_acesso = ResourceAccessKey(info_de_acesso.codigo_de_acesso)

        # Tentativa de obter o recurso novamente na sequência
        resp = requests.post(f'{url}/recurso/', json=chave_de_acesso)
        assert resp.status_code == 409

    @pytest.mark.parametrize('id, nome, url', server_test_data)
    def test_put_recurso(self, id, nome, url):
        # Aguarda o tempo necessário para que o recurso seja liberado
        # devido aos testes anteriores.
        time.sleep(TestRecurso.TEMPO_DE_ACESSO_AO_RECURSO)

        # Obtém acesso ao recurso
        resp = requests.post(f'{url}/recurso/')
        assert resp.status_code == 200

        info_de_acesso = ResourceAccessInfo(**resp.json())
        acesso = ResourceAccessKey(info_de_acesso.codigo_de_acesso)

        # Tenta acesso ao recurso
        resp = requests.get(f'{url}/recurso/', json=acesso.dict())
        data = ResourceData(**resp.json())

        novo_valor = ResourceSetValueRequest(
            codigo_de_acesso=acesso.codigo_de_acesso,
            valor=random.randint(0, 1000000000)
        )

        # Tenta mudar o valor do recurso
        resp = requests.put(f'{url}/recurso/', json=novo_valor.dict())
        assert resp.status_code == 200

        # Obtém o valor do recurso para verificar se foi alterado
        resp = requests.get(f'{url}/recurso/', json=acesso.dict())
        new_data = ResourceData(**resp.json())
        assert data.valor == new_data.valor

    @pytest.mark.parametrize('id, nome, url', server_test_data)
    def test_liberar_acesso(self, id, nome, url):
        # Tenta obter acesso ao recurso
        resp = requests.post(f'{url}/recurso/')
        assert resp.status_code == 200

        info_de_acesso = ResourceAccessInfo(**resp.json())
        acesso = ResourceAccessKey(info_de_acesso.codigo_de_acesso)

        # Tenta acessar o recurso e obter o valor armazenado
        resp = requests.get(f'{url}/recurso/', json=acesso.dict())
        assert resp.status_code == 200

        # Tenta liberar o recurso
        resp = requests.delete(f'{url}/recurso/', json=acesso.dict())
        assert resp.status_code == 200

        # Após liberação tenta acessar com os dados de acesso antigos
        resp = requests.delete(f'{url}/recurso/', json=acesso.dict())
        assert resp.status_code == 410

    @pytest.mark.parametrize('id, nome, url', server_test_data)
    def test_liberar_acesso(self, id, nome, url):

        # Obtém o recurso
        resp = requests.post(f'{url}/recurso/')
        assert resp.status_code == 200

        info_de_acesso = ResourceAccessInfo(**resp.json())
        acesso = ResourceAccessKey(info_de_acesso.codigo_de_acesso)

        # Aguarda o recurso expirar
        time.sleep(TestRecurso.TEMPO_DE_ACESSO_AO_RECURSO)

        # Tenta liberar o recurso após expiração do código
        resp = requests.delete(f'{url}/recurso/', json=acesso.dict())
        assert resp.status_code == 410

