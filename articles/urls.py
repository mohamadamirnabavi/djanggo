
from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "articles"

urlpatterns = [
    path('', views.articles_list, name="list"),
    path('create', views.create_articles, name="create"),
    path('<slug>', views.article_detail, name="detail"),
]

