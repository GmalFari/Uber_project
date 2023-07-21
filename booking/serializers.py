from rest_framework import serializers
from .models import  *
from driver_management.models import AddDriver


class MyBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceBooking
        fields = '__all__'


class ClientregistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientregistration
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddDriver
        fields = '__all__'