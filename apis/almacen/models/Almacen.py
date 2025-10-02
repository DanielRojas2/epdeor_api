from django.db import models
from django.core.validators import RegexValidator

class Almacen(models.Model):
    TIPO_ALMACEN_CHOICES = (
        ('material', 'Material'),
        ('archivos', 'Archivos'),
    )
    
    descripcion = models.TextField()
    ubicacion = models.CharField(
        max_length=50, blank=False, null=False
    )
    tipo_almacen = models.CharField(
        max_length=8,
        blank=False, null=False,
        choices=TIPO_ALMACEN_CHOICES,
        validators=[
            RegexValidator(
                regex='^(material|archivos)$',
                message='Tipo de almacen no válido.'
            )
        ]
    )
    
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'
        
    def __str__(self):
        return f"{self.id} - {self.tipo_almacen}: {self.ubicacion}"
