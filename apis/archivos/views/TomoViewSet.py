from rest_framework import viewsets
from ..models.Tomo import Tomo
from ..serializers.TomoSerializer import TomoSerializer

class TomoViewSet(viewsets.ModelViewSet):
    queryset = Tomo.objects.all().order_by("fecha_apertura")
    serializer_class = TomoSerializer
