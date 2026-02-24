from kafka import KafkaConsumer
import json
import time
import os
from prudocer import KafkaService
kafka = KafkaService()

kafka_uri = os.getenv('KAFKA_URI')
    
def get_from_kafka(topic: str, key: str, func):
    while True:
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
            break
        except Exception:
            print("Waiting for Kafka...")
            time.sleep(2)
    for message in consumer:
            print(f"Received message value: {message.value}")
            data = func(message.value[key])
            kafka.send_to_kafka('clean',data)
            consumer.commit()