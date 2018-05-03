
from django.contrib import admin
from django.urls import path
from .views import PostList
urlpatterns = [
    path('post', PostList),
]
