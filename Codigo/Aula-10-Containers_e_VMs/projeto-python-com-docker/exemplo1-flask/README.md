# Instruções

Este exemplo é baseado no `esqueleto` proposto anteriormente, a ideia
é termos um serviço Flask rodando dentro do container Docker. Após
implmenetar o programa, o processo para construção e execução do container 
são os mesmos mostrados na documentação do `esqueleto`. Você pode mudar o
nome do pacote python `app` bem como o nome do script em `setup.py`, porém
certifique-se de alterar as referências ao pacote e ao script nos arquivos
`setup.py e `  `Dockerfile`.

Note que adicionamos uma nova linha no `Dockerfile`, o comando `EXPOSE 5000`,
ele indica que o container irá expor a porta 5000 para receber conexões. Dessa
forma a porta estará disponível para conexões vindas de outros containeres
rodando nesta instalação Docker.

Para construir a imagem digite:

```
$ docker build -t minha_image_flask .
```

Substitua o nome da imagem `minha_imagem_flask` para o nome que quiser. 
Depois de construir a imagem crie e execute o container. E instrua o Docker
a export a porta 5000 (`-p 5000`) para conexões vindas de outros hosts e não
somente containeres como é o caso do `EXPOSE`. No caso do `-p 5000`, a porta
5000 do host será reservada não poderá ser utilizada por nenhum outro
processo. 

```
$ docker run --name meu_container -p 5000 minha_imagem_flask
``` 

Caso tenha mudado o nome da imagem ajuste o comando acima de acordo. 
Lembrando que para excutar o conteiner em segundo plano acrescente a opção 
`-d`. O `--name` dá um nome ao seu container, você poderá a partir daí
utilizar esse nome em operações futuras e também fica mais fácil
identificar o container que utilizou.

Diferente do aplicativo do skeleton esse container é um daemon, ele roda
indefinidamente até que seja instruido a parar. Caso vc tenha rodado o
container em primeiro plano digite `ctrl+c` para encerrar o container, 
nesse caso o aplicativo será encerrado e o Docker ao perceber isso encerra o
container, visto que a princípio não faz sentido mantê-lo rodando se o
processo principal foi encerrado. O container porém não será deletado.

Para ver os containers e o seu estatus digite:

```
$ docker ps -a
``` 

O menos `-a` instrui o comando a mostrar todos os containerers
independentemente do seu status, se omitido ele só mostrará os containeres
em execução. Na lista você verá um container criado a partir da imagem que
você criou.

Na documentação do esqueleto vimos como deletar o container, primeiro pare-o,
caso ainda esteja em execução, depois utilize a opção `rm`:

```
$ docker stop meu_container
$ docker rm meu_container
```
