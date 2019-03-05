import pika
import time
import random

time.sleep(10)
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '172.18.0.2'))
channel = connection.channel()

channel.queue_declare(queue='random_numbers')
while True:
    time.sleep(random.randint(0, 30))
    msg = str(random.randint(0, 2000000000))
    channel.basic_publish(exchange='',
                        routing_key='random_numbers',
                        body=msg)
    print (" [x] Sent " + msg)

connection.close()
