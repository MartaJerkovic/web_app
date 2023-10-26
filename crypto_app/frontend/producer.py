import pika
from pika.exchange_type import ExchangeType

class RabbitMQProducer:
    def __init__(self, host='localhost'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='direct_exchange', exchange_type=ExchangeType.direct)

    def publish_message(self, routing_key, message):
        self.channel.basic_publish(exchange='direct_exchange',
                                   routing_key=routing_key,
                                   body=message)
        print(f"Sent message with routing key '{routing_key}': {message}")

    def close_connection(self):
        self.connection.close()

