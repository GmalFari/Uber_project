from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AddDriver
from .serializers import MyModelSerializer


class MyModelList(generics.ListCreateAPIView):
    queryset = AddDriver.objects.all()
    serializer_class = MyModelSerializer
    # lookup_field = 'id'


class DriverDetailsView(APIView):
    def get(self, request, id):
        try:
            driver = AddDriver.objects.get(id=id)
            serializer = MyModelSerializer(driver, many=True)
            return Response(serializer.data)
        except AddDriver.DoesNotExist:
            return Response({'error': 'Driver not found'}, status=404)
