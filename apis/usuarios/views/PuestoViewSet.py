from rest_framework import viewsets
from ..models.Puesto import Puesto
from ..serializers.PuestoSerializer import PuestoSerializer

class PuestoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Puesto.objects.select_related("departamento", "unidad").all()
    serializer_class = PuestoSerializer
