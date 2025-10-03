from rest_framework import serializers
from django.contrib.auth.models import User
from ..models.PerfilUsuario import PerfilUsuario
from ..models.Puesto import Puesto

class PerfilUsuarioReporteSerializer(serializers.ModelSerializer):
    puesto = serializers.StringRelatedField(read_only=True)
    usuario = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PerfilUsuario
        fields = [
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'ci',
            'alta',
            'baja',
            'estado',
            'puesto',
            'usuario'
        ]
        read_only_fields = fields


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = [
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'ci',
            'alta',
            'baja',
            'puesto',
        ]
