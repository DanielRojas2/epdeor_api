from rest_framework import serializers
from ...inventario.models.InventarioArchivos import InventarioArchivos
from ...usuarios.models.PerfilUsuario import PerfilUsuario
from ..models.SolicitudTomo import SolicitudTomo

class SolicitudTomoSerializer(serializers.ModelSerializer):
    solicitante = serializers.PrimaryKeyRelatedField(
        queryset=PerfilUsuario.objects.all()
    )
    detalle_solicitud = serializers.PrimaryKeyRelatedField(
        queryset=InventarioArchivos.objects.all()
    )

    class Meta:
        model = SolicitudTomo
        fields = [
            'id',
            'fecha_solicitud',
            'hora_solicitud',
            'tipo_solicitud',
            'estado_solicitud',
            'observacion',
            'solicitante',
            'detalle_solicitud'
        ]
        read_only_fields = ['fecha_solicitud', 'hora_solicitud', 'estado_solicitud']

    def validate(self, data):
        detalle = data.get('detalle_solicitud')
        if detalle.estado == 'prestado' and data.get('tipo_solicitud') == 'fisico':
            raise serializers.ValidationError("El tomo solicitado no está disponible.")
        return data
