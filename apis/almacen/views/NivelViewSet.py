from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from ..models.Nivel import Nivel
from ..serializers.NivelSerializer import NivelSerializer

class NivelViewSet(ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

class ReporteNivelViewSet(ReadOnlyModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer
