from rest_framework import serializers
from ..models.Unidad import Unidad

class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = ['unidad']
        read_only_fields = fields
        