from .models import Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.id')
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'subject', 'message', 'read', 'created']
