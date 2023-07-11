from django.urls import path
from .views import *

urlpatterns = [
    path('country/', MyCountryList.as_view(), name='country_list'),
    path('country/<str:pk>/', MyCountryGetList.as_view()),
    path('country/<str:pk>/update/', MyCountryGetList.as_view()),
   # path('country/<str:pk>/update/', MyCountryUpdate.as_view(), name='country_update_list'),
    path('country/<str:pk>/delete/', MyCountryDelete.as_view(), name='country_delete_list'),
    path('state/', MyStateList.as_view(), name='state_list'),
    path('state/<str:pk>/', MyStateGetList.as_view(), name='state_list_id'),
    path('state/<str:pk>/update/', MyStateUpdate.as_view(), name='state_update_list'),
    path('state/<str:pk>/delete/', MyStateDelete.as_view(), name='state_delete_list'),
]
