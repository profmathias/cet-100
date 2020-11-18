import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost', 5672, '/',
                              pika.PlainCredentials('usuario', 'senha')))
channel = connection.channel()


def callback(ch, method, properties, body):
    print(f'{body}')


def ouvir_mensagens():
    channel.basic_consume(queue="posts", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    ouvir_mensagens()
