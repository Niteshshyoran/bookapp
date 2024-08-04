from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Author,Books,Country
from .serializer import UserSerializer,AuthorSerializer,BookSerializer,CountrySerializer
from django.http import HttpResponse
import datetime
from rest_framework import pagination
# from django.contrib.auth import login,logout,authenticate
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.


class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'sign up sucessfull'})
        return Response ({'message':"invalid input"})
    

class loginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.all
        if user is None:
            return Response({'message':'user not register'})
        # if not user.cheak_password(password):
        return Response({'message':'login sucessfull'})

class AuthorRegisterView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class AuthorUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class BookRegisterView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer



class BookUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer



class CountryRegisterView(CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer





# pagenumber = CustomPagination


# class CustomPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 10000
    