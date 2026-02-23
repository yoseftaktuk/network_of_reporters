#pip install kafka-python
from asyncio import log
from kafka import KafkaProducer
import json
import os
kafka_uri = os.getenv('KAFKA_URI')

class KafkaService:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=kafka_uri,
        value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')) 
          
    def on_send_success(self, record_metadata):
        print(record_metadata.topic)
        print(record_metadata.partition)
        print(record_metadata.offset)

    def on_sent_error(self, excp):
        log.error('I am an errback', exc_info=excp)    
    
    def send_to_kafka(self, data: dict):
        self.producer.send(topic='raw', value=data).add_callback(self.on_send_success).add_errback(self.on_send_error)
        print('send to kafka')