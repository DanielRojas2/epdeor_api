from rest_framework.routers import DefaultRouter
from .views.DepartamentoViewSet import DepartamentoViewSet
from .views.UnidadViewSet import UnidadViewSet
from .views.PuestoViewSet import PuestoViewSet
from .views.PerfilUsuarioViewSet import (
    PerfilUsuarioViewSet, PerfilUsuarioReporteViewSet
)

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet, basename='departamentos')
router.register(r'unidades', UnidadViewSet, basename='unidades')
router.register(r'puestos', PuestoViewSet, basename='puestos')
router.register(r'perfiles-reporte', PerfilUsuarioReporteViewSet, basename='perfiles-reporte')
router.register(r'perfiles', PerfilUsuarioViewSet, basename='perfiles')

urlpatterns = router.urls