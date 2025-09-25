## 📰 Live News Aggregator

This project is a news aggregator system that collects the latest headlines from multiple RSS feeds (e.g., The Hindu) and provides them to users in a structured and interactive way. The news is categorized into World, National, State,Entertainment(Movies), and Sports, making it easy for users to browse topics of interest.

## Features

#  Automated News Scraping
Collects the latest headlines from RSS feeds like The Hindu automatically.
#  Categorized News
Organizes news into World, National, State, and Sports categories for easy browsing.
# Supabase Storage
Stores headlines, URLs, categories, and timestamps efficiently in a Postgres database.
# FastAPI Endpoints
Provides a REST API to fetch news data in JSON format with automatic documentation.
#  Streamlit Frontend
Displays the latest news in an interactive and clean web interface.
# Modular Architecture
Backend, API, and frontend are decoupled, making the system lightweight and easy to maintain.q

## Project Structure

Live News Aggregator/
|
|---src/             #core application logic
|    |---logic.py    #Business logic and tasks
opertions
|    |---db.py       #Database operations
|
|---API/             #Backend API
|   |---main.py      #FastAPI endpoints
|
|---Frondend/        #Frondend application
|   |---app.py       #Streamlit web interface
|
|---requirements.txt  #Python dependencies
|
|---README.md         #Project documentation
|
|---.env              #Python Variables

## Quick start

### Prerequisities

- Python 3.8 or higher
- A Supabase account
- Git(Push,cloning)

### 1.Clone or Download the Project
# Option 1: Clone with Git
git clone `https://github.com/akshaya-darmayagari/Python-Full-stack-project.git`

# Option 2:Download and extract the ZIP file

### 2.Install Dependencies

# Install all required Python packages
pip install -r requirements.txt

### 3.Set Up Supabase Database

1.Create a Supabse Project:

2.Create the news_articles Table:

-Go to the SQL Editor in your Supabse dashboard
-Run this SQL command:

```sql
create table news_articles (
  id uuid primary key default gen_random_uuid(),
  category text,
  headline text not null,
  extracted_from_url text unique not null,
  scraped_at timestamp default now()
);

```

3. **Get Your Credentials:

### 4.Configure Environment Variables

1.Create a `.env` file in the project root

2.Add Your Superbase credentials to `.env`:
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here

**Example:**
SUPABASE_URL="https://uyvclvdyqxhhyfbyavcl.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV5dmNsdmR5cXhoaHlmYnlhdmNsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODIzNzAsImV4cCI6MjA3MzY1ODM3MH0.ARzZPVOMf6roG7wmtqBEaUAIrHP5oBthyYocQW7H8Mw"

### 5.Run the Application

## Streamlit Frontend
streamlit run Frontend/app.py

The app will open in your browswer at `http://localhost:8501`

## FastAPI Backend

cd API
python main.py

The API will be availabe at `http://loaclhost:8000`

## How to Use

## Technical Details

### Technologies Used
-**Frontend**:Streamlit(Python web framework)
-**Backend**:FastAPI(Python REST API framework)
-**Database**: Supabase(PostgreSQL-bases backend-as-a-service)
-**Language**:Python 3.8+

### Key Components

1.**`src\db.py`**:Database operations 
  -Handles all CRUD operations with Supabase

2.**`src\logic.py`**:Business logic
  -Taks validation and processing

## Troubleshooting

## Common Isuues

1. **Module not found errors**
  -Make sure you've installed all dependencies:`pip install -r requirements.txt`
  -Check that you're running commands from the correct directory

### Future Enhancements

Ideas for extending this project:

## Multi-Source Integration
Add support for multiple news sources and RSS feeds beyond The Hindu.
## Search Functionality
Allow users to search news by keywords or topics.
## Personalized News Feed
Enable users to select preferred categories and get  customized news feed.
## Notifications & Alerts
Send real-time notifications for breaking news or category-specific updates.
## Trending & Popular News
Highlight trending articles or the most-read news in each category.
## Save & Bookmark Articles
Allow users to save or bookmark articles for later reading.
## Multi-Language Support
Include news in multiple languages for a wider audience.
## Advanced Analytics
Provide statistics like the number of articles per category, daily updates, or source popularity.

## Support

If you encounter any isuues or have questions:
mail to:`akshayadarmayagari@gmail.com`
contact:`9100034402`


