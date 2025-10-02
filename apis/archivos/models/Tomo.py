from django.db import models
from django.core.validators import RegexValidator
from ..managers.TomoManager import TomoManager

class Tomo(models.Model):
    ESTADO_CHOICES = (
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado')
    )

    nro_tomo = models.SmallIntegerField(blank=False, null=False)
    titulo = models.CharField(max_length=25, blank=False, null=False)
    glosa = models.TextField()
    nro_fojas_total = models.SmallIntegerField(blank=True, null=True)
    fecha_apertura = models.DateField()
    estado = models.CharField(
        max_length=7,
        blank=False, null=False,
        choices=ESTADO_CHOICES,
        validators=[
            RegexValidator(
                regex='^(abierto|cerrado)$',
                message='Estado de Tomo inválido.'
            )
        ]
    )

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    objects = TomoManager()

    class Meta:
        verbose_name = 'Tomo'
        verbose_name_plural = 'Tomos'
        constraints = [
            models.UniqueConstraint(
                fields=['nro_tomo', 'fecha_apertura'],
                name='unique_tomo_fecha_apertura'
            )
        ]

    def __str__(self):
        return f"{self.nro_tomo} - {self.titulo}: {self.glosa}"
    
    @property
    def gestion(self):
        return self.fecha_apertura.year
    
    @property
    def mes_nombre(self):
        return self.fecha_apertura.strftime("%b").capitalize()
