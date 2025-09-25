# src/logic.py

from src.db import DatabaseManager

class NewsAggregator:
    """
    Acts as a bridge between Frontend (Streamlit/FastAPI) and the database.
    """

    def __init__(self):
        # Create a database manager instance (this will handle db operations)
        self.db = DatabaseManager()

    # --- Create ---
    def add_news(self, category, headline, extracted_from_url):
        """
        Add a new news headline to the database.
        Returns a success/error message.
        """
        if not extracted_from_url or not headline:
            return {"Success": False, "Message": "URL & Headline are required"}
        
        # Call DB method to insert news
        result = self.db.create_news(category, headline, extracted_from_url)

        if result.get("Success"):
            return {"Success": True, "Message": "News added successfully!"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('error')}"}

    # --- Get news ---
    def get_news(self):
        """
        Get all the news from the database.
        """
        return self.db.get_all_news()

    # --- Update news ---
    def mark_complete(self, id,headline):
        """
        Mark a news as updated.
        """
        result = self.db.update_news(id,headline)
        if result.get("Success"):
            return {"Success": True, "Message": "News updated successfully"}
        return {"Success": False, "Message": f"Error: {result.get('error')}"}

    # --- Delete news ---
    def del_news(self, id):
        """
        Delete the news from the database.
        """
        result = self.db.delete_news(id)
        if result.get("Success"):
            return {"Success": True, "Message": "News deleted successfully"}
        return {"Success": False, "Message": f"Error: {result.get('error')}"}


