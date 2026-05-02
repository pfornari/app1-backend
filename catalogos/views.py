from rest_framework import viewsets, permissions
from .models import Pais, Provincia, Localidad, Estado, TipoUnidad, Unidad, ConversionUnidad
from .serializers import (
    PaisSerializer, ProvinciaSerializer, LocalidadSerializer,
    EstadoSerializer, TipoUnidadSerializer, UnidadSerializer,
    ConversionUnidadSerializer
)


class PaisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    permission_classes = [permissions.AllowAny]


class ProvinciaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Provincia.objects.select_related('pais').all()
    serializer_class = ProvinciaSerializer
    filterset_fields = ['pais']
    permission_classes = [permissions.AllowAny]


class LocalidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Localidad.objects.select_related('provincia').all()
    serializer_class = LocalidadSerializer
    filterset_fields = ['provincia']
    search_fields = ['loca_nombre']
    permission_classes = [permissions.AllowAny]


class EstadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    filterset_fields = ['esta_uso']
    permission_classes = [permissions.AllowAny]


class TipoUnidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoUnidad.objects.all()
    serializer_class = TipoUnidadSerializer
    permission_classes = [permissions.AllowAny]


class UnidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Unidad.objects.select_related('tipo_unidad').all()
    serializer_class = UnidadSerializer
    filterset_fields = ['tipo_unidad']
    permission_classes = [permissions.AllowAny]


class ConversionUnidadViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConversionUnidad.objects.all()
    serializer_class = ConversionUnidadSerializer
    permission_classes = [permissions.AllowAny]