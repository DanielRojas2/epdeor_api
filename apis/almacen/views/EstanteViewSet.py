from rest_framework import viewsets
from ..models.Estante import Estante
from ..serializers.EstanteSerializer import EstanteSerializer

class EstanteViewSet(viewsets.ModelViewSet):
    queryset = Estante
    serializer_class = EstanteSerializer
    
class ReporteEstanteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Estante
    serializer_class = EstanteSerializer
