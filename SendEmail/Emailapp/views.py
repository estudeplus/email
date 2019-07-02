from .models import Student
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
import json
from rest_framework import serializers
import io
from django.http import HttpResponse



class StudentSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    matricula = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=254)
    link = serializers.CharField(max_length=254)
    mensagem = serializers.CharField(max_length=254)


    @api_view(["POST"])
    def Retrive(nome):
        try:
            
            data =  json.loads(nome.body.decode('utf-8'))
            

            serializer = StudentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.validated_data        
            
            sendemail(serializer)
            savedata(serializer)
            
            
            return HttpResponse(status=200)
        except ValueError as e:
            return Response(status.HTTP_400_BAD_REQUEST)

def savedata(serializer):
    student1 = Student.objects.create(nome=serializer.validated_data["nome"],
            matricula=serializer.validated_data["matricula"],
            email=serializer.validated_data["email"],
        )
        
    student1.save()
            

def sendemail(serializer):
    send_mail(
        serializer.validated_data["mensagem"],
        serializer.validated_data["link"] + serializer.validated_data["link"],
        'estudeplus0@gmail.com',
        [serializer.validated_data["email"]],
        fail_silently=False,
    )







    
    
    