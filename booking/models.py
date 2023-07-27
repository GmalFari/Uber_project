from django.db import models
from client_management.models import AddClient
from driver_management.models import AddDriver
from datetime import datetime, date





class Clientregistration(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='clientregistration', null=True, blank=True)
    full_name=models.CharField(max_length=200, null=True, blank=True)
    mobile_number=models.BigIntegerField()
    city=models.CharField(max_length=100, null=True, blank=True)
    alternet_number=models.BigIntegerField()


    def __str__(self):
        return self.full_name
    
packege=(
        ('4Hours', '4Hours'),
        ('8Hours', '8Hours'),
        ('Night', 'Night')

    )
  
class PlaceBooking(models.Model):
    client_name = models.ForeignKey(Clientregistration, on_delete=models.CASCADE)
    trip_type=models.CharField(max_length=50, null=True ,blank=True)
    package=models.CharField(choices=packege, max_length=20, default='4Hours')
    user_curr_lat=models.FloatField()
    user_curr_long=models.FloatField()
    from_date = models.DateField()
    to_date = models.DateField()
    car_type=models.CharField(max_length=100, null=True)
    gear_type= models.CharField(max_length=100, null=True)
    pickup_location=models.CharField(max_length=100, null=True)
    drop_location=models.CharField(max_length=100, null=True)
    # driver=models.ForeignKey(AddDriver, on_delete=models.CASCADE)
    booking_time=models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.client_name.full_name
    

    # no_of_days = models.PositiveIntegerField()
    # start_time = models.TimeField()
    # coupon_code = models.CharField(max_length=15, null=True, blank=True)
    # religion = models.CharField(choices=(("1", "Hindu"), ("2", "Muslim"), ("3", "Christian"), ("4", "Sikh")),
    #                             max_length=10)
    # visiting_location = models.CharField(max_length=20)
    # request_type = models.CharField(choices=(("1", "Normal"), ("2", "Guest")),
    #                                 max_length=15)
    # trip_type = models.CharField(choices=(("1", "One Way"), ("2", "Round")),
    #                              max_length=15)

    



