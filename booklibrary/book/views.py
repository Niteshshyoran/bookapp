from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import UserSerializer
from django.http import HttpResponse
import datetime
# Create your views here.


class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'sign up sucessfull'})
        return Response ({'message':"invalid input"})
    

