from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
import gridfs



host = os.getenv('HOST', 'mongo')
port = os.getenv('PORT', 27017)
user = os.getenv('USER', 'my_db')
password = os.getenv('PASSWORD', 'my_password')
uri = f"mongodb://{user}:{password}@{host}:{port}"
print(uri)

class MongoDbService:
    def __init__(self):
        self.client = None
        self.db = None
        self.colletion = None
    def conect(self):
        try:
            self.client = MongoClient(uri)
            self.client.admin.command('ping')   
            print('connection') 
        except ConnectionFailure as e:
            raise str(e)
        
    def creat_collection(self):
        self.db = self.client['my_db']
        self.colletion = self.db['my_collection']
        self.fs = gridfs.GridFS(self.db)
        return self.colletion  

    def insert_one_preparing(self, item):
        self.fs.put(item)
            
