from django.db import models
from client_management.models import AddClient


class PlaceBooking(models.Model):
    client_name = models.ForeignKey(AddClient, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    no_of_days = models.PositiveIntegerField()
    start_time = models.TimeField()
    coupon_code = models.CharField(max_length=15, null=True, blank=True)
    religion = models.CharField(choices=(("1", "Hindu"), ("2", "Muslim"), ("3", "Christian"), ("4", "Sikh")),
                                max_length=10)
    visiting_location = models.CharField(max_length=20)
    request_type = models.CharField(choices=(("1", "Normal"), ("2", "Guest")),
                                    max_length=15)
    trip_type = models.CharField(choices=(("1", "One Way"), ("2", "Round")),
                                 max_length=15)

    def __str__(self):
        return self.client_name



