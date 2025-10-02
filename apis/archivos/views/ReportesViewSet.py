from django.http import HttpResponse
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models.Tomo import Tomo
from ..models.DetalleTomo import DetalleTomo
from ..serializers.ReporteTomosSerializers import (
    TomoConDetalleSerializer, DetalleTomoReporteSerializer
)

class TomoConDetalleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tomo.objects.all().prefetch_related("detalletomo_set").order_by("fecha_apertura")
    serializer_class = TomoConDetalleSerializer

    @action(detail=True, methods=["get"], url_path="qr/(?P<nombre_archivo>[^/.]+)", url_name="generar-qr")
    def generar_qr(self, request, pk=None, nombre_archivo=None):
        """
        Genera un QR para descargar un archivo específico de un tomo.
        """
        try:
            tomo = self.get_object()
            detalle = DetalleTomo.objects.get(
                tomo=tomo, nombre_archivo__iexact=nombre_archivo
            )

            if not detalle.archivo:
                return Response(
                    {"error": "El archivo no tiene documento adjunto."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            archivo_url = request.build_absolute_uri(detalle.archivo.url)

            qr = qrcode.make(archivo_url)
            buffer = io.BytesIO()
            qr.save(buffer, format="PNG")
            buffer.seek(0)

            return HttpResponse(buffer, content_type="image/png")

        except DetalleTomo.DoesNotExist:
            return Response(
                {"error": "Archivo no encontrado en este tomo."},
                status=status.HTTP_404_NOT_FOUND,
            )

class DetalleTomoReporteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DetalleTomo.objects.select_related("tomo").all().order_by('nro_archivo')
    serializer_class = DetalleTomoReporteSerializer
