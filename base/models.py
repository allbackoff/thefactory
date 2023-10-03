from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tg_chat_id = models.CharField(
        max_length=100, unique=True, blank=True, null=True)
    token = models.CharField(max_length=100, unique=True)


class Message(models.Model):
    user = models.ForeignKey(
        User, related_name="messages", on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
