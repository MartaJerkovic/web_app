import pika
from pika.exchange_type import ExchangeType

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='direct_exchange', exchange_type=ExchangeType.direct)

channel.queue_declare(queue='signup_queue')
channel.queue_declare(queue='login_queue')

channel.queue_bind(exchange='direct_exchange', queue='signup_queue', routing_key='signup')
channel.queue_bind(exchange='direct_exchange', queue='login_queue', routing_key='login')

def callback(ch, method, properties, body):
    print(f"Received message: {body}")

channel.basic_consume(queue='signup_queue', on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue='login_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()