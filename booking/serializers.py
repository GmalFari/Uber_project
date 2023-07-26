from rest_framework import serializers
from .models import  *
from driver_management.models import AddDriver
from user_master.models import Zone


class MyBookingSerializer(serializers.ModelSerializer):
    #zone= serializers.PrimaryKeyRelatedField(queryset=Zone.objects.all())
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