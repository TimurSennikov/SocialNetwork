
from django.urls import path

from django.conf import settings
from .views import (
    FriendProfile,
    FriendsView, 
    FriendActionView, 
    FriendsSectionView
)


urlpatterns = [
    path(route= '', view= FriendsView.as_view(), name= 'friends_view'),
    path(route= 'profile/<int:user_id>/', view= FriendProfile.as_view(), name= 'profile_view'),
    path("<str:section>/", FriendsSectionView.as_view(), name="friends_section"),  # Віддаємо вкладку друзів через fetch.
    path("action/<int:user_id>/<str:action>/", FriendActionView.as_view(), name="friend_action"),  # Обробляємо дії з картками друзів.
]