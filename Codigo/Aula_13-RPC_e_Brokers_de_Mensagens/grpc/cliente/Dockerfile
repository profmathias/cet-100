# Imagem base para a criação da sua imagem personalizada
# A imagem python é uma imagem os aplciativos essencias para que
# se possa utilizar o python e instalar pacotes.
FROM python:3.8

# Copia o conteúdo deste diretório para o diretório /app dentro do container.
COPY . /app

# Define o diretório /app do container como o diretório principal de trabalho.
WORKDIR /app

# Executa o seguinte comando no container durante a sua criação.
# O comando abaixo instala a aplicação contida neste diretório, no caso o
# seu programa dentro do container utilizando o gerenciador de pacotes do
# Python, o pip
RUN pip install .

# Define o comando que será executado assim que o container iniciar após ter
# sido configurado e preparado pelos comandos anteriores.
ENTRYPOINT 'grpc_client'
