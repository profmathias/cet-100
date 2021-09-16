# Bem-Vindo ao Repositório da Disciplina CET-100 Sistemas Distribuídos


## Metodologia e Planejamento

[Plano de Ensino](https://github.com/profmathias/cet-100/blob/master/CET100%20-%20Plano%20de%20Ensino.doc?raw=true)


## Aulas
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
  - [Código Exemplo](https://github.com/profmathias/cet-100/tree/2021.1/Codigo/exemplo_docker)
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
