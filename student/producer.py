import json
import pika

# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
connection = pika.BlockingConnection(pika.ConnectionParameters('flamboyant_neumann:15672'))
channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='vacdrive', body=json.dumps(body), properties=properties)

