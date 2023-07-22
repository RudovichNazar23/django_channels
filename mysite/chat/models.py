from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="room_creator")
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="room_member")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    message = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("date_created",)

