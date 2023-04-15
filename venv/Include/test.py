from crawler import Crawler
from data import Data
from database import DataBase
import elasticsearch
import json

def JsonFormat(articles):
    jsonformat=[]
    for article in articles:
        jsonformat.append(article.__json__())
    return jsonformat

def send_to_elasticsearch():
    with open("beepingcomputer.json", "r") as f:
        data = json.load(f)
    if not es.indices.exists(index="beepingcomputer"):
        es.indices.create(index="beepingcomputer")

    for article in data:
        es.index(index="beepingcomputer", document=article)

if __name__ == '__main__':
    url = "https://feeds.feedburner.com/TheHackersNews"
    es_host = "http://192.168.6.151:9200/"
    es = elasticsearch.Elasticsearch(es_host)
    with open("beepingcomputer.json", "r") as f:
        data = json.load(f)
    # if not es.indices.exists(index="beepingcomputer"):
    #     es.indices.create(index="beepingcomputer")
    print(data[1])
    for article in data:
        es.index(index="beepingcomputer", body=article)
