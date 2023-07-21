from django.urls import path

from . import views

urlpatterns=[
    path('userregistration/', views.userregistration.as_view(), name='userregistration'),
    path('booking/', views.MyBookingList.as_view(), name='booking-list'),
    path('search_drivers/', views.SearchDriverWithinRadius.as_view(), name='search_drivers'),
]