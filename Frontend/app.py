# app.py

import streamlit as st
import requests
from datetime import datetime

# ------------------- Config -------------------
API_URL = "http://0.0.0.0:8000"  # Your FastAPI backend URL

st.set_page_config(page_title="Live News Aggregator", layout="wide")
st.title("📰 Live News Aggregator Dashboard")

# ------------------- View All News -------------------
st.header("All News")
try:
    response = requests.get(f"{API_URL}/news")
    if response.status_code == 200:
        news_data = response.json()
        if "data" in news_data:
            news_list = news_data["data"]
        else:
            news_list = news_data  # depends on your API response

        for news in news_list:
            st.markdown(f"**ID:** {news['id']} | **Category:** {news['category']} | **Headline:** {news['headline']}")
            st.markdown("---")
    else:
        st.error("Failed to fetch news")
except Exception as e:
    st.error(f"Error: {e}")

# ------------------- Add News -------------------
st.header("Add News")
with st.form("add_news_form"):
    category = st.text_input("Category")
    headline = st.text_input("Headline")
    source_url = st.text_input("Source URL")
    submitted = st.form_submit_button("Add News")

    if submitted:
        if not category or not headline or not source_url:
            st.warning("All fields are required")
        else:
            try:
                response = requests.post(
                    f"{API_URL}/news",
                    json={
                        "category": category,
                        "headline": headline,
                        "extracted_from_url": source_url
                    }
                )
                if response.status_code == 200:
                    st.success("News added successfully!")
                else:
                    st.error(f"Error: {response.json().get('detail')}")
            except Exception as e:
                st.error(f"Error: {e}")

# ------------------- Update News -------------------
st.header("Update News Headline")
with st.form("update_news_form"):
    news_id = st.text_input("News ID to Update")
    new_headline = st.text_input("New Headline")
    submitted = st.form_submit_button("Update News")

    if submitted:
        if not news_id or not new_headline:
            st.warning("Both fields are required")
        else:
            try:
                response = requests.put(
                    f"{API_URL}/news/{news_id}",
                    json={"headline": new_headline}
                )
                if response.status_code == 200:
                    st.success("News updated successfully!")
                else:
                    st.error(f"Error: {response.json().get('detail')}")
            except Exception as e:
                st.error(f"Error: {e}")

# ------------------- Delete News -------------------
st.header("Delete News")
with st.form("delete_news_form"):
    delete_id = st.text_input("News ID to Delete")
    submitted = st.form_submit_button("Delete News")

    if submitted:
        if not delete_id:
            st.warning("News ID is required")
        else:
            try:
                response = requests.delete(f"{API_URL}/news/{delete_id}")
                if response.status_code == 200:
                    st.success("News deleted successfully!")
                else:
                    st.error(f"Error: {response.json().get('detail')}")
            except Exception as e:
                st.error(f"Error: {e}")

# ------------------- Auto-Refresh Latest News -------------------
st.sidebar.header("Auto Refresh")
refresh_interval = st.sidebar.number_input("Refresh Interval (seconds)", value=600, min_value=60)

if st.sidebar.button("Refresh Now"):
    st.experimental_rerun()
