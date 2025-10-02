from rest_framework import serializers
from ..models.Almacen import Almacen

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = [
            'descripcion',
            'ubicacion',
            'tipo_almacen'
        ]
