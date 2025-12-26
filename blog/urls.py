from . import views
from django.urls import path , include

app_name = 'blog'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index_view'),
    path('redirect/',views.RedirectViews.as_view(),name='redirect_view'),
    path('posts/',views.PostListView.as_view(),name='post_list'),
    path('post/<int:pk>/',views.PostDetail.as_view(),name='post_detail'),
    path('create/post/',views.CreatePost.as_view(),name='create_post'),
    path('update/<int:pk>/',views.UpdatePost.as_view(),name='update_post'),
    path('delete/<int:pk>/',views.DeletePost.as_view(),name='delete_post'),

    path('api/v1/',include('blog.api.v1.urls'))
]