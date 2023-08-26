from django.urls import path
from . import views
# from djoser.views import (
#     TokenCreateView, TokenRefreshView, TokenDestroyView, UserCreateView, UserDeleteView, UserDetailView
# )
from rest_framework.authtoken.views import obtain_auth_token 


urlpatterns = [
    path('adduser/', views.Adduser.as_view(), name='adduser'),
    path('login/',views.LoginView.as_view(), name="login"),
    path('logout/', views.Logoutapi.as_view(), name='logout'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),  
    # path('auth/token/create/', TokenCreateView.as_view(), name='token_create'),
    # path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/token/destroy/', TokenDestroyView.as_view(), name='token_destroy'),
    # path('auth/users/create/', UserCreateView.as_view(), name='user_create'),
    # path('auth/users/delete/', UserDeleteView.as_view(), name='user_delete'),
    # path('auth/users/me/', UserDetailView.as_view(), name='user_detail'),
]