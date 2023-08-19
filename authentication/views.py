from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import NewUserSerializer, UserLoginserializer

from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token


# Create your views here.


class Adduser(APIView):
    def post(self, request):
        data= request.data
        serailizer=NewUserSerializer(data=data)
        if serailizer.is_valid():
            serailizer.save()
            return Response({'msg':'Data is saved', 'data': serailizer.data}, status=status.HTTP_201_CREATED)
        
        return Response({'msg':'Error in sav data', 'data': serailizer.errors})
       
    def get(self, request):
        all_user= User.objects.all()
        serializer= NewUserSerializer(all_user, many=True)
        return Response({'msg':'Here is your data', 'data':serializer.data}, status=status.HTTP_200_OK)
    

class LoginView(APIView):
    def post(self, request):
        data =  request.data

        phone = request.data.get('phone')
        password = request.data.get('password')
       
        currunt_user = request.user
           
        user = authenticate(phone=phone, password=password)
        if user is not None:
            login(request, user)
            #token = Token.objects.get_or_create(user=user)
            return Response({"msg":" Welcome Customer", 'data':"serializer.data"}, status=status.HTTP_200_OK)
                
                # 
                
        else:
            return Response({"msg":" unable to login", 'data':"serializer.errors"}, status=status.HTTP_401_UNAUTHORIZED)
            
        
            
