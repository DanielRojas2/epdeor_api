from django.db import models
from django.core.validators import RegexValidator
from .Estante import Estante
from .Nivel import Nivel

class EstanteNivel(models.Model):
    ESTADO_CHOICES = (
        ('hay espacio', 'hay espacio'),
        ('ocupado', 'ocupado'),
    )
    estante = models.ForeignKey(Estante, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    estado = models.CharField(
        max_length=11,
        blank=False, null=False,
        choices=ESTADO_CHOICES,
        validators=[
            RegexValidator(
                regex='^(hay espacio|ocupado)$',
                message='Estado de nivel de estante inválido'
            )
        ]
    )
    
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Nivel de Estante'
        verbose_name_plural = 'Niveles de Estante'
        constraints = [
            models.UniqueConstraint(
                fields=['estante', 'nivel'],
                name='unique_estante_nivel'
            )
        ]
        
    def __str__(self):
        return f"Estante {self.estante}, Nivel {self.nivel}. Estado: {self.estado}"
