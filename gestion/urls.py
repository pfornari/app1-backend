from rest_framework.routers import DefaultRouter
from .views import (
    EstablecimientoViewSet, TamboViewSet, CampoViewSet,
    CultivoViewSet, SiembraViewSet, RazaViewSet,
    CategoriaViewSet, AnimalViewSet, CampoAnimalViewSet,
    HistorialEstadoAnimalViewSet, PesajeViewSet,
    ProduccionDiariaAnimalViewSet, ProduccionDiariaTamboViewSet,
    ReproduccionViewSet
)

router = DefaultRouter()
router.register(r'establecimientos', EstablecimientoViewSet, basename='establecimiento')
router.register(r'tambos', TamboViewSet, basename='tambo')
router.register(r'campos', CampoViewSet, basename='campo')
router.register(r'cultivos', CultivoViewSet, basename='cultivo')
router.register(r'siembras', SiembraViewSet, basename='siembra')
router.register(r'razas', RazaViewSet, basename='raza')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'animales', AnimalViewSet, basename='animal')
router.register(r'campo-animal', CampoAnimalViewSet, basename='campo-animal')
router.register(r'historial-estados', HistorialEstadoAnimalViewSet, basename='historial-estado')
router.register(r'pesajes', PesajeViewSet, basename='pesaje')
router.register(r'produccion-animal', ProduccionDiariaAnimalViewSet, basename='produccion-animal')
router.register(r'produccion-tambo', ProduccionDiariaTamboViewSet, basename='produccion-tambo')
router.register(r'reproducciones', ReproduccionViewSet, basename='reproduccion')

urlpatterns = router.urls