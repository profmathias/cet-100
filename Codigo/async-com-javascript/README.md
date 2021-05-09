# Assincronia com Javascript

## O que é um código assíncrono?

Um código assíncrono a grosso modo é um código que permite a execução não
sequencial de código. Isso não significa execução de código de maneira paralela
como é o caso de programas multiprocessados ou multithreads. Qual a diferença
então?

Muitas funções podem demorar muito para serem executadas devido à espera de
operações de Entrada/Saída (E/S), essas operações são custosas, pois a
velocidade com que elas ocorrem é muito menor quando comparada com a velocidade
do processador. Operações de acesso a disco e em especial o envio e recepção de
dados através da rede são impactados não só pela velocidade dos dispositivos,
mas também pela quantidade de dados sendo lida/escrita ou recebida/enviada.

A ideia por traz dos códigos assíncronos então, é fazer com que o código não
bloqueie em uma operação de espera por E/S. O programador então marca a
operação como assíncrona. Ao marcar a operação como assíncrona a operação
permite com que outras partes do código seja executada enquanto aquela operação
estiver bloqueada à espera da resolução de uma operação de E/S.

Os códigos assíncronos conseguem extrair o máximo do processador aumentando
muito a performance dos programas, especialemente aqueles que são
constantemente bloqueados por operações de entrada e saída (ex. Rede, Disco).

Veja a seguinte função abaixo em javascript:



> **NOTA:** Funções e métodos assíncronos são muito úteis para aplicativos que
> fazem muitas operações de entrada e saída, isso é especialmente útil para
> aplicativos que fazem uso intenso da rede. As requisições são tratadas por
> funções assíncronas, o que libera o fluxo de execução enquanto a
> mensagem não é integralmente recebida, permitindo que outras
> requisições sejam atendidas.

## Como criar código assíncrono (JavaScript)

Existem diversas maneiras, nas mais diversas linguagens, de se criar código
assíncrono. Em javascript você pode utilizar `callbacks` e o loop de eventos.
Podemos dizer que javscript é uma linguagem **assíncrona**, **concorrente** e 
**não bloqueante**. Para entendermos como isso funciona vamos entender o que
é a **pilha de execução** e a **fila de callbacks**.

```                                          
                                             +----------------+
Call Stack                           +-------|   Async APIs   |
 +------+                            |       +----------------+
 |      |----------------------------+                | 
 |      |                                             |
 |      |       +-------------+                       |
 | f4() | ------|  Event Loop | --------+             |
 | f3() |       +-------------+         |             |
 | f2() |                   +-----------------------------------+
 | f1() |          Callback | onFileReady() |  onPackageReady() |             
 +------+            Queue  +-----------------------------------+
 
 Figura 1: Uma representação básica do functionamento da Engine JavaScript.
```

**Call Stack** é a pilha de chamadas de função, conforme o seu código executa
funções são chamadas e quando isso acontece essa função é posta na pilha. Se
ela não chama nenhuma outra função ela é executada e tirada da pilha. Se ela 
chama uma função dentro dela ela interrompe a execução dela é interrompida e
a função chamada dentro dela é colocada na pilha e colocada em execução. No
exemplo acima podemos perceber que f1() ocorre e chama f2(), que por sua vez
chama f3(), que invoca f4(). 

Suponha que f4() é uma função de uma biblioteca assíncrona, ele coloca a 
função na pilha e a executa. Em geral, quando invocamos uma função assíncrona
passamos uma função como parâmetro, que será a função de callback executada 
quando um determinado evento ocorrer, por exemplo, uma interrupção do 
sistema indicando que um arquivo foi lido ou um pacote recebido. 

As chamadas de funções das APIs servem para informar a API que ela deve
prosseguir com a execução em plano de fundo utilizando os parâmetros informados
o que inclui a função de callback. A API fica responsável por monitorar a
execução daquela tarefa, ex. leitura de um arquivo. Quando o arquivo está
pronto a função de callback é colocada na Fila de Callback (Callback Queue).
Toda a vez que a Pilha de Chamadas (Call Stack) está vazia o Event Loop tira 
uma função `callback` da fila e coloca na pilha de execução.

Vejamos um exemplo em javascript:

```javascript
//Exemplo 1: Lendo arquivo de maneira síncrona
import fs from "fs";

const conteudo = fs.readFileSync("exemplo.in", "utf-8");
console.log(conteudo);
console.log("Finalizado!")
```

Supondo que o arquivo `exemplo.in` tenha como conteudo a string 
`Hello World!\n`, o resultado da execução do script acima será:

