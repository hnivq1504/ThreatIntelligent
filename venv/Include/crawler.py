import feedparser

class Crawler:
    def __init__(sefl,url):
        sefl.url = url

    def RSS(sefl):
        feed = feedparser.parse(sefl.url)
        return feed


