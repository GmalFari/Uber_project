from django.shortcuts import render
from rest_framework.views import APIView
from .models import Newuser
from .serializers import NewuserSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class Adduser(APIView):
    def get(self, request):
        all_user= Newuser.objects.all()
        serializer= NewuserSerializer(all_user, many=True)
        return Response({'msg':'Here is your data', 'data':serializer.data}, status=status.HTTP_200_OK)