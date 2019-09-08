from rest_framework.serializers import ModelSerializer
from core.models import Event

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'