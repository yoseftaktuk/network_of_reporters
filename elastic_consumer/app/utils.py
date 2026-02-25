from elasticsearch import Elasticsearch
import os


class ElasticService:
    def mapping(self):
        map = {
            'mappings':{
                'properties':{
                    'meta_data':        {'type': 'object'},
                    'image_id' :        {'type': 'keyword'},
                    'words':            {'type': 'text'},
                    'clean_word':       {'type': 'text'},
                    '10_commend_words': {'type': 'object'},
                    'weapons':          {'type': 'object'},
                    'sentiment_clean_words': {'type': 'keyword'},
                    'sentiment':        {'type': 'keyword'} 
                    }
                }
            }
        return map         
        
    def create_index(self):
        es = Elasticsearch(os.getenv('ELASTIC_URI',"http://elasticsearch:9200"))  
        if not es.indices.exists(index='image'):
            response = es.indices.create(index='image', body=self.mapping())
            print(response)
            return
        return

    def upsert(self, data: dict):
        es = Elasticsearch(os.getenv('ELASTIC_URI',"http://elasticsearch:9200"))
        doc_id = data['image_id']
        index_name = "image"
        document_body = data
        response = es.index(
        index=index_name,
        id=doc_id,
        body=document_body
    )
        return response