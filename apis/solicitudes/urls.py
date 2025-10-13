from rest_framework.routers import DefaultRouter
from .views.SolicitudTomoViewSet import SolicitudTomoViewSet

router = DefaultRouter()
router.register(r'solicitud-archivos', SolicitudTomoViewSet, basename='solitud-archivos')

urlpatterns = router.urls
