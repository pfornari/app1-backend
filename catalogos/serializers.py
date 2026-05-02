from rest_framework import serializers
from .models import Pais, Provincia, Localidad, Estado, TipoUnidad, Unidad, ConversionUnidad


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['pais_id', 'pais_nombre', 'pais_descripcion']


class ProvinciaSerializer(serializers.ModelSerializer):
    pais_nombre = serializers.CharField(source='pais.pais_nombre', read_only=True)

    class Meta:
        model = Provincia
        fields = ['prvi_id', 'pais', 'pais_nombre', 'prvi_nombre', 'prvi_descripcion']


class LocalidadSerializer(serializers.ModelSerializer):
    provincia_nombre = serializers.CharField(source='provincia.prvi_nombre', read_only=True)

    class Meta:
        model = Localidad
        fields = ['loca_id', 'provincia', 'provincia_nombre', 'loca_nombre', 'loca_descripcion']


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['esta_id', 'esta_identificador', 'esta_nombre', 'esta_color', 'esta_uso']


class TipoUnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUnidad
        fields = ['tiun_id', 'tiun_nombre', 'tiun_observaciones']


class UnidadSerializer(serializers.ModelSerializer):
    tipo_unidad_nombre = serializers.CharField(source='tipo_unidad.tiun_nombre', read_only=True)

    class Meta:
        model = Unidad
        fields = ['unid_id', 'tipo_unidad', 'tipo_unidad_nombre', 'unid_nombre', 'unid_observaciones']


class ConversionUnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversionUnidad
        fields = ['coun_id', 'unidad_origen', 'unidad_destino', 'coun_proporcion']