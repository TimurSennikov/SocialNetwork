"""
URL configuration for SocialNetwork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_app.urls'), name= 'user_views'),
    path('friends/', include('friends_app.urls'), name= 'friends_views'),
    path('post/', include('post_app.urls'), name= 'post_views'),
    path("chat/", include("chat_app.urls"), name= "chat_views"),
    path(route= '', view= include('home_app.urls')),
    path(route= 'auth/', view= include('user_app.urls')),
]

if settings.DEBUG:
    """
    STATIC for urlpatterns all project
    """
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)