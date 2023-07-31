from rest_framework import serializers
from .models import  *
from driver_management.models import AddDriver
from user_master.models import Zone


class ClientregistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientregistration
        fields = ['full_name', 'mobile_number', 'city', 'alternet_number']

        
class MyBookingSerializer(serializers.ModelSerializer):
    #zone= serializers.PrimaryKeyRelatedField(queryset=Zone.objects.all())
    class Meta:
        model = PlaceBooking
<<<<<<< HEAD
        fields = ['trip_type', 'from_date','to_date','car_type', 'gear_type', 'pickup_location', 'drop_location']
=======
        fields = ['id', 'trip_type', 'packege', 'user_curr_lat', 'user_curr_long', 'from_date', 'to_date','car_type', 'gear_type','pickup_location', 'drop_location', 'booking_time']
>>>>>>> 3b863214f796e66470316d24c4829e269910068f
        # exclude=['client_name']




class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddDriver
        fields = '__all__'