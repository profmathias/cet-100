# Processos ao invés de Threads 

No exemplo desse diretório modificamos o programa Thread e Sockets para que
ele utilize processos.

## Multithreads vs Multiprocessos 

Primeiro, vamos esclarecer que todos os programas que você cria, ao executá-lo
o SO cria um processo que inicia os recursos necessário para o seu programa e
executa o seu código. 

### Ainda sobre Multithreads

Ao utilizar Threads dentro de um mesmo processo, as
Threads estã compartilhando o espaço de memória deste processo. Qual o
perigo das Threads?

- Elas concorrem por recursos.
- É necessário controlar o acesso a porções do código que múltipla Threads
  podem acessar. Para isso utiliza-se Locks e Semáforos.
    - O mal uso de locks e semáforos podem levar a Dead Locks, ou seja, uma
      Thread obteve o Lock e nunca o liberou.
    - Esse gerenciamento dependendo da aplicação pode começa a se tornar
      muito complexo.
      
Qual a vantagem do uso de Threads?

- São leves e de baixo custo para o SO.
- O comparilhamento do espaço de memória é mais rápido que outras formas de
  compartilhamento de dados.
- E obviamente, Permite a execução de códigos em paralelo.

### Multiprocessos

Programação com multiprocessos se refere ao fato de o processo principal de
um programa disparar outros processos que irão executar em paralelo com o
processo principal. Neste aspecto ele tem o mesmo objetivo das threads, 
permitir a execução de múltiplas sequências de código em paralelo. Mas qual
a diferença?

> A principal diferença entre multithread e multiprocessos é que os
> processos não compartilham um espaço comum de memória, todos possuem um
> escopo de memória próprio, sendo assim eles não conseguem compartilhar
> dados acessando diretamente.

Os processos precisa de outros meios para se comunicarem que não seja o
compartilhamento de memória, eles precisam utilizar algum tipo de
mecanismo de comunicação entre processos, o que pode tornar a lógica de
compartilhamento relativamente complexa, se por um lado os Threads precisam
se assegurar que duas Threads não acessarão certas porções de código
simultaneamente com Locks e Semáforos, uma aplicação multiprocesso precisa
construir toda uma lógica para permitir a comunicação entre os processos.

Mais quais as vantagens de utilizar Multiprocessos?

- Exclui complemtamente as condições de corrida, portanto reduz a
  possibilidade de Dead Locks.
- O escalonamento dos processos ficam a cargo do SO e os processos pode ser
  indepentes do processo que o gerou.

Note que Dead Locks podem continuar ocorrendo, especialmente se um processo
aguarda dados de um outro, que por algum motivo, nunca enviará.  

E quando utilizar processos? 

- Quando a porção de código que vai executar não está fortemente acoplado
  com o código da aplicação porém oferece um serviço essencial.
- Quando se deseja isolar completamente a memória dos processos.

Quais são as desvatanges:

- Comunicação interprocesso pode ser complicado de implementar.
- Tempo maior de inicialização.
- Consome mais memória.

### Multiprocessos e Multithreads em Python

Em Python Threads não executam em múltiplos núcles do Processador, essa
é uma das maiores deficiências do Python. Portanto para se obter ganhos de
performance com paralelismo, necessitamos utilizar o pacote `multiprocessing`.
Para a sorte de muitos, Python implementa a mesma interface para os módulos
`threading` e `multiprocessing`.


