FROM python:3.8

EXPOSE 5000

COPY . /app
WORKDIR /app
RUN pip install -e .

ENTRYPOINT 'meu_app'
