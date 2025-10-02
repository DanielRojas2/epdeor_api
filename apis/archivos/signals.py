from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models.Tomo import Tomo
from .models.DetalleTomo import DetalleTomo

def actualizar_nro_fojas_total(tomo):
    total = tomo.detalletomo_set.aggregate(total=Sum('nro_fojas'))['total'] or 0
    tomo.nro_fojas_total = total
    tomo.save(update_fields=['nro_fojas_total'])

@receiver(post_save, sender=DetalleTomo)
def actualizar_fojas_post_save(sender, instance, **kwargs):
    actualizar_nro_fojas_total(instance.tomo)

@receiver(post_delete, sender=DetalleTomo)
def actualizar_fojas_post_delete(sender, instance, **kwargs):
    actualizar_nro_fojas_total(instance.tomo)
