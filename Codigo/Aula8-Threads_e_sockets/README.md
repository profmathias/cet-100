## Exercício

A partir do programa `ex4_threaded_server.py` e do `ex4_threaded_client.py
faça os seguintes experimentos:

- Analise o cliente e o servidor e tente encontrar o porque de não ganharmos
  desempenho com o sevidor sendo multithread.
- Faça uma versão onde o cliente envie dados utilizando o endereço de
  broadcast e o servidor a receba e tente responder ao cliente.
- Faça uma outra versão do exercício do fatorial sobre essa base de código.
    - use múltiplas threads 
- Tente criar um prompt no cliente, onde o usuário possa enviar diversas
  mensagens diferentes. O programa lê do teclado a mensagem e envia para o
   servidor, que retorar a seguinte mensagem 
   `Mensagem "<a mensagem enviada >" foi recebida às <data e hora>`
