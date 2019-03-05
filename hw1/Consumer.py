import pika
import time

time.sleep(10)
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='172.18.0.2'))
channel = connection.channel()

channel.queue_declare(queue='random_numbers')

print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received " + body.decode())

channel.basic_consume(callback,
                      queue='random_numbers',
                      no_ack=True)

channel.start_consuming()
