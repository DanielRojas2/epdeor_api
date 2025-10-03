from rest_framework.routers import DefaultRouter
from .views.InventarioArchivosViewSet import (
    InventarioArchivoViewSet, ReporteInventarioArchivosViewSet
)

router = DefaultRouter()
router.register(r'asignar-archivo', InventarioArchivoViewSet, basename='asignar-archivo')
router.register(r'reporte-inventario-archivos', ReporteInventarioArchivosViewSet, basename='reporte-inventario-archivos')

urlpatterns = router.urls
