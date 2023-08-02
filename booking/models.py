from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings
#from authentication.models import Newuser
from client_management.models import AddClient
# from driver_management.models import AddDriver
from datetime import datetime, date
from django.utils import timezone 
# from dateutil.parser import parse

class bookinguser(models.Model):
    cities=(
        ('Mumbai', 'Mumbai'),
        ("Navi Mumbai", "Navi Mumbai"),
        ("Thane", "Thane"),
        ("Pune", "Pune"),
        ("Bangaluru", "Bangaluru"),
        ("Delhi", "Delhi")
    )
    full_name=models.CharField(max_length=200, null=True, blank=True)
    mobile_number=models.CharField(max_length=14)
    city=models.CharField(choices=cities,max_length=100, null=True, blank=True, default="Mumbai")
    address= models.CharField(max_length=200, null=True, blank=True)
    


    def __str__(self):
        return self.full_name
    
  
class PlaceBooking(models.Model):
    client_name = models.ForeignKey(bookinguser, on_delete=models.CASCADE)
    trip_type=models.CharField(max_length=50, null=True ,blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    car_type=models.CharField(max_length=100, null=True)
    gear_type= models.CharField(max_length=100, null=True)
    pickup_location=models.CharField(max_length=100, null=True)
    drop_location=models.CharField(max_length=100, null=True)
    booking_time=models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.trip_type
    

@receiver(post_save, sender=PlaceBooking)
def create_profile(sender, instance, created, **kwargs):
    
    if created:
        # PlaceBooking.objects.create(instance)
        print("data saved")

    



