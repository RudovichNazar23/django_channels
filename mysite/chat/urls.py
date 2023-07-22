from django.urls import path
from .views import room_list, room

urlpatterns = [
    path("rooms", room_list, name="rooms"),
    path("<slug:slug>/", room, name="room"),
]
