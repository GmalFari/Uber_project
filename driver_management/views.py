from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import AddDriver
from .serializers import MyModelSerializer




class Mydriver(generics.ListCreateAPIView):
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
        
class Driversearch(ListAPIView):
        try:
            queryset=AddDriver.objects.all()
            serializer_class=MyModelSerializer
            # 
            filter_backends = [DjangoFilterBackend]
            
            filterset_fields= ['driver_type','first_name', 'driver_status']
            

        except AddDriver.DoesNotExist:
            pass
