from django.shortcuts import render
from snippets.views import PostList
from snippets.models import Post
# Create your views here.

def MasterPage(request):
    return  render(request,'MasterPage/MasterIndex.html');

def HomePage (request):
    return render(request,'MasterPage/HomePage.html');
