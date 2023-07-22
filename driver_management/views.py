from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from dateutil.relativedelta import relativedelta
from rest_framework.parsers import MultiPartParser, FormParser

from datetime import date, datetime
from .utils import leavecalcu

class MyDriverList(generics.ListCreateAPIView):
    
    queryset = AddDriver.objects.all()
    serializer_class = MyDriverSerializer
    parser_classes = (MultiPartParser, FormParser)


class MyDriverGetList(APIView):
    def get(self, request, id):
        try:
            driver = AddDriver.objects.get(id=id)
            serializer = MyDriverSerializer(driver)
            return Response(serializer.data)
        except AddDriver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer_class = MyDriverSerializer

    def put(self, request, id):
        try:
            driver = AddDriver.objects.get(id=id)
            serializer = MyDriverSerializer(driver, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(request.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except AddDriver.DoesNotExist:
            Response({'msg': 'Search value not present in database'}, status=status.HTTP_417_EXPECTATION_FAILED)
            return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            driver = AddDriver.objects.get(id=id)
            driver.delete()
            return Response({'message': 'Object Deleted'}, status=status.HTTP_204_NO_CONTENT)
        except AddDriver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)


class Driversearch(ListAPIView):
    try:
        queryset = AddDriver.objects.all()
        serializer_class = MyDriverSerializer
        #
        filter_backends = [DjangoFilterBackend]

        filterset_fields = ['driver_type', 'first_name', 'driver_status', 'branch']
    except AddDriver.DoesNotExist:
        pass



# Driver Leave API

class Driverleaveapi(APIView):
    def post(self, request):
        data=request.data
        serializer=DriverleaveSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Driver Leave save'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'msg':'may be you missed some field'}, status=status.HTTP_400_BAD_REQUEST) 








