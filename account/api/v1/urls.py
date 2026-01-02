from django.urls import path
from . import views
# from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'api-v1'

urlpatterns = [
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),
    # path('tiken/login/',ObtainAuthToken.as_view(),name='token_login'),
    path('token/login/',views.CustomAuthToken.as_view(),name='token_login')




    
]