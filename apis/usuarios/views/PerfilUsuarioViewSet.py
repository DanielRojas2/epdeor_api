from django.utils import timezone
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
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

    @action(detail=True, methods=['patch'], url_path='actualizar-estado')
    def actualizar_estado(self, request, pk=None):
        perfil = self.get_object()
        estado = request.data.get('estado', None)

        if estado is None:
            return Response(
                {"error": "Estado de usuario inválido."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if isinstance(estado, str):
            estado = estado.lower() in ["true", "1", "t", "yes", "on"]
        else:
            estado = bool(estado)

        perfil.estado = estado
        perfil.baja = None if estado else timezone.now().date()
        perfil.save()

        return Response(
            {
                "mensaje": "Estado de usuario actualizado correctamente.",
                "perfil": {
                    "id": perfil.id,
                    "nombre": perfil.nombre,
                    "estado": perfil.estado,
                    "baja": perfil.baja,
                    "usuario": perfil.usuario.username if perfil.usuario else None,
                }
            },
            status=status.HTTP_200_OK
        )