```
Hello World!
Finalizado!
```

O programa acima usa o módulo `fs` para ler um arquivo do disco. Suponha que
esse arquivo seja grande o suficiente para levar 5 segundos para ser lido em
sua totalidade, 5 segundos é uma eternidade para o processador. O seu código
poderia tentar resolver outras coisas enquanto o arquivo não fica pronto. A
operação de leitura do arquivo é feita pelo sistema operacional e o seu código
está parado aguardando-o. Seria interessante se pudessemos, durante a execução
do código, marcar essa como uma operação custosa e bloqueante e liberar o fluxo
de execução para que o programa realize outras tarefas ao invés de ficar a
espera do arquivo. Perceba o uso da função `fs.readFileSync`, ela é uma
operação síncrona, ou seja ela vai bloquear e esperar o resultado sem liberar o
fluxo de execução, em outras palavras ela é muito custosa para o desempenho do
seu aplicativo.


### Assincronia com Callbacks

Podemos tornar o código acima assíncrono, utilizando a função assíncrona de 
leitura de arquivo do módulo `fs` do Node.js runtime. Como faríamos isso então?
A função `readFile` do Node.js é assíncrona, logo ela não vai bloquear. Ao 
invés disso informamos a ela qual código ela deve executar quando estiver o 
arquivo estiver pronto. Note que imprimíamos `Finalizado!` depois de imprimir
o conteúdo do arquivo, queremos manter o mesmo comportamento. 

````javascript
//Exemplo 2: Lendo arquivo de maneira assíncrona.
import fs from "fs";

fs.readFile("exemplo.in", "utf-8", (conteudo) => {
  console.log(conteudo);
})
console.log("Arquivo Lido!")
````

A saída do programa acima é:

```
Arquivo Lido!
Hello World!
```

O código é assíncrono e o resultado não foi o que esperávamos,
o `Arquivo Lido!` foi impresso antes do `Hello World!`. Isso se dá justamente
pelo fato de estarmos utilizando uma função assíncrona para ler o arquivo. O
readFile é uma função do Node.js, quando você a executa, o seu programa pede 
para o Node cuidar da abertura do arquivo e colocar a função de calback na fila
de callbacks quando tudo estiver pronto. O programa então, segue o fluxo de
execução. O processo de leitura de arquivo é lento, e como a função 
`readFile` é assíncrona a próxima linha do código é então executada e imprime 
na tela `Arquivo Lido!`. Algum tempo depois o Node termina de ler o arquivo,
coloca a função de callback na fila de callbacks. O event loop então escalona
o callback e a coloca na pilha quando possível. O callback é executado o 
conteúdo impresso na tela e só então o programa é encerrado.

Para resolvermos o problema acima devemos mover a impressão de `Arquivo Lido!`
para dentro do `callback`.

Muitas das funções oferecidas pelo Node.js são assíncronas e utilizam o 
esquema de callbacks para implementar essa sincronia. Quando for utilizar uma
função é de suma importância que saiba se ela é síncrona ou assíncrona.


### Assincronia com Promise (Promessa)

Uma `Promise` em javascript, e em outras linguagens, é um objeto que intermedia
o acesso a um valor ainda não conhecido durante a criação da `Promise`. Funções
assíncronas podem retornar uma `Promise` que pode ser utilizada para obter 
o valor da operação assíncrona quando ele estiver disponível.

Ao criar uma `Promise` a função que é passada como argumento é colocada em 
execução e o fluxo do programa continua normalmente enquanto a `Promise` é
resolvida (a função executada). Para encerrar a função de uma promise deve ser
chamada o primeiro argumento da função `resolve(value)` com o valor que deve
ser retornado pela `Promise`, ou `reject(motivo)` caso voceê queira indicar um
erro ocorrido durante a execução. Vamos ver um exemplo:

```javascript
//Exemplo 3
const promise = new Promise(function (resolve, reject) {
  const numero = Math.floor((Math.random()*2));
  if(numero === 0) {
    resolve("Ok!");
  }
  else {
    reject("Falha!");
  }
});

promise.then((value) => console.log(value))
       .catch((motivo) => console.log(motivo));

console.log("Promise Executando...");
```

O programa acima irá imprimir o seguinte:

```
Promise Executando...
Falha! 
```

A última linha irá varia entre `Ok!` e `Falha!` a depender do valor da 
variável número 

