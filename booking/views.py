from rest_framework import generics
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from driver_management.models import AddDriver

from geopy.geocoders import Nominatim
import geocoder


class userregistration(APIView):
    def post(self, request):
        data=request.data
        serializer=ClientregistrationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'user is created'}, status=status.HTTP_201_CREATED)
        
        else:
             return Response({'msg': 'user is created'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class MyBookingList(APIView):
    def post(self, request):
        data=request.data
        location = Nominatim(user_agent="booking")
        currunt_loaction=request.data.get('currunt_loaction')
        getLocation=location.geocode(currunt_loaction)
        print(getLocation)
        request.POST._mutable = True
        data['currunt_loaction']= str(getLocation)
        serializer=MyBookingSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        