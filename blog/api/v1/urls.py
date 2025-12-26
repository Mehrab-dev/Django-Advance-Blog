from django.urls import path
from blog.api.v1 import views

app_name = 'api-v1'

urlpatterns = [
    # function base
    path('posts/',views.Post_List_Api_View,name='post_list_fbv'),

]