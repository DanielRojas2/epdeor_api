from rest_framework import serializers
from ..models.EstanteNivel import EstanteNivel

class EstanteNivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstanteNivel
        fields = [
            'estante',
            'nivel',
            'estado'
        ]
