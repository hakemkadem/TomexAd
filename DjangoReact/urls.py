
from django.contrib import admin
from django.urls import path,include
from snippets.views import TestFromHomeIndex


urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippets/',include('snippets.urls')),
    path('TestIndex',TestFromHomeIndex)
]
