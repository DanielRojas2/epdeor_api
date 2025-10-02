from rest_framework import serializers
from ..models.Tomo import Tomo

class TomoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tomo
        fields = [
            'nro_tomo',
            'titulo',
            'glosa',
            'fecha_apertura',
            'estado'
        ]
