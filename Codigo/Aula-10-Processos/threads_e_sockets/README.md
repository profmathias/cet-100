# Threads entregando mais Performance

## Sobre a aula prática anterior 

Na aula *Sockets e Threads com Python*, saímos de um programa simples
utilizando sockets e fomos aperfeiçoando o programa para que ele pudesse
obter uma melhor performance. A evolução que tivemos durante a aula, na
sequencia em que elas ocorreram, foram: 

1. Fizemos uma aplicação simples com sockets, onde um cliente enviava uma
mensagem para o servidor, recebia a resposta e encerrava. e tentamos fazer
com que o servidor conseguisse processar mais requisições. 
2. Fizemos com que o servidor não terminasse após atender uma requisição
implementando um loop infinito que escutava por novos dados a cada iteração.
    * Caso existissem dados para serem lidos, o programa lia os dados, 
    processava, enviava a resposta e só então estava pronto para receber dados
    novos.
3. A fim de medir a performance, ou seja, quantas requisições o servidor
consguia atender em um certo intervalo de tempo, utilizamos a biblioteca
`time` do python para medir o tempo total para se atender um número específico
de requisições.
4. Por fim, tentamos modificar o programa servidor para que ele usasse threads
para processar as requisições e fizemos também com que o cliente utiliza-se
threads para enviar requisições em paralelo, porém não terminamos a tempo e
apesar de utilizarmos threads não obtivemos o ganho de performance, como
exercício ficou a análise dis porquês. Descobriram?

## Sobre essa versão do código


Esta versão corrige o problema que tivemos na aula passada e entrega um
performance muito maior. Aqui podemos confirmar o quão importante é o uso de
fluxos de execução paralela em SD, neste caso Multithreads.

Analíse o código compare-o com as versões anteriores e tente enteder o
porque que a versão anterior não funcionava antes de prosseguir para a
explicação a seguir.

### Executando o Código

Rode o servidor direto utilizando python 3... 

```
$ python3 aula8-fixed-server.py
```

Ou, alternativamente, rode o servidor utilizando Docker caso tenha ele
instalado, para isso crie a imagem e em seguida crie e rode o container.

```
$ docker build -t aula8_server_image .
$ docker run -p 5000 --rm --name aula8_container aula8_server_image 
``` 

Em um outro terminal rode o cliente:

```
$ python3 aula8-fixed-client.py
```

### O que foi modificado?

Na verdade o código do cliente era sequencial e isso fez com que o servidor
recebesse uma requisição por vez. Veja o código antigo do cliente:

```python
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
```

Note que as chamadas a `sock.recv` são bloquenantes, ou seja eles bloqueiam
o fluxo de execução até que alguma coisa seja recebida. Assim devemos
utilizar threads também no cliente para que cada requisição seja feita em
uma Thread separada sendo assim o `sock.recv` bloqueia o fluxo de execução 
da Thread em que roda e não do fluxo principal do programa. Leia e releia
a nova versão e se certifique de que entendeu o código por completo. Então
ficamos por aqui com essa prática. 





