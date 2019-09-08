from rest_framework.viewsets import ModelViewSet
from core.models import Event
from .serializers import EventSerializer

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer