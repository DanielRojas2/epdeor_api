from rest_framework import viewsets
from ..models.DetalleTomo import DetalleTomo
from ..serializers.DetalleTomoSerializer import DetalleTomoSerializer

class DetalleTomoViewSet(viewsets.ModelViewSet):
    queryset = DetalleTomo.objects.select_related("tomo").all().order_by("nro_archivo")
    serializer_class = DetalleTomoSerializer
