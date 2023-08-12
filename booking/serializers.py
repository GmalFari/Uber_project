from rest_framework import serializers
from .models import  *
from driver_management.models import AddDriver
from driver_management.serializers import MyDriverSerializer
from user_master.models import Zone
from .models import bookinguser, Invoice
#from authentication.models import User
from authentication.serializers import NewUserSerializer
from authentication.models import  User

class ClientregistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = bookinguser
        fields = ['full_name', 'mobile_number', 'city', 'address']

        
class PlacebookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=False, read_only=False)
    class Meta:
        model = PlaceBooking
        
        fields= ['user','trip_type', 'from_date', 'to_date', 'car_type', 'gear_type', 'pickup_location', 'drop_location', 'booking_time']

        # def save(self, **kwargs):
        #     user = self.context['request'].user
        #     self.instance.user = user
        #     return super().save(**kwargs)

    user= serializers.SerializerMethodField()
    def get_user(self, obj):
        return obj.user.username



class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddDriver
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    driver =  serializers.SerializerMethodField()
    class Meta:
        model = Invoice
        fields = ('user', 'driver', 'add_favourite', 'invoice_generate')
    
    def get_driver(self, obj):
        driver =  obj.driver
        driver_seri = MyDriverSerializer(driver)
        return driver_seri.data
