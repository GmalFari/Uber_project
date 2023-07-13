from django.urls import path
from .views import *

urlpatterns =[
    path('api/driver/', Mydriver.as_view(), name='driver-list'),
    path('api/driver/<int:id>', DriverDetailsView.as_view()),
    path('api/search/', Driversearch.as_view(), name='search_driver'),
]