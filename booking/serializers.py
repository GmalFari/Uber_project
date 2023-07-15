from rest_framework import serializers
from .models import PlaceBooking, Clientregistration


class MyBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceBooking
        fields = '__all__'


class ClientregistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientregistration
        fields = '__all__'
