import os

class IngestionConfig:
    KAFKA_URI = os.getenv('KAFKA_URI', 'localhost:9092')
    PATH = os.getenv('PATH', 'data')
    MONGODB_LOADER_URL = os.getenv('MONGODB_LOADER_URL', 'http://mongo:8080/post_to_mongodb')