from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Establecimiento, Tambo, Campo, Cultivo, Siembra,
    Raza, Categoria, Animal, CampoAnimal, HistorialEstadoAnimal,
    Pesaje, ProduccionDiariaAnimal, ProduccionDiariaTambo, Reproduccion
)
from .serializers import (
    EstablecimientoSerializer, TamboSerializer, CampoSerializer,
    CultivoSerializer, SiembraSerializer, RazaSerializer,
    CategoriaSerializer, AnimalSerializer, AnimalListSerializer,
    CampoAnimalSerializer, HistorialEstadoAnimalSerializer,
    PesajeSerializer, ProduccionDiariaAnimalSerializer,
    ProduccionDiariaTamboSerializer, ReproduccionSerializer
)


class EstablecimientoViewSet(viewsets.ModelViewSet):
    queryset = Establecimiento.objects.select_related('localidad').all()
    serializer_class = EstablecimientoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['localidad']
    search_fields = ['estb_nombre', 'cuit']
    ordering_fields = ['estb_nombre', 'fecha_alta']
    ordering = ['estb_nombre']


class TamboViewSet(viewsets.ModelViewSet):
    queryset = Tambo.objects.select_related('establecimiento', 'localidad').all()
    serializer_class = TamboSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['establecimiento']
    search_fields = ['tamb_nombre']
    ordering = ['tamb_nombre']


class CampoViewSet(viewsets.ModelViewSet):
    queryset = Campo.objects.select_related('establecimiento', 'localidad').all()
    serializer_class = CampoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['establecimiento']
    search_fields = ['camp_nombre']
    ordering = ['camp_nombre']


class CultivoViewSet(viewsets.ModelViewSet):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['cult_nombre']
    ordering = ['cult_nombre']


class SiembraViewSet(viewsets.ModelViewSet):
    queryset = Siembra.objects.select_related('campo', 'cultivo', 'unidad').all()
    serializer_class = SiembraSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['campo', 'cultivo']
    ordering = ['-siem_fecha_siembra']


class RazaViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['raza_nombre']
    ordering = ['raza_nombre']


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['cate_nombre']
    ordering = ['cate_nombre']


class ReproduccionViewSet(viewsets.ModelViewSet):
    queryset = Reproduccion.objects.all()
    serializer_class = ReproduccionSerializer
    filter_backends = [OrderingFilter]
    ordering = ['-repr_fecha_servicio']


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.select_related(
        'raza', 'categoria',
        'estado_reproductivo', 'estado_productivo',
        'madre', 'padre',
    ).all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['anim_sexo', 'raza', 'categoria', 'estado_reproductivo', 'estado_productivo']
    search_fields = ['anim_nombre', 'anim_numero']
    ordering_fields = ['anim_numero', 'anim_nombre', 'anim_fecha_nacimiento']
    ordering = ['anim_numero']

    def get_serializer_class(self):
        if self.action == 'list':
            return AnimalListSerializer
        return AnimalSerializer


class PesajeViewSet(viewsets.ModelViewSet):
    queryset = Pesaje.objects.select_related('animal', 'unidad').all()
    serializer_class = PesajeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['animal']
    ordering = ['-pesa_fecha']


class ProduccionDiariaAnimalViewSet(viewsets.ModelViewSet):
    queryset = ProduccionDiariaAnimal.objects.select_related('animal', 'unidad').all()
    serializer_class = ProduccionDiariaAnimalSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['animal']
    ordering = ['-pdia_fecha']


class ProduccionDiariaTamboViewSet(viewsets.ModelViewSet):
    queryset = ProduccionDiariaTambo.objects.select_related('tambo', 'unidad').all()
    serializer_class = ProduccionDiariaTamboSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['tambo']
    ordering = ['-pdit_fecha']


class HistorialEstadoAnimalViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstadoAnimal.objects.select_related('animal', 'estado').all()
    serializer_class = HistorialEstadoAnimalSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['animal']
    ordering = ['-hiea_fecha']


class CampoAnimalViewSet(viewsets.ModelViewSet):
    queryset = CampoAnimal.objects.select_related('campo', 'animal').all()
    serializer_class = CampoAnimalSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['campo', 'animal']
    ordering = ['-fecha_alta']