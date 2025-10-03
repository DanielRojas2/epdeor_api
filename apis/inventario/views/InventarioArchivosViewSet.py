from rest_framework import viewsets
from ..models.InventarioArchivos import InventarioArchivos
from ..serializers.InventarioArchivosSerializer import (
    InventarioArchivosSerializer, ReporteInventarioArchviosSerializer
)

class InventarioArchivoViewSet(viewsets.ModelViewSet):
    queryset = InventarioArchivos.objects.all()
    serializer_class = InventarioArchivosSerializer
    
class ReporteInventarioArchivosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InventarioArchivos.objects.all()
    serializer_class = ReporteInventarioArchviosSerializer
