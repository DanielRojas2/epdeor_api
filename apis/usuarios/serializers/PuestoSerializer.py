from rest_framework import serializers
from ..models.Puesto import Puesto
from .DepartamentoSerializer import DepartamentoSerializer
from .UnidadSerializer import UnidadSerializer

class PuestoSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer(read_only=True)
    unidad = UnidadSerializer(read_only=True)

    class Meta:
        model = Puesto
        fields = ['nro_item', 'departamento', 'unidad']
        read_only_fields = fields
