Este exemplo consiste em um programa servidor e um cliente. O servidor inicia
um `socket` e fica aguardando por conexões. Ao aceitar uma conexão vinda de um
cliente o servidor imediatamente envia uma mensagem “Hello World!” para o
cliente. O cliente então imprime a mensagem na tela. O servidor é multithreaded
e trata cada conexão em uma thread separada. Uma operação `sleep` é adicionada
no servidor para simular um processamento longo da requisição. 

Por sua vez, o cliente é um programa simples que cria um `socket` e chama a 
operação `connect` para conectar ao servidor. Após a conexão aciona a 
operação `recv` para receber a mensagem “Hello World!” enviada pelo servidor.

Exercícios Propostos:

1) Modifique este exemplo para que **O SERVIDOR**
   receba um vetor contendo números inteiros além de um número inteiro. O
   número passado deverá ser encontrado no vetor e o servidor responderá o
   cliente com o valor do índice no vetor onde o valor foi encontrado ou `-1`
   caso nada tenha sido encontrado. Você deverá executar 2 ou mais instâncias
   do servidor cada um em uma porta diferente. **O CLIENTE**
   deverá gerar um vetor de tamanho N preenchido com números aleatórios. Este
   vetor deve ser particionado pelo número de instâncias de servidor executando
   e cada parte enviada para uma dessas instâncias. Junto com o pedaço do
   vetor, o cliente deverá também enviar o número a ser buscado para cada
   servidor. **Suponha** que o cliente possui o
   vetor `[1, 2, 0, 9, 3, 7, 8, 5]` e deseja buscar pelo valor `9`. O cliente
   deverá enviar um vetor `[1, 2, 0, 9]` para a primeira instância do servidor,
   e o restante `[3, 7, 8, 5]`. O número a ser buscado também é enviado, no
   caso o `9`. Recebido os dados pelos servidores eles devem retornar o 
   resultado e o cliente deve imprimir o índice onde o número se encontra, 
   nesse caso `3`.
