from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

from post_app.views import PostView

urlpatterns = [
    path("", PostView.as_view(), name= "post_view"),
]