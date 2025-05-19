# text-summarization-and-tts

# News Summarizer and Text-to-Speech

This project fetches the latest news headlines using the NewsAPI, summarizes the article content using Hugging Face's transformers, and converts the summaries into speech using Google's Text-to-Speech (gTTS) library. It is designed to run easily in Google Colab.

---

## Features

- Fetches top news headlines (default country: US) using [NewsAPI](https://newsapi.org/)
- Summarizes news articles with Hugging Face's `distilbart-cnn-12-6` summarization model
- Converts article summaries to audio using `gTTS`
- Plays the audio summaries directly in the notebook
- Easily customizable to change news source, number of articles, and language

---


