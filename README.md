# Bem-Vindo ao Repositório da Disciplina CET-100 Sistemas Distribuídos

* [Metodologia e Planejamento](#metodologia-e-planejamento)
  * [Seminários Datas](#seminarion-e-datas)
  * [Aulas](#aulas)
      - [Sobre as  Videoaulas](#sobre-as--videoaulas)
  * [Heroku Apps URLs](#heroku-apps-urls)
  * [Frameworks para Desenvolvimento de APIs HTTP](#frameworks-para-desenvolvimento-de-apis-http)
    + [Python](#python)
    + [Javascript](#javascript)
    + [Java](#java)
    + [Docker](#docker)

## Metodologia e Planejamento

[Plano de Ensino](https://github.com/profmathias/cet-100/blob/master/CET100%20-%20Plano%20de%20Ensino.doc?raw=true)

## Seminários Datas
<a name="seminarion-e-datas"></a>

Os seminários ocorrerão nas seguintes datas, os temas que podem ser escolhidos
para apresentação são: **1. Tolerancia a Falhas, 2. Seguranca, 3. Sistemas 
Arquivos Distribuidos e 4. Consistência e Replicação**. Os seminários serão 
em **DUPLA**. Abaixo o calendário:

| Aluno      | Tema                        | Data   |
|------------|-----------------------------|--------|
| X      | Y         | 14/Out |
| X      | Y                   | 14/Out |
| X      | Y | 19/jun |
| X      | Y                   | 19/jun |
| X      | Y | 21/jun |
| X      | Y  | 21/jun |
| X      |    Y|26/jun |


## Aulas

- **Aula 13:** Algoritmos de Eleição
  - **Adicionar ao Projeto:** Rota `/info`
    Implemente no seu projeto a rota `[GET] /info`, ela deve retornar 
    as seguintes informações:
    - `[GET] /info`
      - Retorna `HTTP 200 Ok` contendo no corpo as informações do serviço.
      ```json
      {
        "server_name": "server",
        "server_endpoint": "http://xyz.com/", 
        "descrição": "Projeto de SD. Os seguintes serviços estão implementados, ... etc",
        "versao": "0.1", 
        "Status": "online",
        "tipo_de_eleicao_ativa": "ring"
      }
      ```           
    - `[PUT] /info`
      - O corpo da mensagem de requisição (`body`) deve conter os novos dados
        que irão substituir os dados de `/info`. A ideia é que possamos 
        atualizar os dados de `/info`, especialmente para modificar o valor da
        propriedade `status` de `online` para `offline` e vice-versa e para 
        modificar o tipo de eleição para a qual o serviço está configurado.
      - A resposta deve ser uma mensagem com o HTTP status de `200 OK` se a 
        mensagem foi processada com sucesso ou `400 Bad Request` no caso da
        requisição não conter os dados necessários.
    - `[GET] /peers`
      - Deve retornar a lista de servidores conhecidos (os servidores dos 
        seus colegas, utilize a tabela com as URLs deles no final deste 
        documento.). Nomes e IDs devem ser únicos. O formato da mensagem deve 
        ser a seguinte:
        ```json
        [
          {                      
            "id":  "id_server_1",
            "nome": "fulano",
            "url": "url_server_1"
          },                     
          {                      
            "id":  "id_server2",
            "nome": "sicrano",
            "url": "url_server2" 
          } 
        ]     
        ```
    - `[POST] /peers`
      - Um `POST` feito em `/peers` tem o intuito de adicionar um novo `peer` 
        à lista e o conteudo da mensagem deve ser os dados do novo `peer`, 
        como mostra o exemplo abaixo:
      ```json
      {                      
        "id":  "id_server2",
        "nome": "beltrano",
        "url": "url_server2" 
      } 
      ```
      A resposta de ser um `HTTP 200 OK` se a requisição foi processada com 
      sucesso, `HTTP 400 Bad Request` se a requisação está malformada 
      por exemplo, não contém os dados necessários ou estruturados fora do 
      padrão, por fim um `HTTP 409 Conflict` caso esteja tentando adicionar um
      peer com `nome` ou `id` existentes.
    - `[GET] /peers/{id}`
      Ao fazer um get na rota acima queremos obter as informações somente 
      do `peer` cujo id é `{id}`. a resposta deve ser no formato:
      ```json
      {                      
        "id":  "id_server2",
        "nome": "sicrano",
        "url": "url_server2" 
      } 
      ```
      Deve retornar `HTTP 200 OK` com as infromações do `peer` se ele existir,
      ou `HTTP 404 Not Found` se não existir um `peer` com o `{id}` indicado 
      na rota.
    
    - `[PUT] /peers/{id}`
      Uma mensagem do tipo `PUT` na rota acima modifica os dados do `peer` de
      cujo `id` é `{id}`. No corpo da mensagem deve se enviar os novos dados.
      por exemplo:
      ```json
      {                      
        "id":  "id_server2",
        "nome": "sicrano",
        "url": "NOVA_URL" 
      }
      Deve retornar `HTTP 200 OK` com as novas infromações do `peer` se ele 
      existia e foi atualizado ou `HTTP 404 Not Found` se não existir um 
      `peer` com o `{id}` indicado.
    - `[DELETE] /peer/{id}`
      Um delete na rota acima irá deletar o `peer` de id igual a `{id}` da 
      lista de peers do servidor. Deve retornar `HTTP 200 OK` se o `peer` foi
      corretamente deletado. `HTTP 404 Not Found` se não existir um `peer` 
      com o `{id}` indicado.
                       

- **Aula 12:** Sincronização em SD, Relógios e Exclusão Mútua
  - [Slides](https://www.icloud.com/iclouddrive/0U_JxD0LV-g9aWqrq4Crkivfg#SD-Aula14-Sincronizac%CC%A7a%CC%83o) 
  - [Gravação da Aula](https://drive.google.com/file/d/1v1qsbAK8cF2Tii-jEZtTvF1NPuLwNSFI/view?usp=sharing)

- **Aula 11:** Preparação para o Trabalho Final: Git, GitHub e Python/FastAPI
  - [Gravação da Aula](https://drive.google.com/file/d/1Uo0hniKEbyUmn8hhKuiI2A3XAOlkeU-L/view?usp=sharing)
  - [Código exemplo](https://github.com/profmathias/cet-100/tree/master/pratica-4)


- **Aula 10:** Nomeação em SD
  - [Slides](https://www.icloud.com/iclouddrive/0mPZnFuCoUkmo6s7N8tPXrx7w#Aula-8)
  - [Gravação da Aula](https://drive.google.com/file/d/17Wel0LNxR6HcShD9s2T3vYe5vHwBdajC/view?usp=sharing)
  - **Exercício**:
    - Crie uma rota `[POST] /resolver` no seu App que receba no corpo da 
    mensagem HTTP a seguinte informação em JSON:
    ```
    {
      "operacao": "resolver",
      "arguments: {
        "nome": "joao"
      }
    }
    ```
    Use o método POST do HTTP. Para isso no Python utilizando **FastAPI**
    utilize o método `app.post()` do objeto da aplicação FastAPI o mesmo 
    método existe no `Express.js`. **Qualquer dúvida entrem em contato pelo 
    DISCORD.** 


- **Aula 9:** Migração de Código
  - [Slides](https://www.icloud.com/iclouddrive/0Kp_ZQeSSwKdqHWISNyeMpv9Q#Aula7)
  - [Vídeo-Aula (Gravação de 2021.1)](https://drive.google.com/file/d/1zN6khvtNbBtX7jlQzBgTur9xum8Bd9Ff/view) 
  - Exercício: Este exercício visa antecipar o próximo assunto.
    Modifique o código do exercício anterior para que o cliente
    possa encontrar os servidores sem que necessitem de antemão
    o IP, considere implementar um novo componente que resolva os
    nomes para o IP do servidor. O IP deste novo serviço pode
    ser conhecido pelos clientes.
    

- **Aula 8:** Virtualização com Containers Docker
  - [Código Exemplo](https://github.com/profmathias/cet-100/tree/master/pratica-3)
  - [Vídeo-Aula (Gravação de 2021.1)](https://drive.google.com/file/d/1eYhYE3qao3KKxwKql91NNJ5ozYrSJTXX/view?usp=sharing)
  

- **Aula 7: Threads, Processos e Virtualização em SD**
  - [Gravação da Aula](https://drive.google.com/file/d/16h-1mi4GjwfO2S3ZGNoXL0zDweUsgaqq/view?usp=sharing)

- **Aula 6**: Arquiteturas de Sistemas e Threads e Processos na Prática
    - [Slides](https://www.icloud.com/iclouddrive/0KftRdrgVqFwnrpVBpe1Ln_pQ#Aula-6-Arquiteturas_de_Sistemas)
    - [Gravavação da Aula](https://drive.google.com/file/d/105o6UlBLIWCQOBKppufNjCIrFQpLSQxc/view?usp=sharing)
    - [Código feito em Sala](https://github.com/profmathias/cet-100/tree/master/pratica-2)  
    - **Leitura do Livro** Capítulo 3: Processos, Sistemas Distribuídos e 
    Princípios, Tanenbaum e Van Steen.
    - **Exercício:** Releia o código visto em sala de aula tente executá-lo
      na sua máquina. Verifique o tempo total de execução das 
      diferentes versões do programa utilizando o comando `time` (no linux) 
      ou o `Measure-Command` no PowerShell/Windows. 
      - No Linux (Terminal): 
        ```
        time python3 -m multi_process.py
        ```
      - No Windows/PowerShell (Pessoal não testei pois não tenho Windows, 
        mandem feedback informando se funcionou) 
        ```
        Measure-Command {start-process python3 -m multi_process.py -Wait}
        ```
      Depois disso, analise os resultados das diferentes versões e explique
      o porque dos resultados. Lembrem-se que Python não é uma linguagem
      100% Multithreaded.


- **Aula 5**: Continuação da Aula 4 e Estilos Arquitetônicos
  - [Slides](https://www.icloud.com/iclouddrive/0h-Im45H2Xpy4flst2dFgYTsg#Aula05-Continuacao-Aula4-e-Estilos-arqutetonicos)
  - [Gravação da Aula](https://drive.google.com/file/d/1YC4dScm_w6gXqpznU1Iu2kEKbQ4Ku5dK/view?usp=sharing)
  - **Leitura do Livro** Capítulo 2: Arquiteturas, Sistemas Distribuídos e 
    Princípios, Tanenbaum e Van Steen.
- **Aula 4**: Escalabilidade e Tipos de SD 
  - [Slides](https://www.icloud.com/iclouddrive/02tirBqG4gfcLPUjT_XueedtA#Aula03-Escalabilidade_e_Tipos_de_SD)
  - [Gravação da Aula](https://drive.google.com/file/d/1hMZv__sz1N5LVzVHV99hJJdYRv_PTq0q/view?usp=sharing)
  - **Exercício**: Dado a um bug no programa disponibilizado, o exercício da
    aula anterior foi estendida para a próxima aula. NOTEM QUE o passo a passo
    de como colocar o app no Heroku foi visto na Aula 3, portanto caso tenham
    dúvidas revejam a aula. Copiem para o seu computador somente o diretório
    do exemplo, não todo o repositório da disciplina.
  - **Leitura do Livro:** Capítulo 1: Introdução, Sistemas Distribuídos e 
    Princípios, Tanenbaum e Van Steen.
    

- **Aula 3**: Prática 1: Um serviço HTTP Simples e Implantação no Heroku
  - [Heroku](https://heroku.com)
  - [Python FastAPI](https://fastapi.tiangolo.com)
  - [Gravação da Aula](https://drive.google.com/file/d/1dXJEw2LVmueY31LOeuZS31EVVgpRHWT1/view?usp=sharing)
  - [Código de Partida para o Exercício](https://github.com/profmathias/cet-100/tree/master/pratica-1)
  - **Exercício:** A partir do **Código de Partida** modifique-o para adicionar
  novas rotas e faça a implantação no Heroku.
    
- **Aula 2**: Transparência em Sistemas Distribuídos
  - [Slides](https://www.icloud.com/iclouddrive/0scd3zma0M3KP6y_Y3WS2aJmg#Aula-2-Intro_SD-Tranparencia)
  - [Gravação da Aula](https://drive.google.com/file/d/1GcNC53NafeWxSBqhtZ_iEA2JBdzZIYep/view?usp=sharing)
  
  
- **Aula 1**: Apresentação da Disciplina e Introdução a SD**
  - [Slides](https://www.icloud.com/iclouddrive/0z8lgr8LK7aqR8vVlMRaT7MBA#SD)
  - [Gravação da Aula](https://drive.google.com/file/d/1GBB4mwTTX8RSvZorMtj2R-8COH4uwm0j/view?usp=sharing)

#### Sobre as  Videoaulas

**Atenção:** As videoaulas só são acessíveis com o uso do e-mail institucional (`@uesc.br`).

 

## Heroku Apps URLs

|           |                                      | Heroku App URL                                    |
|-----------|--------------------------------------|---------------------------------------------------|
| 201720295 | Allana Dos Santos Campos             | https://sd-ascampos-20212.herokuapp.com/          |
| 201512136 | Annya Rita De Souza Ourives          | https://sd-annyaourives-20212.herokuapp.com/hello |
| 201512137 | Daniel Andrade Penêdo Santos         |                                                   |
| 201710375 | Emmanuel Norberto Ribeiro Dos Santos | https://sd-emmanuel.herokuapp.com/                |
| 201420373 | Gabriel Figueiredo Góes              |                                                   |
| 201710376 | Guilherme Senna Cruz                 | https://nodejs-sd-guilhermesenna.herokuapp.com/   |
| 201710377 | Hiago Rios Cordeiro                  | https://sd-api-uesc.herokuapp.com/                |
| 201810665 | Jenilson Ramos Santos                | https://jenilsonramos-sd-20211.herokuapp.com/     |
| 201610327 | João Pedro De Gois Pinto             | https://sd-joaopedrop-20212.herokuapp.com/        |
| 201610337 | Luís Carlos Santos Câmara            | https://sd-20212-luiscarlos.herokuapp.com/        |
| 201620181 | Matheus Santos Rodrigues             |                                                   |
| 201620400 | Nassim Maron Rihan                   | https://sd-nassimrihan-2021-2.herokuapp.com/      |
| 201710396 | Robert Morais Santos Broketa         |                                                   |
| 201720308 | Victor Dos Santos Santana            | https://sd-victor-20212.herokuapp.com/            |


## Frameworks para Desenvolvimento de APIs HTTP

### Python

- [FastAPI](https://duckduckgo.com/?q=python+fastapi&t=osx): Framework HTTP 
  que utiliza async/await do python. O seu uso lembra um pouco o Express.js 
- [Flask:](https://flask.palletsprojects.com/en/1.1.x/) Framework HTTP para criação de API com suporte a templates HTML
- [Connexion:](https://pypi.org/project/connexion/) Framework para desenvolvimento de APIs HTTP utilizando o conceito de API First Design ou API-Driven Development.


### Javascript

- [Express.js](http://expressjs.com)

### Java
- [Spring Boot](https://spring.io/projects/spring-boot): Framework da familia *Spring* para a criação de APIs baseadas HTTP. Muito estável e com um alto nível de maturidade.

### Docker

- [Página Oficial (Inglês)](https://www.docker.com)
- [Tutorial hands-on oficial Play With Docker. Muito bom para praticar. (Inglês)](https://www.docker.com/play-with-docker)
- Tutorial em Português - Introdução ao Docker - por Cássio Ferraz
  * [Parte I](https://medium.com/@ferrazcassim/introdução-ao-docker-parte-i-7c6ecad3b4fd)
  * [Parte II](https://medium.com/@ferrazcassim/introdução-ao-docker-parte-ii-b44666837d37)
  * [Parte III](https://medium.com/@ferrazcassim/introdução-ao-docker-parte-iii-a675dfbea11e)