No código acima uma `Promise` é criada, ela recebe uma função como 
argumento escrevemos então uma função `inline`, essa é a tarefa que queremos
realizar de maneira assíncrona. A tarefa é criar uma variável com um valor 
aleatório entre `0` e `1`, caso o número seja `0` a `Promise` termina com 
sucesso e caso seja `1` a `Promise` falha.

Depois de criarmos a `Promise` podemos registrar callbacks para serem 
executados quando ela for resolvida fazemos isso chamando o método `then` e 
passando uma função de callback como parâmetro. A função `then` retorna a 
própria `Promise` então se pode chamar o `then` várias vezes, o que é 
conhecido como `chaining`. Vejamos o exemplo abaixo (omitimos a declaração 
da `Promise`). 

```javascript
//Exemplo 4

//Declaração da Promise igual a anterior
//Omitida...

promise.then((value) => console.log("Callback 1: Promisse Ok!"))
       .then((value) => console.log("Callback 2: Promisse Ok!"))
       .then((value) => console.log("Callback 3: Promisse Ok!"))
       .catch((motivo) => console.log(motivo));
```

Perceba que como `then` retorna a prórpia `Promisse`, podemos continuar 
adicionando `callbacks` com `then`. É possível também chamar o `then` com 
dois argumentos `then(callbackDeSucesso, callbackDeErrro)`. Assim você pode
tomar ações diferentes dependendo do estado da `Promise`.

```
promise.then((value) => console.log("Callback 1: Promise OK! " + valor),
             (error) => console.log("Callback Erro: " + error)
```

Geralmente o erro é tratado pelo `callback` registrado com `catch()` porém 
você pode registar `callbacks` de erro também. Existe uma fila de `callbacks` 
e eles serão chamadas em ordem de registro. Se tratado no then, os outros
`callbacks` registrados com `then` serão invocados. Por exemplo:

```javascript
//Exemplo 5

//Declaração da Promise Omitida! Continua a mesma.

promise.then((value) => console.log("Callback 1: Promisse Ok! " + value),
              (erro) => {console.log("Error Callback 1 - " + erro); console.log("Erro capturado no then 1");})
       .then((value) => console.log("Callback 2: Promisse Ok! " + value),
             (erro) => console.log("Error Callback 2 - " + erro))
       .then((value) => console.log("Callback 3: Promisse Ok! " + value),
             (erro) => console.log("Error Callback 3 - " + erro))
       .catch((erro) => console.log("Error Callback 4 - " + erro));
```

```
Error Callback 1 - Falha!
Erro capturado no then 1
Callback 2: Promisse Ok! undefined
Callback 3: Promisse Ok! undefined
```

As funções de `callback` podem retornar um valor, este valor será o valor 
recebido pelo próximo `then`. Se este valor for uma `Promise` o próximo then
só será quando essa `Promise` for resolvida. Ex:

```javascript
function esperar(tempo) {
  return new Promise(((resolve, reject) => setTimeout(resolve, tempo)));
}

esperar(5000).then(() => {console.log("Encerrada! Após 5 seg"); return 
  esperar
(5000)})
  .then(() => console.log("Segundo then! Após 10 seg"));
console.log("Aguardando Promise ser resolvida!")
```
```
Aguardando Promise ser resolvida!
Encerrada! Após 5 seg
Segundo then! Após 10 seg
```

Ciramos no exemplo acima uma `Promise` que executa a função `setTimeout`, 
que utiliza o esquema de `callbacks` para asíncronia (como visto no início 
desde artigo), ela retorna imediatamente e agenda a execução da função 
`resolve` da promise depois da quantidade de tempo especificada. No caso do 
exemplo acima o segundo `then` não é executado imediatamente após o primeiro,
como `esperar` retorna uma `Promise` o `then` subsequente só será executado 
depois dessa `Promise` ser resolvida, sendo assim, o programa anterior irá 
demorar 10 segundos para ser executado.

Esse comportamento é útil no caso de chamadas dependetes umas das outras, 
por exemplo, você poderia desejar que uma URL fosse carregada somente se uma
primeira fosse carregada com sucesso.

### Assíncronia com async/await

As palavras chaves `async/await` são adições recentes ao Javascript. A 
intenção dessas palavras é facilitar a criação e o uso de funções assícronas.
Uma função marcada com `async` sempre retorna uma `Promise`, ou seja, `async`
facilita a criação de `Promises`. Essa `Promisse` é resolvida com o valor de 
retorno da função. Vamos ver um exemplo:

```javascript
async function soma(a, b) {
  return a + b;
}

const result = soma(10, 20);
console.log(result instanceof Promise);

result.then((value) => console.log("O resultado é: " + value));
```
```
true
O resultado é: 30
```

