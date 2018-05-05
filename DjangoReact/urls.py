from django.contrib import admin
from django.urls import path,include
from snippets.views import TestFromHomeIndex,PostList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippets/',include('snippets.urls')),
    path('',include('MasterPage.urls')),
    path('TestIndex',TestFromHomeIndex,name="MainTest"),
    path('Post',PostList)
]
