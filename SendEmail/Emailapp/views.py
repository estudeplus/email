from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.core.mail import send_mail
import json


@api_view(["POST"])
def EnviarEmail(nome):
    try:

        recebido = json.loads(nome.body.decode('utf-8'))

        savedata(serializer)

    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

def savedata(serializer):
    student1 = Student.objects.create(nome=serializer.validated_data["nome"],
            matricula=serializer.validated_data["matricula"],
            email=serializer.validated_data["email"],
        )
        
    student1.save()