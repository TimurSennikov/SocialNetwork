from django.urls import path
from .views import ShowAllPost

from post_app.views import PostCreateView

urlpatterns = [
    path(route= '', view= ShowAllPost.as_view(), name= 'home_view')
]