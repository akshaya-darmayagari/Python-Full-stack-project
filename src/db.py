# db_manager.py
import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# Create news
def create_news(category, headline, extracted_from_url):
    return supabase.table("news_articles").insert({
        "category": category,
        "headline": headline,
        "extracted_from_url": extracted_from_url,
    }).execute()

# get all headlines
def get_all_news():
    return supabase.table("news_articles").select("*").order("scraped_at").execute()

# Update news headline
def update_news(id, headline):
    return supabase.table("news_articles").update(
        {"headline": headline}   
    ).eq("id", id).execute()    

# Delete news headline
def delete_news(id):
    return supabase.table("news_articles").delete().eq("id", id).execute()
