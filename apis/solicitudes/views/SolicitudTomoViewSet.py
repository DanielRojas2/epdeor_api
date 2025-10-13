from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.SolicitudTomo import SolicitudTomo
from ..serializers.SolicitudTomoSerializer import SolicitudTomoSerializer
from ...inventario.models.InventarioArchivos import InventarioArchivos

class SolicitudTomoViewSet(viewsets.ModelViewSet):
    queryset = SolicitudTomo.objects.all().select_related('solicitante', 'detalle_solicitud')
    serializer_class = SolicitudTomoSerializer

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return SolicitudTomo.objects.none()

        if user.groups.filter(name="Encargado de archivos").exists():
            return self.queryset

        perfil = getattr(user, 'perfilusuario', None)
        if perfil:
            return self.queryset.filter(solicitante=perfil)

        return SolicitudTomo.objects.none()

    def perform_create(self, serializer):
        perfil = getattr(self.request.user, 'perfilusuario', None)
        if not perfil:
            raise PermissionError("No se puede crear la solicitud sin perfil asociado.")
        serializer.save(solicitante=perfil)

    @action(detail=True, methods=['post'])
    def aprobar(self, request, pk=None):
        user = request.user
        if not user.groups.filter(name="Encargado de archivos").exists():
            return Response(
                {"detail": "No tienes permiso para aprobar solicitudes."},
                status=status.HTTP_403_FORBIDDEN
            )

        solicitud = self.get_object()
        solicitud.estado_solicitud = 'aprobada'
        solicitud.observacion = request.data.get('observacion', '')

        if solicitud.tipo_solicitud == 'fisico':
            solicitud.detalle_solicitud.estado = 'prestado'
            solicitud.detalle_solicitud.save()

        solicitud.save()
        return Response({'detail': 'Solicitud aprobada correctamente.'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def rechazar(self, request, pk=None):
        user = request.user
        if not user.groups.filter(name="Encargado de archivos").exists():
            return Response(
                {"detail": "No tienes permiso para rechazar solicitudes."},
                status=status.HTTP_403_FORBIDDEN
            )

        solicitud = self.get_object()
        solicitud.estado_solicitud = 'rechazada'
        solicitud.observacion = request.data.get('observacion', '')
        solicitud.save()
        return Response({'detail': 'Solicitud rechazada correctamente.'}, status=status.HTTP_200_OK)
