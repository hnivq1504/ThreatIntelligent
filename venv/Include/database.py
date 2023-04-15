import elasticsearch
import json
from data import Data

class DataBase:
    def __init__(self, host, name_index):
        self.es = elasticsearch.Elasticsearch(hosts=[host])
        self.index = name_index
        self.file_name = name_index + ".json"


    def add_to_database(self):
        with open(self.file_name, "r") as f:
            data = json.load(f)
        if not self.es.indices.exists(index=self.index):
            self.es.indices.create(index=self.index)
        for article in data:
            self.es.index(index=self.index, document=article)

