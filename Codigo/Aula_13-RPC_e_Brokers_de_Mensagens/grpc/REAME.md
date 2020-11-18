# RPC com gRPC
 
O gRPC é um middleware para RPC (Remote Porcdedures Call) desenvolvido e
mantido pelo google. Ele oferece suporte para diferentes linguagens de
programação inclusive python.

Para iniciar um projeto com gRPC e Python certifique-se de que os seguintes
requisitos estejam presentes no seu `setup.py` no atributo `install_requires=`.

```
grpcio
```

O gRPC també ofere o gRPC tools que auxilia da estrutura necessária para a
construção de projetos com gRPC, para instalar execute:

```
pip install grpcio-tools
```

> **Nota:** Perceba que o grpcio-tools não é um requisito da aplicação
> portanto não precisa ser listada como dependência, ela é apenas uma
> ferramenta para auxiliar na construção do projeto.

A estrutura do projeto contém um diretório para o código do cliente, um para
o códifo do servidor e um para a interface Protobuffer requireda pelo gRPC.

```
<raiz>
|
|___ cliente
|___ servidor
|___ protos
```

> **NOTA:** Os diretórios `cliente` e `servidor` são dois projetos distintos.

O diretório `protos` é a novidade aqui, nele estarão definidas as interfaces do
gRPC que utiliza Protocol Buffer que é uma linguagem nutra e indenpendente
de plataforma para serialização de dados.

o `grpc-tools` é a ferramenta oferica pelo gRPC para que depois de criada as
interfaces ele ger os Stubs (o código necessário para a interação entre
cliente e servidor, escondendo os detalhes do desenvolvedor). O código
é gerador na sua linguagem de escolha no nosso caso Python.

Para gerar os Stubs entre dentro da pasta do projeto `cliente` e dentro do 
pacote `grpc_client` (ou seja qual for o nome do seu pacote), rode o
seguinte comando no terminal.

```
python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/blog.proto
```

Novos fontes Python aparecerão no diretório e ele estará da seguinte forma:

```
<./grpc/cliente>
|___ grpc_cliente
|     |___ __ini__.py
|     |___ blog_pb2.py       # Arquivo adicionado pelo gRPC-Tools
|     |___ blog_pb2_grpc.py  # Arquvio adicionado pelo gRPC-Tools
|     |___ main.py
```

Iremos importar e fazer uso de tipos definidos nestes arquivos em nosso '
código. Confira o código de `main.py` e como ele importa esses módulos python
criados pelo `grpc-tools`. Faça o mesmo procedimento dentro da pasta
 `servidor`. Ele irá gerar os mesmos arquivos e com conteúdos idênticos.
 
> **NOTA 1:** Perceba aqui que qualquer mudança na interface (arquivos do
> diretório `protos`) deve ser seguido da atualização dos fontes Python
> portando você deve gerar os stubs novamente com o grpc-tools como fizemos
> agora.

> **Nota 2:** No caso de atualizaçã das interfaces os stups do cliente e do
> servidor devem sempre estar em sincronia. Se ambos estiverem rodando com
> versão diferentes da interface o programa irá falhar.

Execute o cliente e o servidor com o Docker, ou se preferir diretamente,
utilizando os seguintes comandos:


