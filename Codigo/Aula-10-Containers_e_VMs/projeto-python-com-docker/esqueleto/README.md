# Instruções

Use esse diretório como o diretório raiz do seu projeto e para criar a imagem
docker para ser utilizada na criação de containers execute o seguinte
comando docker.

```
$ docker build -t minha_imagem .
```

Este comando irá criar uma imagem com o nome de `minha_imagem`, você pode
utilizar o nome que lhe convir. Estude em detalhes o arquivo 
`Dockerfile` é lá que vc encontrará os detalhes de como a imagem será 
montada, inclusive quais arquivos serão copiados para lá. Modfique-o de
acordo com as suas necessidades. Caso queira ter mais de um Dockerfile, você
pode criar múltiplos como por exemplo.

* Dockerfile.ubuntu
* Dockerfile.fedora
* Dockerfile.debian

Porém nos casos acima você precisará especificar o caminho para o arquivo, 
já que quando você não especifica o nome ele automaticamnete busca pelo
arquivo de nome `Dockerfile`, portanto o comando ficaria assim:

```
$ docker build -t minha_image -f Dockerfile.ubuntu
```

Note que  o docker constrói uma imagem por vez, portando você teria que
executar o comando acima para cada Dockerfile. 

Após criar suas imagens você pode conferir quais estão dsiponíveis para a
criação de um container utilizando o comando `docker image list` ou `docker
image ls`.

Para executar o seu container utilize do comando `docker run minha_imagem`
para que ele execute em segundo plano utilize a opção `-d` para utilizad o
modo daemon.

```
$ docker run -d minha_imagem
```

Parabéns, você acabou de rodar uma aplicação utilizando o Docker.

Os containers criados com o `docker run`, não são eliminados após a execução,
caso você deseje que ele seja destruído (cuidado ele apagará o container e
as informação que eventualmente foram armazenadas dentro dele) você pode
utilizar a opção `--rm`, sendo assim o comando ficaria da seguinte forma:

```
$ docker run --rm -d minha_imagem
``` 

Você também pode atribuir um nome ao container (note que esse nome não tem
relação com o nome da imagem, este é o nome do container) o qual você poderá
utilizar posteriormente para se referir ao container em outros comandos. Ex:

```
$ docker run --rm --name meu_container -d minha_imagem
```  

Você pode listar os containers em execução com o comando: 

```
$ docker ps
```

Caso queira a lista de todos os containeres em execução ou não adicione a 
opção `-a`.

```
docker ps -a
```

Por fim, para eliminar um container docker, certifique-se de que ele não est
á em execução, caso esteja pare o container com `docker stop meu_container` 
(você pode usar o id do container caso ele não tenha um nome.) e depois o
elimine com o comando `docker rm meu_container`, sendo assim a sequencia de
comandos ficaria:

```
$ docker stop meu_container
$ docker rm meu_container
```
