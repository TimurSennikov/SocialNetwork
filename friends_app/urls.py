from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

from friends_app.views import FriendsView

urlpatterns = [
    path("", FriendsView.as_view(), name= "friends_view")
]