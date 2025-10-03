from django.db import models
from ...archivos.models.Tomo import Tomo
from ...almacen.models.EstanteNivel import EstanteNivel

class InventarioArchivos(models.Model):
    ESTADO_CHOICES = (
        ('prestado', 'prestado'),
        ('disponible', 'disponible')
    )
    tomo = models.ForeignKey(Tomo, on_delete=models.CASCADE)
    nivel_estante = models.ForeignKey(EstanteNivel, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(
        blank=False, null=False,
        auto_now_add=True
    )
    hora_asignacion = models.TimeField(
        blank=False, null=False,
        auto_now_add=True
    )
    estado = models.CharField(
        max_length=10,
        blank=False, null=False,
        choices=ESTADO_CHOICES,
        default='disponible'
    )
