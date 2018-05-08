from django.shortcuts import render
from rest_framework import generics
from snippets.models import Post
from snippets.serializers import PostSerializer
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.http import HttpResponse;
from django.core import serializers;
from snippets.models import Post
import json


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




@csrf_exempt
def ActiveUsers(request):
    counts =request.online_now.count();
    data = {"Data":counts}
    return JsonResponse(data)

@csrf_exempt
def TestPost(request):
    RecievedData = list(json.loads(request.POST.get('deal', None)))
    po =Post();
    po.user=request.user;
    po.title=RecievedData[0]['title']
    po.contents = RecievedData[0]['contents']
    po.timestamp = RecievedData[0]['timestamp']
    po.save()
    return JsonResponse({"Data":RecievedData})



# This webservice is used to receive data and send related data using json format
@csrf_exempt
def TestGet(request):
    ResponseData={};
    Newdata=request.GET;
    user=User.objects.filter(username=Newdata['name']);
    ResponseData={"id":user[0].pk};
    return JsonResponse(ResponseData)
    # return HttpResponse(serializers.serialize("json", user),
    #                          content_type='application/json')


from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle

from reportlab.lib.pagesizes import letter, inch
import 
cm = 2.54

def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'

    style = ParagraphStyle(
        name='Normal',

        fontSize=8,
    )
    doc = SimpleDocTemplate(response, pagesize=letter)
    # container for the 'Flowable' objects
    elements = []

    data = [['00', '01', '02', '03', '04'],
            ['10', '11', '12', '13', '14'],
            ['20', '21', '22', '23', '24'],
            ['30', '31', '32', '33', '34']]
    t = Table(data, 5 * [0.4 * inch], 4 * [0.4 * inch])
    t.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                           ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
                           ('VALIGN', (0, 0), (0, -1), 'TOP'),
                           ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                           ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                           ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                           ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                           ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                           ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                           ]))

    elements.append(t)
    # write the document to disk
    styles = getSampleStyleSheet()
    elements.append(Paragraph("حاكم الكنبي", style = style))
    doc.build(elements)

    return response

    # return response



