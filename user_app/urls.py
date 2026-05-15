from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

# from user_app.views import AuthTemplateView , UserView

# urlpatterns = [
#     path(route= '', view= AuthTemplateView.as_view(), name= 'auth'),
#     path(route= 'register/', view= AuthTemplateView.as_view(), name= 'register'),
#     path(route= 'login/', view= AuthTemplateView.as_view(), name= 'login'),
#     path(route= 'confirm-email/', view= AuthTemplateView.as_view(), name= 'confirm-email'),
#     path(route= 'profile/', view= UserView.as_view(), name= 'profile')
# ]

from django.urls import path, include
from .views import AuthTemplateView, RegisterView, LoginView, ActivateAccountView, LogoutView

urlpatterns = [
    path(route= '', view= AuthTemplateView.as_view(), name= 'auth'),
    path(route= 'register/', view= RegisterView.as_view(), name= 'register'),
    path(route= 'login/', view= LoginView.as_view(), name= 'login'),
    path(route='logout/', view= LogoutView.as_view(), name='logout'),
    path(route= 'confirm/', view= ActivateAccountView.as_view(), name='activate')
]