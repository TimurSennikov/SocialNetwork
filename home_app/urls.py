from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

from home_app.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name= "home_view")
]