from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Search_User

app_name = 'userpage'

urlpatterns = [
    path('',views.userHome,name='userHome'),
    path('post', views.post, name='post'),
    path('like_dislike', views.likePost, name='like_dislike_post'),
    path("<int:postId>", views.delPost, name='delPost'),
    path("<str:username>", views.userProfile, name='userProfile' ),
    path("user/follow/<str:username>", views.follow, name="follow"),
    path("search/", Search_User.as_view(), name="search_user"),
]