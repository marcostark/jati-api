from rest_framework.serializers import ModelSerializer
from convidados.models import Convidado

class ConvidadoSerializer(ModelSerializer):
    class Meta:
        model = Convidado
        fields = '__all__'