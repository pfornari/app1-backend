from rest_framework.routers import DefaultRouter
from .views import (
    ClienteViewSet, ProveedorViewSet,
    CategoriaMovimientoViewSet, ConceptoMovimientoViewSet,
    CajaViewSet, MovimientoCajaViewSet,
    VentaViewSet, VentaAnimalDetalleViewSet, VentaCosechaDetalleViewSet,
    CompraViewSet, CompraAnimalDetalleViewSet, CompraCultivoDetalleViewSet
)

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'proveedores', ProveedorViewSet, basename='proveedor')
router.register(r'categorias-movimiento', CategoriaMovimientoViewSet, basename='categoria-movimiento')
router.register(r'conceptos-movimiento', ConceptoMovimientoViewSet, basename='concepto-movimiento')
router.register(r'cajas', CajaViewSet, basename='caja')
router.register(r'movimientos-caja', MovimientoCajaViewSet, basename='movimiento-caja')
router.register(r'ventas', VentaViewSet, basename='venta')
router.register(r'ventas-animal-detalle', VentaAnimalDetalleViewSet, basename='venta-animal-detalle')
router.register(r'ventas-cosecha-detalle', VentaCosechaDetalleViewSet, basename='venta-cosecha-detalle')
router.register(r'compras', CompraViewSet, basename='compra')
router.register(r'compras-animal-detalle', CompraAnimalDetalleViewSet, basename='compra-animal-detalle')
router.register(r'compras-cultivo-detalle', CompraCultivoDetalleViewSet, basename='compra-cultivo-detalle')

urlpatterns = router.urls