import pika as pk
import sys
import json

class EmitLog():

    def __init__(self):
        self.conection = pk.BlockingConnection(pk.ConnectionParameters('localhost'))
        self.channel = self.conection.channel()
        self.channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    def data(self):
        header = sys.argv[1]
        message = sys.argv[2:]
        message_create = json.dumps({header:message})
        self.channel.basic_publish(exchange='direct_logs', routing_key = header , body = message_create)
        print('[X] sent')
        self.conection.close()

E1 = EmitLog()
E1.data()