from rest_framework import serializers
from .models import Chat, Message
from django.contrib.auth.models import User


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['token']


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['tg_chat_id', 'token']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text', 'date']


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name']
