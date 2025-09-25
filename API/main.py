# API/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Import NewsAggregator from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import NewsAggregator

# --------------------------- App Setup ---------------------------
app = FastAPI(title="Live News Aggregator", version="1.0")

# --------------------------- Allow frontend to call API ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a NewsAggregator instance
news_aggregator = NewsAggregator()

# ------- Data Models -------
class NewsCreate(BaseModel):
    category: str
    headline: str
    extracted_from_url: str

class NewsUpdate(BaseModel):
    headline: str  # we need the new headline to update

# ------------ Endpoints -------
@app.get("/")
def home():
    return {"message": "Live News Aggregator API is running!"}

@app.get("/news")
def get_news():
    return news_aggregator.get_news()

@app.post("/news")
def create_news(news: NewsCreate):
    result = news_aggregator.add_news(news.category, news.headline, news.extracted_from_url)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.put("/news/{id}")
def update_news(id: int, news: NewsUpdate):
    result = news_aggregator.mark_complete(id, news.headline)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

@app.delete("/news/{id}")
def delete_news(id: int):
    result = news_aggregator.delete_news(id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("Message"))
    return result

# ------- Run -------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
