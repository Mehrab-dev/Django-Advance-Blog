from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index_view')
]