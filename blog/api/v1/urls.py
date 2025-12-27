from django.urls import path
from blog.api.v1 import views

app_name = 'api-v1'

urlpatterns = [
    # function base
    # path('posts/',views.Post_List_Api_View,name='post_list_fbv'),
    # path('post/<int:pk>/',views.post_detail_api,name='post_detail'),


    # class base
    path('posts/',views.PostList.as_view(),name='post_list'),
    path('post/<int:pk>/',views.PostDetail.as_view(),name='post_detail')


]