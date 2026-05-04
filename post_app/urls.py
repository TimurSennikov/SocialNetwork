from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.urls import path
from .views import MyPostsView

urlpatterns = [
    path(route= '', view= MyPostsView.as_view(), name= 'my_posts'),
]