from rest_framework import serializers
from ..models.DetalleTomo import DetalleTomo

class DetalleTomoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleTomo
        fields = [
            'nro_archivo',
            'nombre_archivo',
            'archivo',
            'nro_fojas',
            'fecha_adjunto',
            'tomo'
        ]
