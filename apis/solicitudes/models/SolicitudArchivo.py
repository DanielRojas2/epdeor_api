from django.db import models
from ...inventario.models.InventarioArchivos import InventarioArchivos

class SolicitudArchivo(models.Model):
    fecha_solicitud = models.DateField(auto_now_add=True)
    hora_solicitud = models.TimeField(auto_now_add=True)
