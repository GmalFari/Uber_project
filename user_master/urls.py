from django.urls import path
from .views import *

urlpatterns = [
    path('country/', MyCountryList.as_view(), name='country_list'),
    path('country/<str:pk>/', MyCountryGetList.as_view(), name='country-list-id'),
    path('state/', MyStateList.as_view(), name='state_list'),
    path('state/<str:pk>/', MyStateGetList.as_view(), name='state-list-id'),
    path('city/', MyCityList.as_view(), name='city_list'),
    path('city/<str:pk>/', MyCityGetList.as_view(), name='city-list-id'),
    path('location/', MyLocationList.as_view(), name='location_list'),
    path('location/<int:id>/', MyLocationGetList.as_view(), name='location-list-id'),
    path('zone/', MyZoneList.as_view(), name='Zone-list'),
    path('zone/<int:id>/', MyZoneGetList.as_view(), name='Zone-list-id'),
    path('branch/', MyBranchList.as_view(), name='branch_list'),
    path('branch/<int:id>/', MyBranchGetList.as_view(), name='branch-list-id'),

    # URL for User
    path('createuser/', createUsermaster.as_view(), name='createuser'),
    path('login/', Loginuser.as_view(), name='login'),
]
