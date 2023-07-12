from django.shortcuts import render, HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response

from rest_framework import status
from .models import *
from .serializers import *
import requests


# Regsitering New user
class createUsermaster(APIView):
    def post(self, request):
        data = request.data
        
        serializer=UsermasterSerializer(data=data)
        if serializer.is_valid():
           
            serializer.save()
            msg = "User is created"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MyCountryList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    queryset = Country.objects.all()
    serializer_class = MyCountrySerializer


class MyCountryGetList(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    try:

        def get(self, request, pk):
            try:
                country = Country.objects.get(pk=pk)
                serializer = MyCountrySerializer(country)
                return Response(serializer.data)
            except Country.DoesNotExist:
                return Response({'error': 'Country not found'}, status=404)
    except:
        Response({'msg': 'Not Authenticated'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    serializer_class = MyCountrySerializer

    def put(self, request, pk):
        try:
            country = Country.objects.get(pk=pk)
            serializer = MyCountrySerializer(country, data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            print(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Country.DoesNotExist:
            return Response({'error': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            country = Country.objects.get(pk=pk)
            country.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Country.DoesNotExist:
            return Response({'error': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)


class MyStateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = MyStateSerializer


class MyStateGetList(APIView):
    def get(self, request, pk):
        try:
            state = State.objects.get(pk=pk)
            serializer = MyStateSerializer(state)
            return Response(serializer.data)
        except State.DoesNotExist:
            return Response({'error': 'State not found'}, status=404)

    serializer_class = MyStateSerializer

    def put(self, request, pk):
        try:
            state = State.objects.get(pk=pk)
            serializer = MyStateSerializer(state, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except State.DoesNotExist:
            return Response({'error': 'State not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            state = State.objects.get(pk=pk)
            state.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except State.DoesNotExist:
            return Response({'error': 'State not found'}, status=status.HTTP_404_NOT_FOUND)


class MyCityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = MyCitySerializer


class MyCityGetList(APIView):
    def get(self, request, pk):
        try:
            city = City.objects.get(pk=pk)
            serializer = MyCitySerializer(city)
            return Response(serializer.data)
        except Location.DoesNotExist:
            return Response({'error': 'City not found'}, status=404)

    serializer_class = MyCitySerializer

    def put(self, request, pk):
        try:
            city = City.objects.get(pk=pk)
            serializer = MyCitySerializer(city, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except City.DoesNotExist:
            return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            city = City.objects.get(pk=pk)
            city.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Location.DoesNotExist:
            return Response({'error': 'City not found'}, status=status.HTTP_404_NOT_FOUND)


class MyLocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = MyLocationSerializer


class MyLocationGetList(APIView):
    def get(self, request, id):
        try:
            location = Location.objects.get(id=id)
            serializer = MyLocationSerializer(location)
            return Response(serializer.data)
        except Location.DoesNotExist:
            return Response({'error': 'Location not found'}, status=404)

    serializer_class = MyLocationSerializer

    def put(self, request, id):
        try:
            location = Location.objects.get(id=id)
            serializer = MyLocationSerializer(location, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Location.DoesNotExist:
            return Response({'error': 'Location not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            location = Location.objects.get(id=id)
            location.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Location.DoesNotExist:
            return Response({'error': 'Location not found'}, status=status.HTTP_404_NOT_FOUND)


class MyZoneList(generics.ListCreateAPIView):
    queryset = Zone.objects.all()
    serializer_class = MyZoneSerializer


class MyZoneGetList(APIView):
    def get(self, request, id):
        try:
            zone = Zone.objects.get(id=id)
            serializer = MyZoneSerializer(zone)
            return Response(serializer.data)
        except Zone.DoesNotExist:
            return Response({'error': 'Zone not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer_class = MyZoneSerializer

    def put(self, request, id):
        try:
            zone = Zone.objects.get(id=id)
            serializer = MyZoneSerializer(zone, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Zone.DoesNotExist:
            return Response({'error': 'Zone not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            zone = Zone.objects.get(id=id)
            zone.delete()
            return Response({'message': 'Object deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Zone.DoesNotExist:
            return Response({'error': 'Zone not found'}, status=status.HTTP_404_NOT_FOUND)


class MyBranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = MyBranchSerializer


class MyBranchGetList(APIView):
    def get(self, request, id):
        try:
            branch = Branch.objects.get(id=id)
            serializer = MyBranchSerializer(branch)
            return Response(serializer.data)
        except Branch.DoesNotExist:
            return Response({'error': 'Branch does not exist'}, status=status.HTTP_404_NOT_FOUND)

    serializer_class = MyBranchSerializer

    def put(self, request, id):
        try:
            branch = Branch.objects.get(id=id)
            serializer = MyBranchSerializer(branch, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Branch.DoesNotExist:
            return Response({'error': 'Branch not found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        try:
            branch = Branch.objects.get(id=id)
            branch.delete()
            return Response({'message': 'object deleted'}, status=status.HTTP_204_NO_CONTENT)
        except Branch.DoesNotExist:
            return Response({'error': 'Branch does not exist'}, status=status.HTTP_404_NOT_FOUND)


def home(request):
    return render(request, 'user_master/index.html')
