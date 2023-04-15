import feedparser
import json
from data import Data
from bot import Bot
from database import DataBase

class Crawler:
    def __init__(self, url, file_name):
        self.url = url
        self.file_name = file_name + ".json"
        self.name = file_name

    def RSS(self):
        self.feed = feedparser.parse(self.url)
        return self.feed

    def load_existing_data(self):
        try:
            with open(self.file_name, "r") as f:
                existing_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []
        return existing_data

    def output(self, crawl_data):
        exist_data = self.load_existing_data()
        new_data = []
        for crawl_item in crawl_data:
            if not any(
                item.get("link") == crawl_item.get("link") for item in exist_data
            ):
                new_data.append(crawl_item)
                message = f"New article: {crawl_item['Title']}\n{crawl_item['Description']}\n{crawl_item['Link']}"
                self.bot.send_message(message)
        with open(self.file_name, "w") as outfile:
            json.dump(new_data + exist_data, outfile, indent=4)

    def crawl_and_format(self):
        self.RSS()
        articles = Data.parse(self.feed)
        json_format = Data.format(articles)
        return json_format
