from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Room, Message


@login_required
def room_list(request):
    rooms = Room.objects.all()

    return render(request, "chat/rooms.html", {"rooms": rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[:11]

    return render(request, "chat/room.html", {"room": room, "messages": messages})


