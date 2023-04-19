import elasticsearch
import json
from data import Data


class DataBase:
    def __init__(self, host, name_index):
        self.es = elasticsearch.Elasticsearch(hosts=[host])
        self.index = name_index
        self.file_name = name_index + ".json"

    # def add_to_database(self):
    #     with open(self.file_name, "r") as f:
    #         data = json.load(f)
    #     if not self.es.indices.exists(index=self.index):
    #         self.es.indices.create(index=self.index)
    #     for article in data:
    #         self.es.index(index=self.index, document=article)

    # def add_to_database(self):
    #     with open(self.file_name, "r") as f:
    #         data = json.load(f)
    #     if not self.es.indices.exists(index=self.index):
    #         self.es.indices.create(index=self.index)
    #     for article in data:
    #         doc_id = article['Link']  # set unique ID for document
    #         self.es.index(index=self.index, id=doc_id, body=article, op_type='create')

    def add_to_database(self):
        # Read the data from the JSON file
        with open(self.file_name, "r") as f:
            data = json.load(f)
        
        # Check if the Elasticsearch index exists, and create it if it doesn't
        if not self.es.indices.exists(index=self.index):
            self.es.indices.create(index=self.index)

        # Get the IDs of the documents already in the index
        existing_ids = [doc['_id'] for doc in self.es.search(index=self.index, body={"query": {"match_all": {}}})['hits']['hits']]
        
        # Add any new documents to the index
        for article in data:
            doc_id = article['Link']
            if doc_id not in existing_ids:
                self.es.index(index=self.index, id=doc_id, body=article)


