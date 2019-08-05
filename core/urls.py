from django.urls import path, include
from . import viewsets

urlpatterns = [
    path('event/', viewsets.EventListView.as_view()),
    path('speakers/', viewsets.SpeakerListView.as_view()),
    path('sessions/', viewsets.SessionListView.as_view()),
]