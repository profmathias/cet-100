import pika
import time


def main():

    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost', 5672, '/',
                                  pika.PlainCredentials('usuario', 'senha')))
    channel = connection.channel()

    try:
        while True:
            time.sleep(5)
            print('Enviando um post...')
            channel.basic_publish(exchange='blog', routing_key='post',
                                  body='Novo Post Publicado...')
    except KeyboardInterrupt:
        connection.close()


if __name__ == '__main__':
    main()
