from django.urls import path
from . import views
# from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)

app_name = 'api-v1'

urlpatterns = [
    # register
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),

    # login
    # path('tiken/login/',ObtainAuthToken.as_view(),name='token_login'),
    path('token/login/',views.CustomAuthToken.as_view(),name='token_login'),

    # logout
    path('token/logout/',views.CustomDiscardAuthToken.as_view(),name='token_logout'),

    # jwt_login
    path('jwt/create/',TokenObtainPairView.as_view(),name='jwt_login'),
    path('jwt/refresh/',TokenRefreshView.as_view(),name='jwt_refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(),name='jwt_verify')




    
]