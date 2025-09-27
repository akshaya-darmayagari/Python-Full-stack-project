import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def create_news(category, headline):
    try:
        return supabase.table("news_articles").insert({
            "category": category,
            "headline": headline,
            "extracted_from_url": "https://www.thehindu.com"
        }).execute()
    except Exception as e:
        return {"error": str(e)}

def get_all_news():
    try:
        return supabase.table("news_articles").select("*").order("scraped_at", desc=True).execute()
    except Exception as e:
        return {"error": str(e)}

def update_news(id, headline, category):
    try:
        return supabase.table("news_articles").update({
            "headline": headline,
            "category": category
        }).eq("id", id).execute()
    except Exception as e:
        return {"error": str(e)}

def delete_news(id):
    try:
        return supabase.table("news_articles").delete().eq("id", id).execute()
    except Exception as e:
        return {"error": str(e)}
