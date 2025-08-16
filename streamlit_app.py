import streamlit as st
import feedparser

st.title("📰 News Dashboard")

# Example RSS feeds
sources = {
    "Reuters World": "https://feeds.reuters.com/reuters/worldNews",
    "Guardian Politics": "https://www.theguardian.com/politics/rss",
}

choice = st.selectbox("Choose source", list(sources.keys()))

feed = feedparser.parse(sources[choice])

for entry in feed.entries[:10]:
    st.subheader(entry.title)
    st.write(entry.summary)
    st.markdown(f"[Read more]({entry.link})")
