from django.urls import path
from blog.api.v1 import views

app_name = 'api-v1'

urlpatterns = [
    # function base
    # path('posts/',views.Post_List_Api_View,name='post_list_fbv'),
    # path('post/<int:pk>/',views.post_detail_api,name='post_detail'),


    # class base
    # path('posts/',views.PostList.as_view(),name='post_list'),
    # path('post/<int:pk>/',views.PostDetail.as_view(),name='post_detail'),

    # viewset
    # path('posts/',views.PostViewSet.as_view({'get':'list','post':'create'}),name='post_list_viewset'),
    # path('post/<int:pk>/',views.PostViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='post_detail_viewset'),

    path('posts/',views.PostModelViewSet.as_view({'get':'list','post':'create'},name='post_list_modelviewset')),
    path('post/<int:pk>/',views.PostModelViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}))


]