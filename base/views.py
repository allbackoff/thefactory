import random
import string
import requests

from rest_framework import generics, mixins, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password


from django.conf import settings

from .models import Chat, Message, User
from .serializers import ChatSerializer, MessageSerializer, TokenSerializer, UserSerializer


class Register(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(self.request.data['password']))


class GenerateToken(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        chat = Chat.objects.filter(user=request.user).first()
        status_ = status.HTTP_200_OK if chat else status.HTTP_201_CREATED
        serializer = TokenSerializer(chat, data={
            'token': self.generate_token()
        })
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status_)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def generate_token(self):
        return ''.join(random.SystemRandom().choice(
            string.ascii_uppercase + string.digits) for _ in range(20))


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        message = f"{self.request.user.first_name}, я получил от тебя сообщение:\n{self.request.data['text']}"
        req = requests.post(
            f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage", data={
                'chat_id': self.request.user.chat.tg_chat_id,
                'text': message
            })
        if req.status_code == requests.codes.ok:
            serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(user=user)


class ConnectChat(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    lookup_field = 'token'

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
