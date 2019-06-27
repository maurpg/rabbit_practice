import pika as pk
import sys
from functions import *


class Receptor_info():

    def __init__(self , exchange , exchange_type  ):
        self.conection = pk.BlockingConnection(pk.ConnectionParameters('localhost'))
        self.channel = self.conection.channel()
        self.exchange_type = exchange_type
        self.result_queue = self.channel.queue_declare(queue='' , exclusive=True)
        self.queue_name = self.result_queue.method.queue
        self.exchange  = exchange


    def conection_queen(self):
        keys = sys.argv[1:]
        self.channel.exchange_declare(exchange= self.exchange, exchange_type=self.exchange_type)
        for key in keys:
            self.channel.queue_bind(exchange= self.exchange , queue = self.queue_name , routing_key=key)


    def callback_info(self ,ch = None , method = None , properties = None , body = None ):
        self.channel.basic_consume (queue = self.queue_name , on_message_callback=self.callback_info , auto_ack=True)
        if body is not None:
            print('[X] receive {}'.format(body.decode()))
            create_file(body)
  

    def start(self, *args, **kwargs):
        self.channel.start_consuming()


R1 = Receptor_info('direct_logs' , 'direct')
R1.conection_queen()
R1.callback_info()
R1.start()
