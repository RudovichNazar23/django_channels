import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from .models import Message


class ChatConsumer(WebsocketConsumer):

    def fetch_messages(self, data):
        author = User.objects.get(username=data["from"])
        author_messages = Message.objects.get(author=author)
        messages = author_messages.last_messages()
        content = {
            "messages": self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        author = data["from"]
        author_user = User.objects.filter(username=author)[0]
        message = Message.objects.create(
            author=author_user,
            message=data["message"]
            )
        content = {
            "command": "new_message",
            "message": self.message_to_json(message)
        }
        return self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []

        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            "author": message.author,
            "message": message.message,
            "date_created": message.date_created
        }

    commands = {
        "fetch_messages": fetch_messages,
        "new_message": new_message
    }

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        self.commands[data["command"]](self, data)

    def send_chat_message(self, message):

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps(message))

