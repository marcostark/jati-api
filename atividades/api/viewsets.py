from rest_framework.viewsets import ModelViewSet
from atividades.models import Atividade
from .serializers import AtividadeSerializer

class AtividadeViewSet(ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer