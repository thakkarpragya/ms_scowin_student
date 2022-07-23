import json
from unittest.mock import DEFAULT
import pika
# import os

def publish(method, body):
    amqp_url = 'amqp://rabbit-mq?connection_attempts=10&retry_delay=10'
    url_params = pika.URLParameters(amqp_url)
    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()
    # amqp_url = os.environ['AMQP_URL']

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
    channel.queue_declare(queue='vacdrive')
    # properties = pika.BasicProperties(content_type=method)
    channel.basic_publish(exchange='', routing_key='vacdrive', body=json.dumps(body), properties=pika.BasicProperties(content_type=method,delivery_mode=2))
    print("Produced the message")
    channel.close()
    connection.close()
