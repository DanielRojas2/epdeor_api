from django.db import models
from django.db.models import Q

class TomoQueryset(models.QuerySet):
    def filtrar(self, titulo=None, gestion=None, mes=None, glosa=None, fecha_apertura=None, estado=None):
        """Aplica filtros dinámicos al queryset según los parámetros recibidos.

        Args:
            titulo (str, busqueda parcial)
            gestion (date, busqueda por año)
            mes (date, busqueda por mes)
            glosa (str, busqueda parcial)
            fecha_apertura (date, busqueda por fecha)
            estado (str, busqueda por el estado del tomo)
        """
        qs = self

        if titulo:
            qs = qs.filter(titulo__icontains=titulo)
        if gestion:
            qs = qs.filter(fecha_apertura__year=gestion)
        if mes:
            qs = qs.filter(fecha_apertura__month=mes)
        if glosa:
            qs = qs.filter(glosa__icontains=glosa)
        if fecha_apertura:
            qs = qs.filter(fecha_apertura=fecha_apertura)
        if estado:
            qs = qs.filter(estado=estado)

        return qs

class TomoManager(models.Manager):
    def get_queryset(self):
        return TomoQueryset(self.model, using=self.db)
    
    def filtrar(self, **kwargs):
        return self.get_queryset().filtrar(**kwargs)
