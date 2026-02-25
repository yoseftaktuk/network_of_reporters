from PIL import Image, UnidentifiedImageError
import logging
import os
import requests
from producer import KafkaService
import uuid  
from PIL import Image
import pytesseract



class ImageService:
    def read_from_image(self,img: str):
        try:
            img = Image.open(img)
            result = pytesseract.image_to_string(img)
            return result
        except TypeError as e:
            logging.warning(str(e))
        return result
    
    def get_matedata(self, path: str):
        try:
            img = Image.open(path)
        except UnidentifiedImageError as e:
            logging.warning(e)
            return str(e)    
        return{'size': img.size,
               'format': img.format,
               'weight': f'{os.path.getsize(path)} kb'}
    
    def get_image_byts(self, path):
        try: 
            with open(path, "rb") as f:
                return f.read()
        except UnidentifiedImageError as e:
            logging.warning(e)
            return str(e) 
        img.close()
        return img.tobytes()
    
    def to_kafka(self, path: str):
       return {
               'meta_data': self.get_matedata(path),
               'image_id': str(uuid.uuid4()),
               'words': self.read_from_image(path)}


kafka = KafkaService()  
class SendServie:
    def send_to_mongodb_loader(self, data: bytes):
        url = os.getenv('MONGODB_LOADER_URL', 'http://mongodb_loader_service:8080/post_to_mongodb')
        try: 
            requests.post(url=url, data=data)
        except requests.exceptions.RequestException as e:
            logging.warning(f"An error occurred: {e}")   
    def send_to_kafka(self, data: dict):
        kafka.send_to_kafka('raw', data=data)
