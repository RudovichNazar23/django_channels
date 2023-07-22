from django.urls import path
from .views import room_list, room, create_room

urlpatterns = [
    path("rooms", room_list, name="rooms"),
    path("<slug:slug>/", room, name="room"),
    path("create_room", create_room, name="create_room"),
]
