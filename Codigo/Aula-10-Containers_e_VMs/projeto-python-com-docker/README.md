## Processos, Máquinas Virtuais e Container

**Livro Texto: Cápitulo 3**

### Resumo

Sistemas Distribuídos tem tudo a ver com uma multitude de processos sendo
executados paralelamente, distribuídos em diferentes máquinas e que se
comunicam através de um rede de comunicação. Nesta aula aprenderemos:

* Como criar processos em um programa.
* Como encapsular processos em um Container Docker, como executá-lo e como
  gerenci a-lo.
* Como encapsular processos em Máquinas Virtuais utilizando o Vagrant com
  Virtual Box.
* Falar sobre comunicação inter-processos.
  

### Containers e Docker

O Docker é um sistema gerenciador de containers, que por sua vez são
virtualização leve que se utilizam do sistema operacional do hospedeiro e 
não requer a instalação completa de um sistema operacional. O nível de
isolamento de um container em relação ao sistema operacional do hospeiro
é muito baixa, quando comparado com as Máquinas Virtuais, porém o que se
ganha com isso é desempenho. Containers tem um tempo de inicialização muito 
maior do que seus primos as Máquinas Virtuais.

Containeres tem sido utilizado com frequência para implantar sistemas na
nuvem e também para desenvolvimento, por exemplo, para executar testes em
ambientes com setups variados. Suponha que você deseja verificar se o seu
programa é compatível com múltiplas versões do Python, ou com diferentes
distribuições Linux. Com containeres essas tarefas se tornam mais simples e
fácil de automatizar.

Os containeres isolam o processo em um ambiente de execução com baixíssimos
priveilégios garantindo o isolamento do processo em relação a outros
processos executando na máquina, por exemplo, eles não possuem por padrão
acesso a dispositivos, à arvore do sistema de arquivos, etc.

Containers são iniciados geralmente a partir de uma imagem, que é basicamente
uma árvore de arquivos que simula o sistema de arquivos de um sistema Linux.
Os arquivos responsáveis por operações de baixo nível do SO são omitidos, 
praticamente somente as aplicações são instaladas no container, visto que ele
utiliza o sistema operacional da máquina hospedeira.

Ambientes de gerenciamento de containers podem criar redes de sobreposição
permitindo que os containers sejam conectados à rede, basicamente dois modos
são comuns:

* **Modo Bridge:** Onde o gerenciador de containers faz uma ponte entre uma
  interface de rede virtual no container para uma interface de rede física no
  hospedeiro.
* **Modo Overlay:** Onde o gerenciador cria uma rede virtual independente e
  usa a interface do hospedeiro como o gateway para a rede. Os containers
  podem se comunicar entre si dentro desta rede de sobreposição e quando
  querem ir para fora, vão através do gateway.
  
Apesar de limitar o acesso a muitos recursos do hospedeiro, os sistemas de
gerenciamento de containers, muitas vezes permitem escalar os privilégios
de um container, permitindo ele acessar recursos antes não autorizados.

Nesta aula veremos:
    
* Como criar uma imagem e um container.
* Como carregar o nosso programa no container para que seja executado.
* Como configurar o container e o seu acesso à rede.
* Como gerenciar o container.

#### Recursos

Neste diretório você encontrará um esqueleto de projeto para iniciar um
projeto utilizando containers. Também encontrá alguns exemplos para servir
de ponto de partida para os seus projetos.
