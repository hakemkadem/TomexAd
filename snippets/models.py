from django.db import models
from django.conf import settings;
class Post(models.Model):
    user        =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title       =models.CharField(max_length=120, null=True,blank=True)
    contents    =models.CharField(max_length=120, null=True,blank=True)
    timestamp   =models.DateTimeField(auto_now_add=True)
    CountryID   =models.IntegerField(null=False, default=0)
    def __str__(self):
        return "Post Table"

class Country:
    CountryName = models.CharField(max_length=50,null=True,blank=True)
    CityName    = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return "Country Table"



