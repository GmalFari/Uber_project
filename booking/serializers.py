from rest_framework import serializers
from .models import  *
from driver_management.models import AddDriver
from user_master.models import Zone
from .models import bookinguser
#from authentication.models import User


class ClientregistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = bookinguser
        fields = ['full_name', 'mobile_number', 'city', 'address']

        
class MyBookingSerializer(serializers.ModelSerializer):
    client_name = serializers.PrimaryKeyRelatedField(queryset=bookinguser.objects.all())
    class Meta:
        model = PlaceBooking
        fields = ['client_name','trip_type', 'from_date','to_date','car_type', 'gear_type', 'pickup_location', 'drop_location', 'booking_time']
        # exclude=['client_name']




class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddDriver
        fields = '__all__'