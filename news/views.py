import requests
from django.shortcuts import render

def fetch_news():
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4d87f5db6ec84dd1810a81124817926c"
    response = requests.get(url)
    data = response.json()
    return data.get("articles", [])

def news_home(request):
    articles = fetch_news()
    return render(request, 'news_home.html', {'articles': articles})
