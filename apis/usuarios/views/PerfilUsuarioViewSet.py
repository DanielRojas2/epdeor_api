from rest_framework import viewsets
from ..models.PerfilUsuario import PerfilUsuario

from ..serializers.PerfilUsuarioSerializer import (
    PerfilUsuarioSerializer, PerfilUsuarioReporteSerializer
)

class PerfilUsuarioReporteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PerfilUsuario.objects.select_related("puesto", "usuario").all()
    serializer_class = PerfilUsuarioReporteSerializer

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
