from kafka import KafkaConsumer
import json
import time
import os
from prudocer import KafkaService
from utils import ElasticService

elastic = ElasticService()
kafka = KafkaService()
elastic.create_index()
kafka_uri = os.getenv('KAFKA_URI')
    
def get_from_kafka(topic: str):
    
        try:
            consumer = KafkaConsumer(
                topic,
                bootstrap_servers=kafka_uri,
                auto_offset_reset='earliest',
                enable_auto_commit=False,
                max_poll_interval_ms=300000,
                value_deserializer=lambda x: json.loads(x.decode('utf-8'))
            )
            print("Connected to Kafka")
            return
        except Exception:
            print("Waiting for Kafka...")
            time.sleep(2)
        for message in consumer:
            print(f"Received message value: {message.value}")
            elastic.upsert(message.value)
            consumer.commit()