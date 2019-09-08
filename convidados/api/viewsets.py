from rest_framework.viewsets import ModelViewSet
from convidados.models import Convidado
from .serializers import ConvidadoSerializer

class ConvidadoViewSet(ModelViewSet):
    queryset = Convidado.objects.all()
    serializer_class = ConvidadoSerializer