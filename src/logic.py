from src.db import create_news, get_all_news, update_news, delete_news
import feedparser

THE_HINDU_FEEDS = {
    "World": "https://www.thehindu.com/news/international/feeder/default.rss",
    "National": "https://www.thehindu.com/news/national/feeder/default.rss",
    "Telangana": "https://www.thehindu.com/news/national/telangana/feeder/default.rss",
    "Entertainment": "https://www.thehindu.com/entertainment/feeder/default.rss",
    "Sports": "https://www.thehindu.com/sport/feeder/default.rss"
}

class NewsAggregator:
    def fetch_rss_news(self, limit=10):
        data = {}
        for category, url in THE_HINDU_FEEDS.items():
            parsed = feedparser.parse(url)
            headlines = [(entry.title, entry.link) for entry in parsed.entries[:limit]]
            data[category] = headlines
        return data

    def add_news(self, category, headline):
        if not category or not headline:
            return {"Success": False, "Message": "Category & Headline required"}
        result = create_news(category, headline)
        if "error" in result:
            return {"Success": False, "Message": f"Error: {result['error']}"}
        return {"Success": True, "Message": "News added successfully!"}

    def get_news_db(self):
        result = get_all_news()
        if "error" in result:
            return []
        return result.data

    def update_news_db(self, id, headline, category):
        result = update_news(id, headline, category)
        if "error" in result:
            return {"Success": False, "Message": f"Error: {result['error']}"}
        return {"Success": True, "Message": "News updated successfully!"}

    def delete_news_db(self, id):
        result = delete_news(id)
        if "error" in result:
            return {"Success": False, "Message": f"Error: {result['error']}"}
        return {"Success": True, "Message": "News deleted successfully!"}
