from django.shortcuts import render
from rest_framework import generics
from snippets.models import Post
from snippets.serializers import PostSerializer
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

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






# class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
#     lookup_field = 'pk'
#     serializer_class = PostSerializer
#
#     def get_queryset(self):
#         return Post.objects.all()
