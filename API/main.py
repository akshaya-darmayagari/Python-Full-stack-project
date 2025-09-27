from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import NewsAggregator

app = FastAPI(title="Live News Aggregator", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

aggregator = NewsAggregator()

# Data Models
class NewsCreate(BaseModel):
    category: str
    headline: str

class NewsUpdate(BaseModel):
    category: str
    headline: str

# Endpoints
@app.get("/")
def home():
    return {"message": "Live News Aggregator API is running!"}

@app.get("/rss_news")
def fetch_rss_news():
    return aggregator.fetch_rss_news()

@app.get("/db_news")
def get_db_news():
    return aggregator.get_news_db()

@app.post("/db_news")
def insert_news(news: NewsCreate):
    result = aggregator.add_news(news.category, news.headline)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.put("/db_news/{id}")
def update_db_news(id: int, news: NewsUpdate):
    result = aggregator.update_news_db(id, news.headline, news.category)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

@app.delete("/db_news/{id}")
def delete_db_news(id: int):
    result = aggregator.delete_news_db(id)
    if not result["Success"]:
        raise HTTPException(status_code=400, detail=result["Message"])
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
