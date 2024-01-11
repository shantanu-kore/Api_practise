from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Teacher
from django.contrib.auth.models import User
from django.db.models import Q
from django .http import JsonResponse
from .serializers import Studentserializer,Teacherserializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def student(request):
    
    if request.method=='GET':
        stdlist=Student.objects.all()
        serializer=Studentserializer(stdlist,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        jsonData=JSONParser().parse(request)
        print(jsonData)
        serializer=Studentserializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)




def userlist(request):
    tech=User.objects.all()
    ss=Teacherserializer(tech, many=True)
    return JsonResponse(ss.data,safe=False)
@csrf_exempt
def primary(request,pk):
    
    try:
        msg=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse(status=404)

    

    
        
    if request.method =="GET":
        serializer=Studentserializer(msg)
        return JsonResponse(serializer.data)
    elif request.method =="PUT":
        data=JSONParser().parse(request)
        serializer=Studentserializer(msg,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)
    elif request.method=='DELETE':
        msg.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
        
        
        
        
        

        
    