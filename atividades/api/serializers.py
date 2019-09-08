from rest_framework.serializers import ModelSerializer
from atividades.models import Atividade

class AtividadeSerializer(ModelSerializer):
    class Meta:
        model = Atividade
        fields = '__all__' 