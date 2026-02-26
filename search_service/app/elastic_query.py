import streamlit as st
import pandas as pd
from elasticsearch import Elasticsearch
import os
from streamlit_autorefresh import st_autorefresh

es = Elasticsearch(os.getenv('ELASTIC_URI', "http://localhost:9200"))
class ElastikQueryService:
    def get_wepons(self):
        query = {
  "size": 0,
  "aggs": {
    "list_of_items": {
      "terms": {
        "field": "weapons",
        "size": 100
      }
    }
  }
}
        return es.search(index='image', body=query)
    
    def streamlit_get_wepons(self, result: dict):    
          wepons_list = []
          count = []
          for item in result['aggregations']['list_of_items']['buckets']:
              wepons_list.append(item['key'])
              count.append(item['doc_count'])
          data = {'weapons':wepons_list, 'data':count}
          df = pd.DataFrame(data)
          st.bar_chart(df.set_index('weapons'))

    def get_most_common_words(self):
        query = {
  "size": 0,
  "aggs": {
    "list_of_items": {
      "terms": {
        "field": "10_commend_words",
        "size": 100
      }
    }
  }
}
        return es.search(index='image', body=query)
    
    def streamlit_get_common_words(self, result: dict):
        words_list = []
        count = []
        for item in result['aggregations']['list_of_items']['buckets']:
              words_list.append(item['key'])
              count.append(item['doc_count'])
        data = {'words': words_list, 'data':count}
        df = pd.DataFrame(data)
        st.bar_chart(df.set_index('words'))