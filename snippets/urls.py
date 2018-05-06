
from django.contrib import admin
from django.urls import path
from .views import PostList,TestIndex,TestFromHomeIndex,ActiveUsers
app_name = 'snippets'
urlpatterns = [
    path('post', PostList),
    path('currentUsers',ActiveUsers),
    path('TestIndex',TestIndex,name="Testifying"),
    path('TestFromHomeIndex',TestFromHomeIndex,name="MainPage")

]
