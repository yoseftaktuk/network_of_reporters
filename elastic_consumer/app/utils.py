from elasticsearch import Elasticsearch
import os
{'image_byts' : bytes,
               'meta_data': dict,
               'image_id': str,
               'words': str,
               'clean_word': str}

class ElasticService:
    def mapping(self):
        map = {
            'mappings':{
                'properties':{}}}
        
    def create_index(self, mapping):
        es = Elasticsearch(os.getenv('ELASTIC_URI',"localhost:9200"))  
        response = es.indices.create(index='agents', body=mapping)

    def upsert(self):
        es = Elasticsearch(os.getenv('ELASTIC_URI',"localhost:9200"))
        es.update(
        index="images",
        doc_type="test1",
        id="1",
        body={
            "doc": {"username": "Tom"}, 
            "doc_as_upsert": True
        }
        )