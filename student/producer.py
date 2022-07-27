import json
from unittest.mock import DEFAULT
import pika
# import os

def publish(method, body,queue):
#     amqp_url = 'amqp://rabbit-mq?connection_attempts=10&retry_delay=10'
    amqp_url = 'amqp://guest:guest@rabbit-mq:5672?connection_attempts=10&retry_delay=10'
    url_params = pika.URLParameters(amqp_url)
    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()
    # amqp_url = os.environ['AMQP_URL']

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
    # channel.queue_declare(queue='vacdrive')
    channel.queue_declare(queue=queue)
    # properties = pika.BasicProperties(content_type=method)
    channel.basic_publish(exchange='', routing_key=queue, body=json.dumps(body), properties=pika.BasicProperties(content_type=method,delivery_mode=2))
    print("Produced the message")
    channel.close()
    connection.close()
