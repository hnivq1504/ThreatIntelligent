import elasticsearch
import json
from data import Data

class DataBase:
    def __init__(self,host,name_index):
        self.es = elasticsearch.Elasticsearch(hosts=[host])
        self.index = name_index

    def add(self,article):
        if not self.es.indices.exists(index=self.index):
            self.es.indices.create(index=self.index)

        existing_data = []

        try:
            results = self.es.search(index=self.index, body={"query": {"match_all": {}}})
            for hit in results["hits"]["hits"]:
                existing_data.append(hit["_source"])
        except elasticsearch.exceptions.NotFoundError:
            pass

        if article not in existing_data:
            return article

    # def add(self,articles):
    #     for article in self.check_exist(articles):
    #         self.es.index(index=self.index, document=article)

    def Load_Exist(file_name):
        try:
            with open(file_name, "r") as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = []
        return existing_data