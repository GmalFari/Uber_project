from django.shortcuts import render, HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class MyCountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = MyCountrySerializer


class MyCountryGetList(APIView):
    def get(self, request, pk):
        try:
            country = Country.objects.get(pk=pk)
            serializer = MyCountrySerializer(country)
            return Response(serializer.data)
        except Country.DoesNotExist:
            return Response({'error': 'Country not found'}, status=404)


class MyCountryUpdate(APIView):
    def put(self, request, pk):
        try:
            country = Country.objects.get(pk=pk)
            serializer = MyCountrySerializer(country, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Country.DoesNotExist:
            return Response({'error': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)


class MyCountryDelete(APIView):
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


class MyStateUpdate(APIView):
    def put(self, request, pk):
        try:
            state = State.objects.get(pk=pk)
            serializer = MyCountrySerializer(state, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except State.DoesNotExist:
            return Response({'error': 'State not found'}, status=status.HTTP_404_NOT_FOUND)


class MyStateDelete(APIView):
    def delete(self, request, pk):
        try:
            state = State.objects.get(pk=pk)
            state.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except State.DoesNotExist:
            return Response({'error': 'State not found'}, status=status.HTTP_404_NOT_FOUND)


def home(request):
    return render(request, 'user_master/index.html')
