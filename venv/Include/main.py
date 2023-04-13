# from crawler import Crawler
# from data import Data
# from database import DataBase
# import elasticsearch
# import json

# def JsonFormat(articles):
#     jsonformat=[]
#     for article in articles:
#         jsonformat.append(article.__json__())
#     return jsonformat

# def OutPut(file_name,crawl_datas):
#     exist_data = Load_Exist(file_name)
#     for crawl_data in crawl_datas:
#         if crawl_data not in exist_data:
#             with open(file_name, "a") as outfile:
#                 json.dump(crawl_data,outfile,indent=6)


# def Load_Exist(file_name):
#     try:
#         with open(file_name, "r") as infile:
#             exist_data = json.load(infile)
#     except FileNotFoundError:
#         exist_data = []
#     return exist_data

# if __name__ == '__main__':
#     url = "https://feeds.feedburner.com/TheHackersNews"
#     bot_token = "6216004222:AAHo7A_DoK5e6sCdfBHp2VpwOn_H-Hg9Og8"
#     chat_id = "-901299271"
#     es_host = "http://192.168.6.151:9200/"
#     index_name = "hackernews"
#     HackerNewCrawl = Crawler(url)
#     feed = HackerNewCrawl.RSS()
#     articles = Data.parser(feed)
#     db = DataBase(es_host,index_name)
#     crawl_datas = JsonFormat(articles=articles)
#     OutPut("hackernews.json",crawl_datas)
#     # es = elasticsearch.Elasticsearch(hosts=[es_host])
#     # if not es.indices.exists(index="hackernews"):
#     #     es.indices.create(index="hackernews")
#     # for crawl_data in crawl_datas:
#     #     es.index(index="hackernews", document=crawl_data)
#     # print(DataBase.Load_Exist("hackernews.json"))

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

def Load_Exist(file_name):
    try:
        with open(file_name, "r") as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []
    return existing_data

def OutPut(file_name, crawl_datas):
    exist_data = Load_Exist(file_name)
    new_data = []
    for crawl_data in crawl_datas:
        if crawl_data not in exist_data:
            new_data.append(crawl_data)
    with open(file_name, "w") as outfile:
        json.dump(new_data+exist_data, outfile, indent=6)
        outfile.write('\n')

if __name__ == '__main__':
    url = "https://feeds.feedburner.com/TheHackersNews"
    bot_token = "6216004222:AAHo7A_DoK5e6sCdfBHp2VpwOn_H-Hg9Og8"
    chat_id = "-901299271"
    es_host = "http://192.168.6.151:9200/"
    index_name = "hackernews"
    HackerNewCrawl = Crawler(url)
    feed = HackerNewCrawl.RSS()
    articles = Data.parser(feed)
    db = DataBase(es_host, index_name)
    crawl_datas = JsonFormat(articles=articles)
    # exist_data = Load_Exist("hackernews.json")
    OutPut("hackernews.json", crawl_datas)
    # es = elasticsearch.Elasticsearch(hosts=[es_host])
    # if not es.indices.exists(index="hackernews"):
    #     es.indices.create(index="hackernews")
    # for crawl_data in new_crawl_data:
    #     es.index(index="hackernews", document=crawl_data)
    # print(DataBase.Load_Exist("hackernews.json"))