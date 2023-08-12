from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings
from authentication.models import User
from client_management.models import AddClient
from driver_management.models import AddDriver
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
        booking= PlaceBooking.objects.create(user=instance)
        booking.save()
        print(f"data saved:{booking}")



# def invoice_number():
#     number=000
#     for i in range(number):
#         inv += f"BK{i}"
#         print(inv)
#     return number

class Invoice(models.Model):
    invoicenumber =  models.IntegerField(null=True, blank=True)
    user =  models.ForeignKey(bookinguser, on_delete=models.CASCADE)
    driver = models.ForeignKey(AddDriver, on_delete=models.CASCADE)
    add_favourite = models.BooleanField(default=False)
    invoice_generate =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.full_name

    # def save(self, invoicenumber, *args, **kwargs):
    #     if invoicenumber == 000:
    #         number = self.invoicenumber + 1
    #         super(Invoice, number).save(*args, **kwargs)







