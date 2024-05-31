# filename: bitcoin_news.py

import requests

# Your API key
api_key = '2a009d59e361430b97a1305cc997e68f'

# Get the latest 5 news articles related to Bitcoin
response = requests.get(f'https://newsapi.org/v2/everything?q=bitcoin&sortBy=publishedAt&pageSize=5&apiKey={api_key}')
articles = response.json()['articles']

for i, article in enumerate(articles, start=1):
    print(f'Article {i}:')
    print(f'Title: {article["title"]}')
    print(f'Description: {article["description"]}')
    print(f'URL: {article["url"]}')
    print()
