from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from . import models


class EventListView(generics.ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = '__all__'
    filter_fields = '__all__'
    search_fields = 'title'


class SpeakerListView(generics.ListAPIView):
    queryset = models.Speaker.objects.all()
    serializer_class = serializers.SpeakerSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = '__all__'
    filter_fields = '__all__'
    search_fields = 'name'


class SessionListView(generics.ListAPIView):
    queryset = models.Session.objects.all()
    serializer_class = serializers.SessionSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = '__all__'
    filter_fields = '__all__'
    search_fields = 'title'