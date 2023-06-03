from rest_framework import generics
from .models import PlaceBooking
from .serializers import MyBookingSerializer


class MyBookingList(generics.ListCreateAPIView):
    queryset = PlaceBooking.objects.all()
    serializer_class = MyBookingSerializer
