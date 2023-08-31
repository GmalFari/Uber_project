from django.contrib import admin
from .models import *

# this is to enable colors on the map in model page
from django.contrib.gis.admin import GISModelAdmin

# enable colors
class PlaceBookingAdmin(GISModelAdmin):
    #tuple([field.name for field in PlaceBooking._meta.get_fields()])
    pass
admin.site.register( PlaceBooking,PlaceBookingAdmin)

# admin.site.register(bookinguser)
# admin.site.register(PlaceBooking)
admin.site.register(Invoice)
admin.site.register(Feedback)


