# Django Build in User Model
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from messaging.models import Message
from .serializers import UserSerializer, MessageSerializer

from rest_framework.mixins import ListModelMixin, DestroyModelMixin, CreateModelMixin


class RecievedListAPIView(ListAPIView):
    """API View that lists all messages recieved by the current user for Inbox"""

    serializer_class = MessageSerializer
#     # permission_classes = [IsAccountAdminOrReadOnly]

    def get_queryset(self):
        """return current user messages"""
        user = self.request.user
        queryset = Message.objects.filter(recipient=user)
        return queryset


class SentListAPIView(ListAPIView):
    """API View that lists all messages sent by the current user for Sentbox"""
    serializer_class = MessageSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]

    def get_queryset(self):
        """return current user messages that have been sent"""
        user = self.request.user
        queryset = Message.objects.filter(sender=user)
        return queryset


class ComposeAPIView(CreateAPIView):
    """Compose a message; POST to database"""
    serializer_class = MessageSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(sender=self.request.user)


class ReadMessageAPIView(RetrieveUpdateDestroyAPIView):
    """Retrieves a specific instance by pk in url; gives available methods 
    PUT, PATCH, DELETE"""
    serializer_class = MessageSerializer
    # permission_classes
    lookup_url_kwarg = 'pk'
    queryset = Message.objects.all()


class UsersListAPIView(ListAPIView):
    """API View that lists all users available to message"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
#     # permission_classes = [IsAccountAdminOrReadOnly]
