from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import requests
from datetime import datetime
from dateutil import parser
from django.conf import settings

NEWS_API_KEY = settings.NEWS_API_KEY
# # Create your views here.
# https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=16315a35a8014e019491abe6dbd0a60f
class NewsView(View):
    def get(self,request):
        news_type = request.GET.get('type', 'all')
        header = {
            'Authorization': NEWS_API_KEY
            
        }
        
        # Set URL based on news_type
        if news_type == 'sports':
            url = 'https://newsapi.org/v2/top-headlines?country=us&category=sports'
            type_label = "Sports News"
        elif news_type == 'science':
            url = 'https://newsapi.org/v2/top-headlines?country=us&category=science'
            type_label = "Science News"
        elif news_type == 'headlines':
            url = 'https://newsapi.org/v2/top-headlines?country=us'
            type_label = "Top US Headlines"
        else:
            url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news'
            type_label = "BBC Top News"
                # Fetch data
        response = requests.get(url=url, headers=header)
        news_data = response.json()
        articles = news_data.get('articles', [])
        

        for article in articles:
            try:
                dt = parser.isoparse(article['publishedAt'])
                article['publishedAt'] = dt.date()  # <-- now it's a real date object
            except Exception as e:
                article['publishedAt'] = None 
        
        context = {
            'type':type_label,
            'data':articles
        }        
 
        return render(request,'news.html',context)


class TrendingTopicsView(View):
    def get(self,request):
        url_trending_topics = 'https://newsapi.org/v2/everything?q=sensex'
        url_bussiness_topics = 'https://newsapi.org/v2/everything?q=crypto'
        header = {#32df30cc819b4f7a819e4aa5cdaa4c1b
            'Authorization':'16315a35a8014e019491abe6dbd0a60f'
        }
        #Crypto Response
        response_crypto = requests.get(url=url_trending_topics,headers=header)
        crypto_news = response_crypto.json()
        articles_crypto = crypto_news.get('articles',[])

        #Bussiness Response
        response_bussiness = requests.get(url=url_bussiness_topics,headers=header)
        bussiness_news = response_bussiness.json()
        articles_bussiness = bussiness_news.get('articles',[])
        

        # Convert publishedAt to datetime object
        for article in articles_crypto:
            try:
                article['publishedAt'] = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            except:
                article['publishedAt'] = None
        context = {
            'articles_crypto':articles_crypto,
            'articles_bussiness':articles_bussiness
        } 

        return render(request,'trending-topics.html',context)
    


class SpecialReportsView(View):
    def get(self,request):
        url_inflation = 'https://newsapi.org/v2/everything?q=inflation'
        url_bitcoin = 'https://newsapi.org/v2/everything?q=bitcoin'
        header = {
            'Authorization':'16315a35a8014e019491abe6dbd0a60f'
        }
        
        #Bitcoin Response
        response_bitcoin = requests.get(url=url_bitcoin,headers=header)
        bitcoin_news = response_bitcoin.json()
        articles_bitcoin = bitcoin_news.get('articles',[])
        #Inflation Response
        response_inflation = requests.get(url=url_inflation,headers=header)
        inflation_news = response_inflation.json()
        articles_inflation = inflation_news.get('articles',[])
        # Convert publishedAt to datetime object
        for article in articles_inflation:
            try:
                article['publishedAt'] = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            except:
                article['publishedAt'] = None
        context = {
            'articles_inflation':articles_inflation,
            'articles_bitcoin':articles_bitcoin
        }
        return render(request,'special-reports.html',context)    



class TodaysPicView(View):
    def get(self,request):
        # https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=32df30cc819b4f7a819e4aa5cdaa4c1b
        url_today_news = 'https://newsapi.org/v2/top-headlines?sources=bbc-news'
        header = {
            'Authorization':'16315a35a8014e019491abe6dbd0a60f'
        }
        #BBC News Response
        response_bbc_news = requests.get(url=url_today_news,headers=header)
        bbc_news = response_bbc_news.json()
        articles_bbc_news = bbc_news.get('articles',[])
        
        # Convert publishedAt to datetime object
        for article in articles_bbc_news:
            try:
                article['publishedAt'] = datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            except:
                article['publishedAt'] = None

        context = {
            'articles_bbc_news':articles_bbc_news
        }
        return render(request,'todays-pic.html',context)
    

class TestingView(View):
    def get(self,request):
        news_type = request.GET.get('type', 'all')
        header = {
            'Authorization': '16315a35a8014e019491abe6dbd0a60f'
        }
        # Set URL based on news_type
        if news_type == 'sports':
            url = 'https://newsapi.org/v2/top-headlines?country=us&category=sports'
            type_label = "Sports News"
        elif news_type == 'science':
            url = 'https://newsapi.org/v2/top-headlines?country=us&category=science'
            type_label = "Science News"
        elif news_type == 'headlines':
            url = 'https://newsapi.org/v2/top-headlines?country=us'
            type_label = "Top US Headlines"
        else:
            url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news'
            type_label = "BBC Top News"
                # Fetch data
        response = requests.get(url=url, headers=header)
        news_data = response.json()
        articles = news_data.get('articles', [])

        for article in articles:
            try:
                dt = parser.isoparse(article['publishedAt'])
                article['publishedAt'] = dt.date()  # <-- now it's a real date object
            except Exception as e:
                article['publishedAt'] = None 
        
        context = {
            'type':type_label,
            'data':articles
        }        
 
        return render(request,'testing.html',context)   


class Cloning(View):
    def get(self,request):
        news_type = request.GET.get('type','all')
        header = {
            'Authorization':'16315a35a8014e019491abe6dbd0a60f'
        }
        if news_type == 'sports':
            url = 'https://newsapi.org/v2/top-headlines?country=us&category=sports'
            type_label = "Sports News"
        elif news_type == 'science':
            url = 'https://newsapi.org/v2/top-headlines?country=us&category=science'
            type_label = 'Science News'
        elif news_type == 'headlines':
            url = 'https://newsapi.org/v2/top-headlines?country=us'
            type_label = 'Top US Headlines'
        else:
            url = 'https://newsapi.org/v2/top-headlines?sources=bbc-news'
            type_label = 'BBC Top News'

        # Fetching Data Here 
        response = requests.get(url=url,headers=header)
        news_data = response.json()
        articles = news_data.get('articles',[])

        # For Date 
        for article in articles:
            try:
                dt = parser.isoparse(article['publishedAt'])
                article['publishedAt'] = dt.date()
            except Exception as e:
                article['publishedAt'] = None

        context = {
            'type':type_label,
            'data':articles
        }                 

        return render(request,'practice.html',context)