from rest_framework.routers import DefaultRouter
from .views.AlmacenViewSet import AlmacenViewSet, ReporteAlmacenViewSet
from .views.EstanteViewSet import EstanteViewSet, ReporteEstanteViewSet
from .views.NivelViewSet import NivelViewSet, ReporteNivelViewSet
from .views.EstanteNivelViewSet import EstanteNivelViewSet, ReporteEstanteNivelViewSet

router = DefaultRouter()
router.register(r'almacen', AlmacenViewSet, basename='almacen')
router.register(r'reporte-almacen', ReporteAlmacenViewSet, basename='reporte-almacen')
router.register(r'estante', EstanteViewSet, basename='estante')
router.register(r'reporte-estante', ReporteEstanteViewSet, basename='reporte-estante')
router.register(r'nivel', NivelViewSet, basename='nivel')
router.register(r'reporte-nivel', ReporteNivelViewSet, basename='reporte-nivel')
router.register(r'estante-nivel', EstanteNivelViewSet, basename='estante-nivel')
router.register(r'reporte-estante-nivel', ReporteEstanteNivelViewSet, basename='reporte-estante-nivel')

urlpatterns = router.urls
