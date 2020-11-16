from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'userpage'

urlpatterns = [
    path('',views.userHome,name='userHome'),
    path('post', views.post, name='post'),
    path("<str:username>", views.userProfile, name='userProfile' ),
]