from rest_framework import serializers
from .models import  *
from driver_management.models import AddDriver
from user_master.models import Zone
from .models import bookinguser
from authentication.models import Newuser


class ClientregistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = bookinguser
        fields = ['full_name', 'mobile_number', 'city', 'address']

        
class PlacebookingSerializer(serializers.ModelSerializer):
    client_name= serializers.SerializerMethodField()
    class Meta:
        model = PlaceBooking
        fields = ['client_name','trip_type', 'from_date', 'to_date', 'car_type', 'gear_type', 'pickup_location', 'drop_location', 'booking_time']
    def get_client_name(self, obj):
        return obj.client_name



class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddDriver
        fields = '__all__'