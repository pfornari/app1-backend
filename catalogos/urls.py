from rest_framework.routers import DefaultRouter
from .views import (
    PaisViewSet, ProvinciaViewSet, LocalidadViewSet,
    EstadoViewSet, TipoUnidadViewSet, UnidadViewSet,
    ConversionUnidadViewSet
)

router = DefaultRouter()
router.register(r'paises', PaisViewSet, basename='pais')
router.register(r'provincias', ProvinciaViewSet, basename='provincia')
router.register(r'localidades', LocalidadViewSet, basename='localidad')
router.register(r'estados', EstadoViewSet, basename='estado')
router.register(r'tipos-unidad', TipoUnidadViewSet, basename='tipo-unidad')
router.register(r'unidades', UnidadViewSet, basename='unidad')
router.register(r'conversiones-unidad', ConversionUnidadViewSet, basename='conversion-unidad')

urlpatterns = router.urls