from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from ..models.EstanteNivel import EstanteNivel
from ..serializers.EstanteNivelSerializer import EstanteNivelSerializer

class EstanteNivelViewSet(ModelViewSet):
    queryset = EstanteNivel.objects.all()
    serializer_class = EstanteNivelSerializer

class ReporteEstanteNivelViewSet(ReadOnlyModelViewSet):
    queryset = EstanteNivel.objects.all()
    serializer_class = EstanteNivelSerializer
