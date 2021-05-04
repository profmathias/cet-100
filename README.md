# Bem-Vindo ao Repositório da Disciplina CET-100 Sistemas Distribuídos


## Metodologia e Planejamento

[Plano de Ensino](https://github.com/profmathias/cet-100/blob/master/CET100%20-%20Plano%20de%20Ensino.doc?raw=true)

## Aulas
- **Aula 12:** Preparação para o Projeto Final: Orquestração de App distribuído com Docker
  - [Gravação da Aula](https://drive.google.com/file/d/1OWXCxgoqyGrbr29gfh3IN6-8Xh0ptcMv/view?usp=sharing)
  - [Código Versão 1](https://github.com/profmathias/cet-100/tree/master/Codigo/docker-express)  
- **Aula 11:** Sincronização de Relógio (Parte 2)
  - [Slides](https://drive.google.com/file/d/11vIvqUfI2xsBRUwvribRIDtTxPwOC4z0/view?usp=sharing)
  - [Gravação da Aula](https://youtu.be/3Jc7vUQyk7A)
- **Aula 10:** Sincronização de Relógio (Parte 1)
  - [Slides](https://drive.google.com/file/d/11vIvqUfI2xsBRUwvribRIDtTxPwOC4z0/view?usp=sharing)
  - [Gravação da Aula](https://drive.google.com/file/d/11vIvqUfI2xsBRUwvribRIDtTxPwOC4z0/view?usp=sharing)  
- **Aula 9:** Nomeação em SD
  - [Slides](https://www.icloud.com/iclouddrive/0mPZnFuCoUkmo6s7N8tPXrx7w#Aula-8)
  - [Gravação da Aula](https://drive.google.com/file/d/1-IdruiKfwIUdcBMt3CjOarqy5nZu9XRn/view?usp=sharing)
- **Aula 8:** Containers com Docker
  - [Código Exemplo](https://github.com/profmathias/cet-100/tree/master/Codigo/exemplo_docker)
  - [Gravação da Aula](https://drive.google.com/file/d/1eYhYE3qao3KKxwKql91NNJ5ozYrSJTXX/view?usp=sharing)
- **Aula 7:** Migração de Código
  - [Slides](https://www.icloud.com/iclouddrive/0Kp_ZQeSSwKdqHWISNyeMpv9Q#Aula7)
  - [Gravação da Aula](https://drive.google.com/file/d/1zN6khvtNbBtX7jlQzBgTur9xum8Bd9Ff/view) 
  - Exercício: Este exercício visa antecipar o próximo assunto.
    Modifique o código do exercício anterior para que o cliente
    possa encontrar os servidores sem que necessitem de antemão
    o IP, considere implementar um novo componente que resolva os
    nomes para o IP do servidor. O IP deste novo serviço pode
    ser conhecido pelos clientes.
- **Aula 6:** Virtualização em SD e Cliente/Servidor
  - [Slides](https://www.icloud.com/iclouddrive/0yJCGjt764dJqekMICvNdYHuw#Aula6)
  - [Gravação da Aula](https://youtu.be/Vdf0W95xTeI)
  - **Atenção:** Entrega do exercício com Sockets e Threads na próxima 
    Quarta-Feira.  
- **Aula 5:** Processos em SD: Threads
  - [Slides](https://www.icloud.com/iclouddrive/0M5Biz0ov78L2VBuTMkTkIXog#Aula5)
  - [Gravação da Aula](https://drive.google.com/file/d/1stzklOvgyRvsATggHhemcVLRqIh4o0Rt/view?usp=sharing)
  - **Exemplo visto em Sala de Aula**: [Sockets e Threads com Python](https://github.com/profmathias/cet-100/tree/master/Codigo/Exemplos/hello_world_com_threads_e_sockets)
  - **Exercício:** Modifique este exemplo para que **O SERVIDOR**
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
- **Aula 4:** Arquitetura de Sistemas Distribuídos
  - [Slides](https://www.icloud.com/iclouddrive/0RLFGBmH-fDzqDexK4bQSik-g#Aula4)
  - [Gravação da Aula](https://drive.google.com/file/d/1F8F97Hp-gvWic5PMdLZ6g0PBcti99ku8/view?usp=sharing)
- **Aula 3:** Tipos de Sistemas Distribuídos
  - [Slides](https://www.icloud.com/iclouddrive/0pa25O-TUs1mtA3rFaia2ulLA#Aula3)
  - [Gravação da Aula](https://drive.google.com/file/d/1XsScNFBjz5_6z5jDVQt1JfDm5_pdqzWV/view?usp=sharing)
  - **Exercício 1:** Com base no [código exemplo](https://github.com/profmathias/cet-100/tree/master/Codigo/aula1-exemplo1) visto em sala de aula, 
  mdoifquei-o para criar rotas de uma aplicação, outra que não o sistema de 
  blogs. Utilize a criatividade ou escolha um sistema de sei interesse, como
  e-commerce, gerenciamento de estoques, um jogo, etc. O exemplo visto em sala
  de aula implementa uma interface de comunicação utilizando HTTP com Python e
  o framework Flask. Modifique-o para criar as interfaces para as operações 
  para a sua solução. [Clique para ir para o código exemplo](https://github.com/profmathias/cet-100/tree/master/Codigo/aula1-exemplo1)
- **Aula 2: Características e Desafios na Implementação de um SD**
  - [Slides](https://www.icloud.com/iclouddrive/0t3Xd2p_v6FeXuDC5_PEu5okQ#Aula2)
  - [Gravação da Aula](https://drive.google.com/file/d/1NAYw7F8lkYKX-auhcVdXlCTSkR0CxHmO/view?usp=sharing)

- **Aula 1: Apresentação da Disciplina e Introdução a SD**
  - [Slides](https://www.icloud.com/iclouddrive/0z8lgr8LK7aqR8vVlMRaT7MBA#SD)
  - [Gravação da Aula](https://drive.google.com/file/d/1gEIy9955tU-6wbG9qIr3drPOpTEYKkN6/view?usp=sharing)
  
#### Sobre as  Videoaulas

**Atenção:** As videoaulas só são acessíveis com o uso do e-mail institucional (`@uesc.br`).


## Frameworks para Desenvolvimento de APIs HTTP

### Python

- [Flask:](https://flask.palletsprojects.com/en/1.1.x/) Framework HTTP para criação de API com suporte a templates HTML
- [Connexion:](https://pypi.org/project/connexion/) Framework para desenvolvimento de APIs HTTP utilizando o conceito de API First Design ou API-Driven Development.

### Java
- [Spring Boot](https://spring.io/projects/spring-boot): Framework da familia *Spring* para a criação de APIs baseadas HTTP. Muito estável e com um alto nível de maturidade.

### Docker

- [Página Oficial (Inglês)](https://www.docker.com)
- [Tutorial hands-on oficial Play With Docker. Muito bom para praticar. (Inglês)](https://www.docker.com/play-with-docker)
- Tutorial em Português - Introdução ao Docker - por Cássio Ferraz
  * [Parte I](https://medium.com/@ferrazcassim/introdução-ao-docker-parte-i-7c6ecad3b4fd)
  * [Parte II](https://medium.com/@ferrazcassim/introdução-ao-docker-parte-ii-b44666837d37)
  * [Parte III](https://medium.com/@ferrazcassim/introdução-ao-docker-parte-iii-a675dfbea11e)
