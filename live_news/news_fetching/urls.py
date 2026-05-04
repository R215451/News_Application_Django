from django.contrib import admin
from django.urls import path
from news_fetching.views import NewsView,TrendingTopicsView,SpecialReportsView,TodaysPicView,TestingView,Cloning

urlpatterns = [
    path('', NewsView.as_view(),name='live'),
    path('trending/',TrendingTopicsView.as_view(),name='trending'),
    # path('trending-topics/', TrendingTopicsView.as_view(),name='trending'),
    path('special/', SpecialReportsView.as_view(),name='special'),
    path('today/', TodaysPicView.as_view(),name='today'),
    path('testing/',TestingView.as_view(),name='testing'),
    path('clone/',Cloning.as_view(),name='clone'),
]
