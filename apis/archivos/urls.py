from rest_framework.routers import DefaultRouter
from .views.TomoViewSet import TomoViewSet
from .views.DetalleTomoViewSet import DetalleTomoViewSet
from .views.ReportesViewSet import (
    TomoConDetalleViewSet, DetalleTomoReporteViewSet
)

router = DefaultRouter()
router.register(r"tomos", TomoViewSet, basename="tomos")
router.register(r"tomos-reportes", TomoConDetalleViewSet, basename="tomos-reportes")
router.register(r"detalles", DetalleTomoViewSet, basename="detalles")
router.register(r"detalles-reportes", DetalleTomoReporteViewSet, basename="detalles-reportes")

urlpatterns = router.urls
