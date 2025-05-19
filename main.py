from datetime import datetime
import requests
from transformers import pipeline
from gtts import gTTS
from IPython.display import Audio, display
import os

# Your NewsAPI key here
API_KEY = "eeee"


 
today = datetime.today().strftime("%Y-%m-%d")

# Fetch today's news without topic filter
def fetch_today_news_top_headlines():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",   # Change to your preferred country code
        "apiKey": API_KEY,
        "pageSize": 5
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        print("Error fetching news:", response.status_code)
        return []


articles = fetch_today_news_top_headlines()


# Load summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    if len(text) > 1000:
        text = text[:1000]
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    return filename

# Main

if not articles:
    print("No news articles found for today.")
else:
    for idx, article in enumerate(articles, 1):
        print(f"\n📰 Article {idx}: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"URL: {article['url']}")
        content = article.get("content") or article.get("description") or ""
        if not content:
            print("No content to summarize.")
            continue
        
        summary = summarize_text(content)
        print("🔍 Summary:", summary)

        audio_file = f"summary_{idx}.mp3"
        text_to_speech(summary, audio_file)
        display(Audio(audio_file))
