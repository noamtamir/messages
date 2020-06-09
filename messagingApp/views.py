from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Message
from .serializers import MessageSerializer
from .filters import MessageFilterSet


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filterset_class = MessageFilterSet

    def get_queryset(self):
        if self.request.user.is_staff:
            return Message.objects.all()
        else:
            return Message.objects.filter(Q(sender=self.request.user) | Q(receiver=self.request.user))

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)