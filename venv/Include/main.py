from crawler import Crawler
from data import Data
from database import DataBase
from bot import Bot
import sys
import elasticsearch
import json

if __name__ == '__main__':
    es_host = "http://192.168.6.151:9200/"
    
    Crawl_HackerNews = Crawler("https://feeds.feedburner.com/TheHackersNews","hackernews")
    Data_HackerNewsCrawl = Crawl_HackerNews.crawl_and_format()
    Bot_HackerNews = Bot("6216004222:AAHo7A_DoK5e6sCdfBHp2VpwOn_H-Hg9Og8","-901299271")
    Crawl_HackerNews.bot = Bot_HackerNews
    DB_Hackernews = DataBase("http://192.168.6.151:9200/","hackernews")
    Crawl_HackerNews.output(Data_HackerNewsCrawl)
    DB_Hackernews.add_to_database()


    Crawl_BeepingComputer = Crawler("https://www.bleepingcomputer.com/feed/","beepingcomputer")
    Data_BeepingComputer = Crawl_BeepingComputer.crawl_and_format()
    Bot_BeepingComputer = Bot("6031688399:AAHkRbu_UUOFdJSRVJlvxcmmHqATH3q-wYI","-858491908")
    Crawl_BeepingComputer.bot = Bot_BeepingComputer
    DB_BeepingComputer = DataBase("http://192.168.6.151:9200/","beepingcomputer")
    Crawl_BeepingComputer.output(Data_BeepingComputer)
    DB_BeepingComputer.add_to_database()
    # db = DataBase(es_host, index_name)