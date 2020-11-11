# Projeto Python com Vagrant

Muitas vezes vamos querer testar o nosso código em uma máquina completa e
talvez um container não seja desejável. Nesses casos podemos utilizar o
Vagrant no lugar do Docker. O vagrant assim como o docker possui uma interface
amigável que permite a configuração e a execução de máquinas virtuais de
maneira fácil. Assim como o docker depende de um `Dockerfile`, o vagrant se
baseia no `Vagratfile`.

> **Atenção:** O Vagrant depende de um Monitor de Máquina Virutal para rodar as
> VMs o Virtual Box é a solução mais utilizada.

No diretório `esqueleto` deste diretório, você encontra um projeto simples
pronto para ser utilizado e já com um Vagrantfile configurado para executar
o código Python na VM. Porém caso queira iniciar um novo projeto do zero, o
Vagrant oferece uma opção simples para criar um `Vagrantfile` inicial, para
isso basta executar o seguinte comando:

```
$ vagrant init
```  

Para iniciar a VM, faça:

```
$ vagrant up
```

E para acessar a VM, faça:

```
vagrant ssh
```

Simples assim, o vagrant compartilha automaticamente a pasta onde o
Vagrantfile se encontra, os arquivos desta pasta podem ser encontradas no
diretório `/vagrant` dentro da VM. Sendo que o Vagrantfile está exatamente
no diretório do nosso projeto, podemos acessar a VM com `vagrant ssh` e
instalar o pacote, com os seguintes comandos:

> **OBS:** Podemos configurar o Vagrantfile de forma que ele execute
> este comando para nós quando iniciarmos a VM, veja o Vagrantifle do
> esqueleto

```
meu-computador$ vagrant ssh
vm$ cd /vagrant
vm$ pip install -e .
```

A opção `-e` no pip faz com que a instalação do nosso projeto seja sensível
a mudanças no arquivo, sendo assim enquanto editamos os arquivos no IDE eles
são atualizado na VM, portanto se executarmos o projeto na VM ele executar
á a versão mais recente do código. 

## Usando o esqueleto

Utilize o esqueleto como ponto de partida para o seu projeto Python, depois
basta iniciar a VM com o vagrant, acessar e rodar o seu programa lá dentro.
Algumas IDEs como PyCharm oferece suporte ao Vagrant permitindo que ao
apertar o botão de executar o programa seja executado automaticamente na VM.  
