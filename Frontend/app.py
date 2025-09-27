# Frontend/app.py
import streamlit as st
import feedparser
import requests

API_URL = "http://localhost:8000"

# RSS Feeds
feeds = {
    "World": "https://www.thehindu.com/news/international/feeder/default.rss",
    "National": "https://www.thehindu.com/news/national/feeder/default.rss",
    "Telangana": "https://www.thehindu.com/news/national/telangana/feeder/default.rss",
    "Sports": "https://www.thehindu.com/sport/feeder/default.rss",
    "Entertainment": "https://www.thehindu.com/entertainment/feeder/default.rss",
    "Business": "https://www.thehindu.com/business/feeder/default.rss"
}

st.set_page_config(page_title="📰 Live News Aggregator", layout="wide", page_icon="📰")

# Main heading
st.markdown("<h1 style='color:darkblue; text-align:center;'>📰 Live News Aggregator</h1>", unsafe_allow_html=True)
st.markdown("---")

# CSS Styling
st.markdown("""
<style>
/* Sidebar menu color */
.css-1aumxhk { 
    color: darkgreen;  /* changed menu color */
    font-weight: bold; 
    font-size: 18px;
}

/* Buttons */
.stButton>button {
    background-color: #ADD8E6;
    color: black;
    font-weight: bold;
    border-radius: 6px;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #87CEFA;
    transform: scale(1.05);
    box-shadow: 0 0 10px #87CEFA;
}

/* Category headings */
.category { color: orange; font-size: 22px; font-weight: bold; }

/* Headlines hover effect */
.headline:hover { color: #FF4500; cursor: pointer; }
</style>
""", unsafe_allow_html=True)

# Sidebar menu
st.sidebar.title("📌 Menu")
choice = st.sidebar.radio("Select Action", ["View News", "Add News", "Update News", "Delete News", "View Stored News"])

# ------------------- VIEW NEWS -------------------
if choice == "View News":
    st.subheader("📰 Live News from The Hindu")
    for category, url in feeds.items():
        st.markdown(f"<div class='category'>{category}</div>", unsafe_allow_html=True)
        parsed = feedparser.parse(url)
        for entry in parsed.entries[:10]:
            st.markdown(
                f"<a href='{entry.link}' target='_blank' class='headline' style='color:black; text-decoration:none;'>• {entry.title}</a>",
                unsafe_allow_html=True
            )
        st.markdown("---")

# ------------------- ADD NEWS -------------------
elif choice == "Add News":
    st.subheader("➕ Add News")
    category = st.selectbox("Select Category", list(feeds.keys()))
    headline = st.text_input("Enter Headline")

    if st.button("Add News"):
        if headline:
            try:
                res = requests.post(f"{API_URL}/db_news", json={
                    "category": category,
                    "headline": headline
                })
                if res.status_code == 200:
                    st.success("✅ News added successfully!")
                else:
                    st.error(f"❌ Failed to add news: {res.json().get('detail')}")
            except Exception as e:
                st.error(f"❌ Failed to add news: {e}")
        else:
            st.warning("⚠️ Please enter a headline.")

# ------------------- UPDATE NEWS -------------------
elif choice == "Update News":
    st.subheader("🔄 Update News")
    try:
        res = requests.get(f"{API_URL}/db_news")
        data = res.json()
        for item in data:
            st.markdown(f"ID: {item['id']} | {item['category']} - {item['headline']}")
        news_id = st.number_input("Enter ID to Update", min_value=1, step=1)
        new_category = st.selectbox("Select New Category", list(feeds.keys()))
        new_headline = st.text_input("Enter New Headline")

        if st.button("Update News"):
            if new_headline:
                try:
                    res = requests.put(f"{API_URL}/db_news/{news_id}", json={
                        "headline": new_headline,
                        "category": new_category
                    })
                    if res.status_code == 200:
                        st.success("✅ News updated successfully!")
                    else:
                        st.error(f"❌ Failed to update: {res.json().get('detail')}")
                except Exception as e:
                    st.error(f"❌ Failed to update: {e}")
            else:
                st.warning("⚠️ Please enter a new headline.")
    except Exception as e:
        st.error(f"❌ Could not fetch stored news: {e}")

# ------------------- DELETE NEWS -------------------
elif choice == "Delete News":
    st.subheader("🗑 Delete News")
    try:
        res = requests.get(f"{API_URL}/db_news")
        data = res.json()
        for item in data:
            st.markdown(f"ID: {item['id']} | {item['category']} - {item['headline']}")
        news_id = st.number_input("Enter ID to Delete", min_value=1, step=1)

        if st.button("Delete News"):
            try:
                res = requests.delete(f"{API_URL}/db_news/{news_id}")
                if res.status_code == 200:
                    st.success("✅ News deleted successfully!")
                else:
                    st.error(f"❌ Failed to delete: {res.json().get('detail')}")
            except Exception as e:
                st.error(f"❌ Failed to delete: {e}")
    except Exception as e:
        st.error(f"❌ Could not fetch stored news: {e}")

# ------------------- VIEW STORED NEWS -------------------
elif choice == "View Stored News":
    st.subheader("📰 Stored News")
    try:
        res = requests.get(f"{API_URL}/db_news")
        data = res.json()
        for item in data:
            st.markdown(
                f"<p style='color:black;'>ID: {item['id']} | {item['category']} - {item['headline']}</p>",
                unsafe_allow_html=True
            )
    except Exception as e:
        st.error(f"❌ Could not fetch stored news: {e}")
