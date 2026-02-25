import streamlit as st
import pandas as pd
from elasticsearch import Elasticsearch
import os

data = {'weapons': ['Sword', 'Bow', 'Axe'], 'data': [1, 3, 2]}
df = pd.DataFrame(data)

st.bar_chart(df.set_index('weapons'))
es = Elasticsearch(os.getenv('ELASTIC_URI',"http://elasticsearch:9200"))
class ElastikQueryService:
    def get_wepons(self):
        query = {
  "size": 0,
  "aggs": {
    "list_of_items": {
      "terms": {
        "field": "weapons.keyword",
        "size": 100 
      }
    }
  }
}