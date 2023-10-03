from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views


urlpatterns = [
    path('register/', views.Register.as_view()),
    path('api-token-auth/', token_views.obtain_auth_token),
    path('generate-token/', views.GenerateToken.as_view()),
    path('connect/<str:token>', views.ConnectChat.as_view()),
    path('messages/', views.MessageList.as_view()),
]
