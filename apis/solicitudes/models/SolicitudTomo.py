from django.db import models
from django.core.validators import RegexValidator
from ...inventario.models.InventarioArchivos import InventarioArchivos
from ...usuarios.models.PerfilUsuario import PerfilUsuario

class SolicitudTomo(models.Model):
    TIPO_SOLICITUD_CHOICES = (
        ('digital', 'Digital'),
        ('fisico', 'fisico'),
    )
    ESTADO_SOLICITUD_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada')
    )
    
    fecha_solicitud = models.DateField(auto_now_add=True)
    hora_solicitud = models.TimeField(auto_now_add=True)
    tipo_solicitud = models.CharField(
        max_length=7, blank=False, null=False,
        validators=[
            RegexValidator(
                regex='^(digital|fisico)',
                message='Formato de solicitud no válido'
            )
        ]
    )
    estado_solicitud = models.CharField(
        max_length=9, blank=False,
        null=False, default='pendiente',
        validators=[
            RegexValidator(
                regex='^(pendiente|aprobada|rechazada)',
                message='Estado de solicitud no válida.'
            )
        ]
    )
    observacion = models.TextField(blank=True, null=True)
    solicitante = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    detalle_solicitud = models.ForeignKey(
        InventarioArchivos, on_delete=models.CASCADE
    )
    
    class Meta:
        verbose_name = 'Solicitud de Tomo'
        verbose_name_plural = 'Solicitudes de Tomos'
    
    def __str__(self):
        return f"{self.detalle_solicitud} - {self.solicitante}: {self.fecha_solicitud} / {self.hora_solicitud}"
        
