import sys

import pytest
import requests
from pydantic import ValidationError

from app.models import ServerInfo, ServerEndpoint

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
        pytest.fail("Não posso prosseguir, problemas removendo peer de teste. "
                    "Implemente o DELETE peer.")


@pytest.fixture()
def endpoint():
    return ServerEndpoint(id='test_id', nome='test_endpoint',
                          url='https://example.com')


@pytest.fixture()
def bad_endpoint():
    return {"id": 1000, "nome": 5001, "url": 2111}


@pytest.mark.parametrize('id, nome, url',  server_test_data)
def test_get_info(id, nome, url):
    """Test response codes."""
    resp = requests.get(f'{url}info/')
    assert resp.status_code == 200


@pytest.mark.parametrize('id, nome, url', server_test_data)
def test_get_info_esquema(id, nome, url):
    try:
        resp = requests.get(f'{url}info/')
        ServerInfo.validate(resp.json())
    except ValidationError():
        pytest.fail("A resposta tem um esquema inválido!")


@pytest.mark.skip
def test_put_info():
    pytest.fail()


@pytest.mark.parametrize('id, nome, url',  server_test_data)
def test_get_peers(id, nome, url):
    resp = requests.get(f'{url}peers/')
    assert resp.status_code == 200


@pytest.mark.parametrize('id, nome, url',  server_test_data)
def test_get_peers_schema(id, nome, url):
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
def test_post_peers(id, nome, url, endpoint):
    resp = requests.post(f'{url}/peers/', json=endpoint.dict())
    # Esperado 200: Tentativa de adicionar peer com dados corretos
    assert resp.status_code == 200

    resp = requests.post(f'{url}/peers/', json=endpoint.dict())
    # Esperado 409: Tentativa de adicionar peer existente
    assert resp.status_code == 409


@pytest.mark.parametrize('id, nome, url',  server_test_data)
def test_post_peers_com_dados_malformados(id, nome, url, bad_endpoint):
    resp = requests.post(f'{url}/peers/', json=bad_endpoint)
    # Esperado 400: Tentativa de adicionar peer com dados incorretos e fora do esquema.
    assert resp.status_code == 400


@pytest.mark.parametrize('id, nome, url',  server_test_data)
def test_put_peer(id, nome, url, endpoint):
    resp = requests.post(f'{url}peers/', json=endpoint.dict())
    assert resp.status_code == 200

    endpoint.nome = 'novo_nome'
    resp = requests.put(f'{url}peers/{endpoint.id}', json=endpoint.dict())

    assert resp.status_code == 200
    assert ServerEndpoint(**resp.json()) == endpoint


@pytest.mark.skip
@pytest.mark.parametrize('id, nome, url',  server_test_data)
def test_put_peer_inexistent(id, nome, url, endpoint):
    resp = requests.post(f'{url}peers/', json=endpoint.dict())
    assert resp.status_code == 200

    resp = requests.delete(f'{url}peers/{endpoint.id}')
    assert resp.status_code == 200

    resp = requests.put(f'{url}peers/{endpoint.id}', json=endpoint.dict())
    assert resp.status_code == 404


@pytest.mark.skip
@pytest.mark.parametrize('id, nome, url',  server_test_data)
def test_put_peer_dados_malformatados(id, nome, url, endpoint, bad_endpoint):
    resp = requests.post(f'{url}peers/', json=endpoint.dict())
    assert resp.status_code == 200

    resp = requests.put(f'{url}peers/', json=bad_endpoint)
    assert resp.status_code == 400


@pytest.mark.parametrize('id, nome, url',  server_test_data)
def test_get_peer_pelo_id(id, nome, url):
    resp = requests.post(f'{url}peers/', json=endpoint.dict())
    assert resp.status_code == 200

    resp = requests.get(f'{url}peers/{endpoint.id}')
    assert resp.status_code == 200


@pytest.mark.parametrize('id, nome, url',  server_test_data)
def test_get_peer_pelo_id_verificacao_de_esquema(id, nome, url, endpoint):
    resp = requests.post(f'{url}peers/', json=endpoint.dict())
    assert resp.status_code == 200

    resp = requests.get(f'{url}peers/{endpoint.id}')
    assert resp.status_code == 200

    try:
        ServerEndpoint.validate(resp.json())
    except ValidationError:
        pytest.fail("Esquema do peer inválido!")


@pytest.mark.parametrize('id, nome, url',  server_test_data)
def test_get_peer_id_inexistente(id, nome, url, endpoint):
    resp = requests.post(f'{url}peers/', json=endpoint.dict())
    assert resp.status_code == 200

    resp = requests.delete(f'{url}peers/{endpoint.id}')
    assert resp.status_code == 200

    resp = requests.get(f'{url}peers/{endpoint.id}')
    assert resp.status_code == 404


@pytest.mark.parametrize('id, nome, url',  server_test_data)
def test_delete_peer(id, nome, url, endpoint):
    resp = requests.post(f'{url}peers/', json=endpoint.dict())
    assert resp.status_code == 200

    resp = requests.delete(f'{url}peers/{endpoint.id}')
    assert resp.status_code == 200


@pytest.mark.parametrize('id, nome, url', server_test_data)
def test_delete_peer_inexistente(id, nome, url, endpoint):
    resp = requests.post(f'{url}peers/', json=endpoint.dict())
    assert resp.status_code == 200

    resp = requests.delete(f'{url}peers/{endpoint.id}')
    assert resp.status_code == 200

    resp = requests.delete(f'{url}peers/{endpoint.id}')
    assert resp.status_code == 404


