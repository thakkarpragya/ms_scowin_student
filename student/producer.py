import json
from unittest.mock import DEFAULT
import pika
# import os

def publish(method, body):
    # amqp_url = os.environ['AMQP_URL']
    amqp_url = 'amqp://rabbit_mq?connection_attempts=10&retry_delay=10'
    url_params = pika.URLParameters(amqp_url)
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()
    channel.queue_declare(queue='vacdrive', durable=True)
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='vacdrive', body=json.dumps(body), properties=pika.BasicProperties(delivery_mode=2))
    print("Produced the message")
    channel.close()
    connection.close()