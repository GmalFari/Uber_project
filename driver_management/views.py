from rest_framework import generics
from .models import AddDriver
from .serializers import MyModelSerializer


class MyModelList(generics.ListCreateAPIView):
    queryset = AddDriver.objects.all()
    serializer_class = MyModelSerializer
    lookup_field = 'id'
