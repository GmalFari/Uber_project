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
            print(f'User Registration is done: {serializer.data}')
            return Response({'msg': 'user is created'}, status=status.HTTP_201_CREATED)
        
        else:
             return Response({'msg': 'user not created'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class MyBookingList(APIView):
    def post(self, request):
        data=request.data
        
        driver_type=request.data.get('driver_type')

        driver_rating=request.data.get('driver_rating')

        car_type=request.data.get('car_type')

        transmission_type=request.data.get('transmission_type')

        driver=AddDriver.objects.all()

        if driver_type:
            driver=driver.filter(driver_type=driver_type)
        
        if driver_rating:
            driver=driver.filter(driver_rating=driver_rating)

        if car_type:
            driver=driver.filter(car_type=car_type)
        
        if transmission_type:
            driver=driver.filter(transmission_type=transmission_type)
       
        serializer=MyBookingSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        