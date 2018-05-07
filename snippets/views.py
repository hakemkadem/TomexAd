from django.shortcuts import render
from rest_framework import generics
from snippets.models import Post
from snippets.serializers import PostSerializer
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def TestFromHomeIndex(request):
   return render(request,'snippets/main.html')


def TestIndex(request):
   return render(request,'snippets/Test.html')

@csrf_exempt
def PostList(request):
    if(request.method=="GET"):
        post=Post.objects.all()
        seralizer = PostSerializer(post,many=True)
        return JsonResponse(seralizer.data,safe=False)
    elif (request.method=="POST"):
        data=JSONParser.parse(request)
        seralizer=PostSerializer(data=data)
        if(seralizer.is_valid()):
            seralizer.save()
            return JsonResponse(data==data,status=201)
        return JsonResponse(seralizer.errors,status=401)


from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.http import HttpResponse;
from django.core import serializers;

@csrf_exempt
def ActiveUsers(request):
    counts =request.online_now.count();
    data = {"Data":counts}
    return JsonResponse(data)



# class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
#     lookup_field = 'pk'
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         return Post.objects.all()
