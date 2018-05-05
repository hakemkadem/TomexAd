from django.contrib import admin
from django.urls import path,include

from snippets.views import TestFromHomeIndex,PostList
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippets/',include('snippets.urls')),
    path('',include('MasterPage.urls')),
    path('TestIndex',TestFromHomeIndex,name="MainTest"),
    path('Post',PostList),
    path('accounts/',include('django.contrib.auth.urls'))
]


