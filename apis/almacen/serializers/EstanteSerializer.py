from rest_framework import serializers
from ..models.Estante import Estante

class EstanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estante
        fields = [
            'nro_estante',
            'almacen'
        ]
