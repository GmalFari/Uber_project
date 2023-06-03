from rest_framework import serializers
from .models import PlaceBooking


class MyBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceBooking
        fields = '__all__'
