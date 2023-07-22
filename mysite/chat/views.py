from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateRoomForm

from .models import Room, Message


@login_required
def room_list(request):
    rooms = Room.objects.filter(creator=request.user)
    if not rooms:
        rooms = Room.objects.filter(member=request.user)

    return render(request, "chat/rooms.html", {"rooms": rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[:11]

    return render(request, "chat/room.html", {"room": room, "messages": messages})


@login_required
def create_room(request):
    if request.method == "POST":
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            member = form.cleaned_data.get("member")
            slug = form.cleaned_data.get("slug")
            room_object = Room.objects.create(name=name, creator=request.user, member=member, slug=slug)
            return redirect("/")
    return render(request, "chat/create_room.html", {"form": CreateRoomForm()})


