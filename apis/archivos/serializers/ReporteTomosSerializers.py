from rest_framework import serializers
from django.urls import reverse
from ..models.DetalleTomo import DetalleTomo
from ..models.Tomo import Tomo

class DetalleTomoReporteSerializer(serializers.ModelSerializer):
    qr_url = serializers.SerializerMethodField()

    class Meta:
        model = DetalleTomo
        fields = [
            'nro_archivo',
            'nombre_archivo',
            'archivo',
            'nro_fojas',
            'fecha_adjunto',
            'estado_archivo',
            'qr_url'
        ]
        read_only_fields = fields
    
    def get_qr_url(self, obj):
        request = self.context.get("request")
        if request and obj.archivo:
            return request.build_absolute_uri(
                reverse(
                    "tomos-reportes-generar-qr",
                    kwargs={
                        "pk": obj.tomo.pk,
                        "nombre_archivo": obj.nombre_archivo
                    }
                )
            )
        return None

class TomoConDetalleSerializer(serializers.ModelSerializer):
    detalles = DetalleTomoReporteSerializer(
        many=True, source='detalletomo_set', read_only=True
    )

    class Meta:
        model = Tomo
        fields = [
            'nro_tomo',
            'titulo',
            'glosa',
            'nro_fojas_total',
            'fecha_apertura',
            'estado',
            'gestion',
            'detalles',
        ]
        read_only_fields = fields
