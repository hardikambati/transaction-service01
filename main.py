import json

from programs.process import (
    core_process,
)

from utils import (
    config,
    broker,
)


queue_name = 'service-01'

# listen to queue continuously
consumer = broker.Consumer(config.BROKER_URL)
consumer.declare_queue(queue_name=queue_name)
method_frame, _, body = consumer.basic_get(queue_name=queue_name)


def callback(ch, method, properties, body):
    print('Received message\n')
    print(f'{body}')
    body = json.loads(body)
    
    result = core_process(body)

    consumer.ack(method)


print('[service-01] started consuming...')

consumer.recieve_messages(queue_name, callback)

consumer.start_consuming()