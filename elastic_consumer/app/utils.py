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
        es = Elasticsearch(os.getenv('ELASTIC_URI',"localhost:9200"))  
        response = es.indices.create(index='image', body=self.mapping())
        print(response)

    def upsert(self, data: dict):
        es = Elasticsearch(os.getenv('ELASTIC_URI',"localhost:9200"))
        doc_id = data['image_id']
        index_name = "my_index"
        document_body = data
        response = es.index(
        index=index_name,
        id=doc_id,
        body=document_body,
        doc_as_upsert=True
    )
        return response