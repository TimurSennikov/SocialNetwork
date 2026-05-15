from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.urls import path
from .views import PostListView, PostCreateView, PostCreateView

urlpatterns = [
    path(route= '', view= PostListView.as_view(), name= 'my_posts'),
    path(route= 'post/', view=PostCreateView.as_view(), name='post_create')
]