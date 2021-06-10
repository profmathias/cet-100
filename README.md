# Bem-Vindo ao Repositório da Disciplina CET-100 Sistemas Distribuídos


## Metodologia e Planejamento

[Plano de Ensino](https://github.com/profmathias/cet-100/blob/master/CET100%20-%20Plano%20de%20Ensino.doc?raw=true)

## Seminários Datas

| Aluno      | Tema                        | Data   |
|------------|-----------------------------|--------|
| Diego      | Tolerancia a Falhas         | 15/jun |
| Ramon      | Seguranca                   | 15/jun |
| Adrian     | Sis. Arquivos Distribuidos  | 15/jun |
| Saionara   | Seguranca                   | 17/jun |
| Maira      | Consistencia e Replicacao   | 17/jun |
| Joao       | Tolerancia a Falhas         | 17/jun |
| Jesulino   |                             | 22/jun |
| Joao Pedro |                             | 22/jun |


## Aulas

- **Aula 20: Avaliação do Andamento do Projeto**
  - [Gravação da Aula](https://drive.google.com/file/d/1-goL_tDgW9Jov0zFRNQuiFfGESNw52kp/view?usp=sharing)
  - **PARA ENTREGAR NA PRÓXIMA AULA**
    - Modificação do `/info`, ele deve agora retornar uma lista dos servidores
      conhecidos, deve ser adicionado um atributo "servidores_conhecidos", ex.
      ```json
      {
        "componente": "server",
        "versao": "0.1",
        "descrição": "serve os clientes com os serviços X, Y e Z",
        "ponto_de_acesso": "https://meu-app-sd.heroku.com",
        "status": "up",
        "identificacao": 2,
        "lider": 0,
        "eleicao": "valentao",
        "servidores_conhecidos": [
          {
            "id":  "id_server_1",
            "url": "url_server_1" 
          },
          {
            "id":  "id_server2",
            "url": "url_server2"
          }
        ]
      }
      ```
    - Adição de método para `/recurso` que indica se o recurso está ocupado ou
      não `ocupador` pode ser `true ou false`.
      - [GET] /recurso
        - Retorno:
          ```json
          {
            "ocupado": false
          }
          ```
      
    - Implementar os endpoints:
      - [GET] /eleicao
        - Retorno:
          ```json
            {
              "tipo_de_eleicao_ativa": "valentao",
              "eleicao_em_andamento": false
            } 
          ```
      - [POST] /eleicao
        - Dispara o processo de eleição baseado no algoritmo atualmente ativo.
        - Note que ao ativar o processo de eleição o seu server deverá disparar
        requisições para outros servers se necessário, esse processo pode ser
        disparado em uma nova Thread enquanto que você retorna OK 
        como resposta à chamada a `/eleicao`.
        - A requisição deve conter o id da eleição no corpo da mensagem. Ex.
          - ```json
            {
              "id": "algum_id_como_string"
            }
            ```
        - No desdobramento do processo de eleição, ou seja nas mensagens 
          que você enviar na sequência como parte do processo para o 
          `/eleicao` dos outros servers, o `id` da eleição deverá ir junto 
          "SEMPRE", exatamente como no formato acima. Isso garantirá que cada
          server saiba à qual eleição ele está respondendo/reagindo.
      - [POST] /eleicao/coordenador
        - Recebe o id do novo coordenador no formato:
        ```json
        { 
          "coordenador": 2,
          "id_eleicao": "o id da eleição"
        }
        ```
        

- **Aula 19: Atividade em Classe - Projeto** 

- **Aula 18:** Algoritmos de Eleição
  - [Slides](https://www.icloud.com/iclouddrive/0YE3SftpNOOKMDxdl16Pnnghw#Aula-Eleic%CC%A7a%CC%83o)
  - [Gravação da Aula](https://drive.google.com/file/d/1EoDcpc71rYh-Q2Eh6bVqucXVWjncSTKz/view?usp=sharing)
  - **Instruções para etapa 2 do Projeto:** Ver o final dos slides dessa aula.
  - **Exemplo de JSON retornado pela rota `/info`**
    - ```json
      {
        "componente": "server",
        "versao": "0.1",
        "descrição": "serve os clientes com os serviços X, Y e Z",
        "ponto_de_acesso": "https://meu-app-sd.heroku.com",
        "status": "up",
        "identificacao": 2,
        "lider": 0,
        "eleicao": "valentao" 
      }
      ```
- **Aula 17:** Cloud com Heroku - Implantação
  - [Gravação da Aula](https://drive.google.com/file/d/1Bawa3BRulX53uD6Z7L13Ml73wHQUAkQR/view?usp=sharing)
    - Atenção para a gravação a partir do minuto 36, que é qunado os 
      comandos rodam sem problemas.
  - [Código visto em Aula](https://github.com/profmathias/cet-100/blob/master/Codigo/docker-express)
  - **Exercício para a próxima aula**
    - Faça a implantação do componente `server` do seu projeto no Heroku.
    - Em caso de dúvidas entrar em contato pelo Discord.
- **Aula 16:** Seminários
  - Escolha um tema de sua preferência dentre os listados abaixo no livro 
    texto: Sistemas Distribuídos - Tanenbaum, e prepare um seminário de 30 
    minutos sobre o tema. As apresentações serão na semana do dia 15 - 24/06.
      - Tolerância a Falhas
      - Segurança
      - Sistemas de Arquivos Distribuídos
      - Consistência e Replicação
    Serão 3 apresentações por aula. O seminário irá valer uma nota.
  - Implemente no módulo servidor do seu projeto uma rota chamada `/recurso`.
    Ela deve simular o controle de acesso a um recurso. 
    A sua função deverá disparar uma Thread que ao final de um tempo (10 seg)
    especificado (use`sleep`), irá liberar um Lock (revejam a aula de 
    threads ou o [doc do python](https://docs.python.org/3/library/threading.html#lock-objects)).
    Quem estiver utilizando JavaScript pode usar `setTimeout` 
    para mudar o Lock que pode ser uma variável simples, por exemplo, chamada 
    `ocupado`. Depois da primeira requisição solicitando acesso, o sistema irá 
    travar o Lock e irá responder com `409 conflict`, após 10 segundos ao 
    liberar o Lock, a próxima requisição será atendida e o processo se repete.
  - Esse exercício servirá de base para implementarmos um controle de 
    acesso a recurso descentralizado bem como um algoritmo de eleição cuja 
    coordenação ocorrerá entre as instâncias dos servidores de todos os 
    alunos da disciplina.  
- **Aula 15:** Preparação de Repositório e Código Base do Projeto Final
  - Nesta aula, até o final, os estudantes deverão:
    - Criar uma organização no GitHub com nome SD-<Matrícula do Aluno>
    - Criar 4 repositórios dentro desta organização
        - client
        - server
        - nameserver
        - resourcemanager
        - orchestracao
    - Todos os repositórios deverão ter uma implementação básica baseada nos 
      exemplos visto em sala de aula, todos devem iniciar um servidor http 
      (pode-se usar Python/Flask ou Javascript/Express.js). TODOS devem ter
      uma rota chamada GET:"/info" que retorna um JSON contendo as seguintes 
      informações:
      ```json
      {
        "componente": "server",
        "descrição": "serve os clientes com os serviços X, Y e Z",
        "versao": "0.1" 
      }
      ```
    - Todos os repositórios devem possuir um Dockerfile que crie um container 
      funcional do serviço. Deve ser possível, se dentro do diretório de um 
      repositório (ex. server) fazer o seguinte:
      ```
      $ docker build -t server .
      $ docker run server
      ```
      Logo após uma consulta à rota `/info` deve retornar (note que você 
      deve ajustar a porta):
      ```
      $ curl -XGET http://127.0.0.1:8000/info
      {
        "componente": "server",
        "descrição": "serve os clientes com os serviços X, Y e Z",
        "versao": "0.1" 
      }
      $
      ```
    - O repositório `orchestracao` deve ter um arquivo `docker-compose.yml`
      e caso queira scripts para fazer o pull dos repositórios e criar as 
      imagens docker, você pode optar por criar as imagens docker manualmente
      entrando em cada repositório e rodando `docker build <opcoes>`. Ao 
      executar o arquivo com o comando `docker-compose` todos os 
      componentes devem ser iniciados. Adicione no `docker-compose.yml` um
      serviço de banco de dados, recomendado o MongoDB.
    - **Dicas:**
      - Use Linux instalado nativamente no seu computador se possível.
      - Use as imagens node:14-alpine (para Node.js) ou python:3.9-alpine 
        para (Python), essas imagens são leves e bem pequenas e consomem 
        menos recursos do computador.
      - Caso o computador fique lendo quando você estiver utilizando o Docker
        feche as IDEs e use a linha de comando `docker`.
  

- **Aula 14:** Programação Assíncrona (Javascript)
  - [Tutorial  e Códigos de Exemplo](https://github.com/profmathias/cet-100/tree/master/Codigo/async-com-javascript)
  - [Gravação da Aula](https://drive.google.com/file/d/1A7CxljP__HngJpJu5OvUrJDMKVL2lhYv/view?usp=sharing)  
- **Aula 13:** Preparação para o Projeto Final (Parte 2): Orchestração de 
  App Distribuído - **docker-compose**
  - [Gravação da Aula - Correção de Erro](https://drive.google.com/file/d/1wmrK-qH1u_Q76XhXSQovaLRJHXgC8L-b/view?usp=sharing)
  - [Gravação da Aula](https://drive.google.com/file/d/1q49lh3Wg6vynO0vK46LZVJPyFVn8zJTQ/view?usp=sharing)
  - [Código da Aula](https://github.com/profmathias/cet-100/tree/master/Codigo/docker-express)  
- **Aula 12:** Preparação para o Projeto Final (Parte 3): Orquestração de App 
  distribuído - **docker**
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
