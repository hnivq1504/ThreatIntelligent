import json

class Data:
    def __init__(sefl,title,published,description,link):
        sefl.title = title
        sefl.published = published
        sefl.description = description
        sefl.link = link

    def __json__(self):
        return {"Title": self.title, "Published": self.published,
                "Description": self.description,"Link": self.link}

    def parser(feed):
        articles = []
        for item in feed["items"]:
            article = Data(item["title"],item["published"],item["description"],item["link"])
            articles.append(article)
        return articles