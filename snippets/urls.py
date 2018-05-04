
from django.contrib import admin
from django.urls import path
from .views import PostList,TestIndex
urlpatterns = [
    path('post', PostList),
    path('TestIndex',TestIndex)
]
