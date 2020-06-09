from django_filters import FilterSet, CharFilter, BooleanFilter
from django.db.models import Q
from .models import Message


class MessageFilterSet(FilterSet):
    user = CharFilter(method='filter_user')
    username = CharFilter(method='filter_username')
    read = BooleanFilter()

    def filter_user(self, queryset, name, value):
        return queryset.filter(Q(sender=value) | Q(receiver=value))

    def filter_username(self, queryset, name, value):
        return queryset.filter(Q(sender__username=value) | Q(receiver__username=value))


    class Meta:
        model = Message
        fields = ['user', 'username', 'read', 'sender', 'sender__username', 'receiver', 'receiver__username']