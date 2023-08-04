from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import NewUserSerializer

from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
#from django.contrib.auth.models import User

# Create your views here.


class Adduser(APIView):
    def post(self, request):
        data= request.data
        serailizer=NewUserSerializer(data=data)
        if serailizer.is_valid():
            serailizer.save()
            return Response({'msg':'Data is saved', 'data': serailizer.data}, status=status.HTTP_201_CREATED)
        
        return Response({'msg':'Error in sav data', 'data': serailizer.errors})
       
    # def get(self, request):
    #     all_user= User.objects.all()
    #     serializer= UserSerializer(all_user, many=True)
    #     return Response({'msg':'Here is your data', 'data':serializer.data}, status=status.HTTP_200_OK)