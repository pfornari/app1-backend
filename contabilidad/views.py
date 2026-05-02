from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Cliente, Proveedor, CategoriaMovimiento, ConceptoMovimiento,
    Caja, MovimientoCaja, Venta, VentaAnimalDetalle, VentaCosechaDetalle,
    Compra, CompraAnimalDetalle, CompraCultivoDetalle
)
from .serializers import (
    ClienteSerializer, ProveedorSerializer,
    CategoriaMovimientoSerializer, ConceptoMovimientoSerializer,
    CajaSerializer, MovimientoCajaSerializer,
    VentaSerializer, VentaAnimalDetalleSerializer, VentaCosechaDetalleSerializer,
    CompraSerializer, CompraAnimalDetalleSerializer, CompraCultivoDetalleSerializer
)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.select_related('localidad').all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['localidad']
    search_fields = ['clie_nombre', 'cuit']
    ordering = ['clie_nombre']


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.select_related('localidad').all()
    serializer_class = ProveedorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['localidad']
    search_fields = ['prov_nombre', 'cuit']
    ordering = ['prov_nombre']


class CategoriaMovimientoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaMovimiento.objects.all()
    serializer_class = CategoriaMovimientoSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['camo_nombre']
    ordering = ['camo_nombre']


class ConceptoMovimientoViewSet(viewsets.ModelViewSet):
    queryset = ConceptoMovimiento.objects.select_related('categoria_movimiento').all()
    serializer_class = ConceptoMovimientoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['categoria_movimiento']
    search_fields = ['como_nombre', 'como_codigo']
    ordering = ['como_nombre']


class CajaViewSet(viewsets.ModelViewSet):
    queryset = Caja.objects.select_related('establecimiento').all()
    serializer_class = CajaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['establecimiento']
    ordering = ['-caja_fecha_inicio']


class MovimientoCajaViewSet(viewsets.ModelViewSet):
    queryset = MovimientoCaja.objects.select_related('caja', 'concepto', 'unidad').all()
    serializer_class = MovimientoCajaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['caja', 'moca_tipo']
    ordering = ['-moca_fecha']


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.select_related(
        'establecimiento', 'cliente'
    ).prefetch_related(
        'detalles_animal', 'detalles_cosecha'
    ).all()
    serializer_class = VentaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['establecimiento', 'cliente']
    ordering = ['-vent_fecha']


class VentaAnimalDetalleViewSet(viewsets.ModelViewSet):
    queryset = VentaAnimalDetalle.objects.select_related('venta', 'animal', 'unidad').all()
    serializer_class = VentaAnimalDetalleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['venta']


class VentaCosechaDetalleViewSet(viewsets.ModelViewSet):
    queryset = VentaCosechaDetalle.objects.select_related('venta', 'cultivo', 'unidad').all()
    serializer_class = VentaCosechaDetalleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['venta']


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.select_related(
        'establecimiento', 'proveedor'
    ).prefetch_related(
        'detalles_animal', 'detalles_cultivo'
    ).all()
    serializer_class = CompraSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['establecimiento', 'proveedor']
    ordering = ['-comp_fecha']


class CompraAnimalDetalleViewSet(viewsets.ModelViewSet):
    queryset = CompraAnimalDetalle.objects.select_related('compra', 'animal', 'unidad').all()
    serializer_class = CompraAnimalDetalleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['compra']


class CompraCultivoDetalleViewSet(viewsets.ModelViewSet):
    queryset = CompraCultivoDetalle.objects.select_related('compra', 'cultivo', 'unidad').all()
    serializer_class = CompraCultivoDetalleSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['compra']