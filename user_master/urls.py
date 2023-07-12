from django.urls import path
from .views import *

urlpatterns = [
    path('country/', MyCountryList.as_view(), name='country_list'),
    path('country/<str:pk>/', MyCountryGetList.as_view()),
    
    path('country/<str:pk>/update/', MyCountryUpdate.as_view(), name='country_update_list'),
    path('country/<str:pk>/delete/', MyCountryDelete.as_view(), name='country_delete_list'),
    path('state/', MyStateList.as_view(), name='state_list'),
    path('state/<str:pk>/', MyStateGetList.as_view(), name='state_list_id'),
    path('state/<str:pk>/update/', MyStateUpdate.as_view(), name='state_update_list'),
    path('state/<str:pk>/delete/', MyStateDelete.as_view(), name='state_delete_list'),
    path('city/', MyCityList.as_view(), name='city_list'),
    path('city/<str:pk>/', MyCityGetList.as_view(), name='city_list_id'),
    # path('city/<str:pk>/update/', MyCityUpdate.as_view(), name='city_update_list'),
    path('city/<str:pk>/delete/', MyCityDelete.as_view(), name='city_delete_list'),
    path('location/', MyLocationList.as_view(), name='location_list'),
    path('location/<int:id>/', MyLocationGetList.as_view(), name='location_list_id'),
    path('location/<int:id>/update/', MyLocationUpdate.as_view(), name='location_update_list'),
    path('location/<int:id>/delete/', MyLocationDelete.as_view(), name='location_delete_list'),

    # URL for User
    path('createuser/', createUsermaster.as_view(), name='createuser'),
    path('login/', Loginuser.as_view(), name='login'),
]
