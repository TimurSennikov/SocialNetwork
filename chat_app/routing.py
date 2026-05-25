"""
    Файл для налаштування маршрутизації WebSocket-з`єднань.
    Цей файл є аналогом urls.py і працює в асинхронному режимі. 
    В цьому файлі ми створюємо url-адреси для WebSocket-з`єднань.
"""
from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path(route='chatwebsocket/', view= ChatConsumer.as_asgi()),
    path("chatwebsocket/<int:room_id>/", ChatConsumer.as_asgi()),
]

