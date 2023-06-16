from __future__ import absolute_import, unicode_literals
from celery import shared_task
import pika
import time

@shared_task
def producer(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='teste')    
    time.sleep(5)
    channel.basic_publish(exchange='', routing_key='teste', body=message)
    connection.close()
    return message

def callback(ch, method, properties, body):
        
        print("Mensagem recebida:", body)  
        user = Users.objects.create(username="alllllll")
        user.save()
        ch.basic_ack(delivery_tag=method.delivery_tag)
        

#channel.basic_consume(queue='teste', on_message_callback=callback, auto_ack=True)
#channel.start_consuming()