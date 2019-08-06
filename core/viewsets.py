from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from . import models
from .pagination import CustomPagination


class EventListView(generics.ListAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = '__all__'
    #filter_fields = '__all__'
    search_fields = 'title'
    pagination_class = CustomPagination


class SpeakerListView(generics.ListAPIView):
    queryset = models.Speaker.objects.all()
    serializer_class = serializers.SpeakerSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = '__all__'
    #filter_fields = '__all__'
    search_fields = 'name'
    pagination_class = CustomPagination


class SessionListView(generics.ListAPIView):
    queryset = models.Session.objects.all()
    serializer_class = serializers.SessionSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = '__all__'
    #filter_fields = '__all__'
    search_fields = 'title'
    pagination_class = CustomPagination
