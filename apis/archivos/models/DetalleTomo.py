from django.db import models
from ..functions.guardar_archivo import get_upload_to
from ..functions.validar_pdf import validar_pdf
from .Tomo import Tomo

class DetalleTomo(models.Model):
    ESTADO_CHOICES = (
        ('adjunto', 'adjunto'),
        ('no adjunto', 'no adjunto'),
    )

    nro_archivo = models.PositiveSmallIntegerField(blank=False, null=False)
    nombre_archivo = models.CharField(max_length=50, blank=False, null=False)
    archivo = models.FileField(
        blank=True, null=True,
        upload_to=get_upload_to,
        validators=[validar_pdf]
    )
    nro_fojas = models.PositiveSmallIntegerField(
        default=1, blank=False, null=False
    )
    fecha_adjunto = models.DateField(blank=True, null=True)
    estado_archivo = models.CharField(
        max_length=10,
        blank=False, null=False,
        choices=ESTADO_CHOICES,
        default='no adjunto'
    )
    tomo = models.ForeignKey(Tomo, on_delete=models.CASCADE)

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Detalle Tomo'
        verbose_name_plural = 'Detalles de Tomo'
        constraints = [
            models.UniqueConstraint(
                fields=['nro_archivo', 'tomo'],
                name='unique_archivo_tomo'
            )
        ]

    def save(self, *args, **kwargs):
        if self.archivo:
            self.estado_archivo = 'adjunto'
        else:
            self.estado_archivo = 'no adjunto'

        super(DetalleTomo, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nro_archivo}: {self.nombre_archivo} | {self.tomo}"
