from django.urls import path

from .views import *

urlpatterns = [
    path('driver_detail/', MyDriverList.as_view(), name='driver-list'),
    path('driver_detail/<int:id>/', MyDriverGetList.as_view(), name='driver-list-id'),
]