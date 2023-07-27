from rest_framework import serializers
from .models import  *
from driver_management.models import AddDriver
from user_master.models import Zone


class ClientregistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = userregistration
        fields = ['full_name', 'mobile_number', 'city', 'alternet_number']

        
class MyBookingSerializer(serializers.ModelSerializer):
    #zone= serializers.PrimaryKeyRelatedField(queryset=Zone.objects.all())
    class Meta:
        model = PlaceBooking
        fields = '__all__'
        # exclude=['client_name']




class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddDriver
        fields = '__all__'