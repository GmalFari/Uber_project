from django.urls import path

from . import views

urlpatterns=[
    path('userregistration/', views.userregistration.as_view(), name='user_registration'),
    path('booking/', views.MyBookingList.as_view(), name='booking-list'),
]