# Comunicação com Broker de Mensagem (RabbitMQ)

Para iniciarmos precisamos rodar uma instância do RabbitMQ, docker facilita
muito a nossa vida durante o desenvolvimento, nos livrando do tedioso
processo de instalação.

> **Nota:** Para implantação em ambientes de produção o trabalho ser
> á tedioso de qualquer forma pois precisamos nos certificar de que o
> sistema está seguro e bem configurado.

```
docker run -d --hostname rabbit-server -p 15672:15672 -p 5672:5672 -e
RABBITMQ_DEFAULT_USER=usuario -e RABBITMQ_DEFAULT_PASS=senha --name 
rabbit-container rabbitmq:management 
```

No comando acima a opção `-e` define variáveis de ambiente que serão
definidas no container, no caso do RabbitMQ caso ele identifique a
existencia das variáveis de ambiente `RABBITMQ_DEFAULT_USER` e
`RABBITMQ_DEFAULT_PASS` ele as utilizará para configura o usuário e senha do
sistema de gerenciamento. A opção `-p` mapeia as portas especificadas do
container para portas no hospedeiro.

O RabbitMQ oferece uma interface de gerenciamento e é lá que iremos criar as
nossas filas de mensagens. Você pode acessar a interface de gerenciamento
através do browser apontando para o endereço `http://localhost:15762` e
informando o usuário e senha definidos pelas variáveis de ambiente setadas
quando executou o `docker run`.

Vá na aba `Exchange` do gerenciador do RabbitMQ. Clique em `Add a new
Exchange` logo abaixo da tabela de Exchanges. De um nome para a Exchange, no
nosso caso `blog` é suficiente, deixe o resto como está e clique em 
`Add Exchange`. A nova Excahnge aparecerá na tabela. Se clicarmos nela
poderemos ver os detalhes e editar a Exchange. Agora clique na aba `Queues`
para criarmos as filas. Clique em `Add new Queue`, deixe o tipo como `Classic`
e o restante deixe como também como está clique em Criar.

Agora vamos vincular a Fila que criamos (Queue) com o Exchange. Clique na
Queue que apareceu na tabela da aba `Queues`. Você verá em `Binding` que a
fila não possui Bindings e um formulário para preencher para adicionar um
`Bind`. Preencha esse formulário com os seguintes valores:
 
 - From exchange: `blog`
 - Routing Key: `post` (mensagens com essa chave serão roteadas para esta fila)
 
Pronto, agora verifique os códigos de `server.py` e `cliente.py` para
verificar como interagimos com as filas utilizando python.
