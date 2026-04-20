from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

from user_app.views import AuthTemplateView , UserView

urlpatterns = [
    path(route= '', view= AuthTemplateView.as_view(), name= 'auth'),
    path(route= 'register/', view= AuthTemplateView.as_view(), name= 'register'),
    path(route= 'login/', view= AuthTemplateView.as_view(), name= 'login'),
    path(route= 'confirm-email/', view= AuthTemplateView.as_view(), name= 'confirm-email'),
    path(route= 'profile/', view= UserView.as_view(), name= 'profile')
]

