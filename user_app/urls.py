from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

from user_app.views import UserView

urlpatterns = [
    path("", UserView.as_view(), name= "user_view")
]