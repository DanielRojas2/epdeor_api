from rest_framework import serializers
from ..models.InventarioArchivos import InventarioArchivos
from ...archivos.models.Tomo import Tomo
from ...almacen.models.EstanteNivel import EstanteNivel

class InventarioArchivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioArchivos
        fields = [
            'tomo',
            'nivel_estante'
        ]

class TomoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tomo
        fields = [
            'nro_tomo',
            'titulo',
            'glosa',
            'nro_fojas_total',
            'fecha_apertura',
            'estado'
        ]
        read_only_fields = fields

class EstanteNivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstanteNivel
        fields = [
            'estante',
            'nivel',
            'estado'
        ]
        read_only_fields = fields

class ReporteInventarioArchviosSerializer(serializers.ModelSerializer):
    tomo = TomoSerializer(read_only=True)
    nivel_estante = EstanteNivelSerializer(read_only=True)
    class Meta:
        model = InventarioArchivos
        fields = [
            'tomo',
            'nivel_estante',
            'fecha_asignacion',
            'hora_asignacion',
            'estado'
        ]
        read_only_fields = fields
