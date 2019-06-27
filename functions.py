import json
import time

def create_file(body=None):
    if body is not None:
        with open(str('informations'), 'a+') as f:
            f.write(body.decode())
        print('Creatin File Done')
        return 'File was create'


def send_email(body):
    pass