Pelo exemplo anterior percebemos com a operação `result instanceof Promise` que
o retorno da função é uma `Promise`. Já que temos uma `Promise` podemos 
registrar callbacks com o `then` para serem executadas quando a `Promise` 
for resolvida.

No exemplo anterior apesar de termos uma função assíncrona o seu código não 
possui chamadas a funções assíncronas, ou seja o código quando começa a 
executar irá até o final sem interromper a sua execução, que é o que 
geralmente acontece com funções assíncronas. Elas existem porque dentro 
delas existem operações assíncronas muitas vezes custosas, então elas 
liberam o interpretador para realizar outras operações. Vamos ver um outro 
exemplo:

```javascript
function esperar(tempo) {
  return new Promise(((resolve, reject) => setTimeout(resolve, tempo)));
}

async function somaLenta(a, b) {
  await esperar(5000);
  return a + b;
}

somaLenta(10, 20).then((value) => console.log(value));
console.log("Aguardando a soma...");
```
```
Aguardando a soma...
30
```

No exemplo acima reutilizamos a função `esperar` para simular uma operação
lenta `somaLenta`. A palavra `await` é utilizada para liberar o interpretador
enquanto a promise não é resolvida, a função ela bloqueia ali e não
executa a próxima linha até a `Promise` retornada por `esperar` for resolvida.

Ao executarmos `somaLenta(10, 20)`, por ser uma função `async` uma `Promise` é
retornada, então registramos imediatamente um `callback` com `then`. A soma 
é lenta e programa fica aguardando a resolução da `Promise`, só então o 
programa encerra.

Notem que dentro da função o `await` bloqueia, liberando a execução. Uma 
grande vantagem do `await` é que ele permite uma programação mais próxima 
da programação assíncrona em termos de sintaxe. Perceba que as linhas da 
função `somaLenta` é executada em sequência. Vamos ver outro exemplo:`

```javascript
function esperar(tempo) {
  return new Promise(((resolve, reject) => setTimeout(resolve, tempo)));
}

async function operacaoLenta(a, b) {
  let resultado = 0;
  console.log("resultado = ", resultado);
  await esperar(2000);
  resultado = a + b;
  console.log("resultado = ", resultado);
  await esperar(2000)
  resultado = resultado * 2;
  console.log("resultado = ", resultado)
}

somaLenta(10, 20).then((value) => console.log(value));
console.log("Aguardando a soma...");
```
```
resultado =  0
Aguardando a soma...
resultado =  30
resultado =  60
60
```

Perceba no exemplo acima como `operacaoLenta` é mais próximo do que 
programas síncornos. O `await` sempre libera o interpretador para executar 
algo enquanto a operação marcada não retorna. Veja como o primeiro `console.
log` é executado, porém ao executar o `await` logo abaixo a última linha de 
códgio é executada. Quando os dois segundos passa e a `Promise` do 
`esperar` é resolvida ele retorna para a execução da função `operacaoLenta` 
e imprime o resultado parcial até ser interrompida novamente pelo próximo 
`await`.

O resultado do await é o valor resolvido da `Promise`. Então podemos fazer 
o seguinte:

```javascript
// omitindo declaração das funções somaLenta e esperar

async function variasOperacoes() {
  x = await somaLenta(10, 20);
  y = await somaLenta(5, 5);
  z = await somaLenta(1, 1);
  
  return x + y + z;
}

variasOperacoes().then((value) => console.log(value));
console.log("Aguardando a soma...");

```
```
Aguardando a soma...
42
```

Note mais uma vez como a sintaxe do `async/await` está mais próxima da 
programação síncrona a qual estamos acostumados. Cada vez que o `await` é 
chamado em `variasOperacoes` a execução da função é interrompida. 

Por último, para você entender como o bloqueio do `await` funciona, vamos 
chamá-lo no escopo global.

```javascript
// omitindo declaração das funções somaLenta e esperar
// omitida a declaração da função variasOperacoes
let resultado = await variasOperacoes();
console.log(resultado);
console.log("Aguardando a soma...");
```
```
42
Aguardando a soma...
```

No exemplo acima estamos fazendo o código ficar síncrono, porque como o 
`await` esta sendo chamado no escopo global ele irá bloquear, caso alguma 
outra operação assíncrona estivesse pendente elas seriam executadas, mas 
neste caso `variasOpcoes` é a única operação assíncrona que invocamos o 
programa ficará ali aguardando a sua resolução.



