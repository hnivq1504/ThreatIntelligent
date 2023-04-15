import json

class Data:
    def __init__(self, item):
        self.title = item.get("title", "")
        self.published = item.get("published", "")
        self.description = item.get("description", "")
        self.link = item.get("link", "")

    def __json__(self):
        return {
            "Title": self.title,
            "Published": self.published,
            "Description": self.description,
            "Link": self.link,
        }

    @staticmethod
    def parse(feed):
        articles = []
        for item in feed["items"]:
            article = Data(item)
            articles.append(article)
        return articles

    @staticmethod
    def format(articles):
        return [article.__json__() for article in articles]