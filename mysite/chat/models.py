from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author

    def last_messages(self):
        return Message.objects.order_by("-date_created").all()[:10]
