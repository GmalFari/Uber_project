from rest_framework import generics
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from driver_management.models import AddDriver

from geopy.geocoders import Nominatim
import geocoder

from math import sin, radians, cos, sqrt, atan2


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


class SearchDriverWithinRadius(APIView):
    def haversine_distance(self, lat1, lon1, lat2, lon2):
        # Convert latitude and longitude from degrees to radians
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        radius = 6371  # Earth's radius in kilometers
        distance = radius * c

        return distance

    def get(self, request):
        client_latitude = request.query_params.get('client_latitude')
        client_longitude = request.query_params.get('client_longitude')
        if not client_latitude or not client_longitude:
            return Response([])

        client_latitude = float(client_latitude)
        client_longitude = float(client_longitude)

        # Filter drivers within 3 km from the client location.
        drivers = Driver.objects.all()
        filtered_drivers = []

        for driver in drivers:
            distance = self.haversine_distance(
                client_latitude, client_longitude, driver.latitude, driver.longitude
            )
            if distance <= 3:
                filtered_drivers.append(driver)

        serializer = DriverSerializer(filtered_drivers, many=True)
        return Response(serializer.data)