from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.DepartamentoViewSet import DepartamentoViewSet
from .views.UnidadViewSet import UnidadViewSet
from .views.PuestoViewSet import PuestoViewSet
from .views.PerfilUsuarioViewSet import (
    PerfilUsuarioViewSet, PerfilUsuarioReporteViewSet
)
from .views.AuthViews import (
    IniciarSesionView, CerrarSesionView
)

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet, basename='departamentos')
router.register(r'unidades', UnidadViewSet, basename='unidades')
router.register(r'puestos', PuestoViewSet, basename='puestos')
router.register(r'perfiles-reporte', PerfilUsuarioReporteViewSet, basename='perfiles-reporte')
router.register(r'perfiles', PerfilUsuarioViewSet, basename='perfiles')

urlpatterns = [
    path('iniciar-sesion/', IniciarSesionView.as_view(), name='inciar-sesion'),
    path('cerrar-sesion/', CerrarSesionView.as_view(), name='cerrar-sesion'),
]

urlpatterns += router.urls
