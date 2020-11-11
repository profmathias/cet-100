# Instruções

Neste exemplo utilizamos a biblioteca do python chamada `zeroconf` para
descobrir serviços utilizando DNS-SD e mDNS. A biblioteca oferece o que
eles chamam de ServiceBrowser, cujo construtor tem a seguinte assinatura:

```python
ServiceBrowser(zeroconf, "_sd-chat-host._tcp.local.", listener)
```

Onde a primeira variável é um contexto Zeroconf, que pode ser criado
a partir do objeto `zeroconf.Zeroconf` fazendo `zeroconf = Zeroconf
()`, seguido
do tipo do serviço que estamos procurando e um objeto de um tipo que
implemente a classe abstrata `zeroconf.ServiceListener`, está classe
especifica os métodos que serão invocados quando um evento de descoberta
ocorrer.

Após criar o objeto ServiceBrowser invocanco o seu construtor ele ir
á iniciar uma thread e deixará o fluxo do programa seguir, o ServiceBrowser
no entanto continua executando na Thread em paralelo com o fluxo principal
de execução. Quando quiser parar o Browser invoque o método `cancel()` do
service browser.

Este é um exemplo de tecnologia que podemos utilizar para descobrir serviços
em uma rede. Considere utilizá-lo no projeto final. 

## Executando o exemplo

Para executar o exemplo rode o módulo `main` diretamente com:

```
$ python3 main.py
```

ou instale o script com:

```
$ pip3 install -e .

```

O menos -e vai fazer com que a instalação seja sensível a mudanças no código
do projeto, assim, caso você atualize o projeto as mudanças serão refletidas
no script instalado. Depois de instalar para executar rode o seguinte comando:

```
$ sd_descoberta
```
