from rest_framework import serializers
from .models import (
    Establecimiento, Tambo, Campo, CampoTambo, Cultivo, Siembra,
    Raza, Categoria, Animal, CampoAnimal, HistorialEstadoAnimal,
    Pesaje, ProduccionDiariaAnimal, ProduccionDiariaTambo, Reproduccion
)


class EstablecimientoSerializer(serializers.ModelSerializer):
    localidad_nombre = serializers.CharField(source='localidad.loca_nombre', read_only=True)

    class Meta:
        model = Establecimiento
        fields = [
            'estb_id', 'estb_nombre', 'estb_imagen', 'cuit',
            'estb_direccion', 'estb_codigo_postal',
            'localidad', 'localidad_nombre',
            'estb_telefono', 'estb_fax', 'estb_email',
            'estb_contacto_nya', 'estb_contacto_telefono',
            'estb_contacto_celular', 'estb_contacto_email',
            'estb_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['estb_id', 'fecha_alta']


class TamboSerializer(serializers.ModelSerializer):
    establecimiento_nombre = serializers.CharField(source='establecimiento.estb_nombre', read_only=True)
    localidad_nombre = serializers.CharField(source='localidad.loca_nombre', read_only=True)

    class Meta:
        model = Tambo
        fields = [
            'tamb_id', 'establecimiento', 'establecimiento_nombre',
            'tamb_nombre', 'tamb_fecha_establecimiento',
            'tamb_direccion', 'tamb_codigo_postal',
            'localidad', 'localidad_nombre',
            'tamb_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['tamb_id', 'fecha_alta']


class CampoSerializer(serializers.ModelSerializer):
    establecimiento_nombre = serializers.CharField(source='establecimiento.estb_nombre', read_only=True)
    localidad_nombre = serializers.CharField(source='localidad.loca_nombre', read_only=True)

    class Meta:
        model = Campo
        fields = [
            'camp_id', 'establecimiento', 'establecimiento_nombre',
            'camp_nombre', 'camp_area',
            'camp_direccion', 'camp_codigo_postal',
            'localidad', 'localidad_nombre',
            'camp_telefono', 'camp_email',
            'camp_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['camp_id', 'fecha_alta']


class CultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cultivo
        fields = ['cult_id', 'cult_nombre', 'cult_observaciones', 'fecha_alta']
        read_only_fields = ['cult_id', 'fecha_alta']


class SiembraSerializer(serializers.ModelSerializer):
    campo_nombre = serializers.CharField(source='campo.camp_nombre', read_only=True)
    cultivo_nombre = serializers.CharField(source='cultivo.cult_nombre', read_only=True)

    class Meta:
        model = Siembra
        fields = [
            'siem_id', 'campo', 'campo_nombre', 'cultivo', 'cultivo_nombre',
            'siem_area', 'siem_fecha_siembra', 'siem_fecha_cosecha',
            'siem_cantidad_cosechada', 'unidad', 'siem_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['siem_id', 'fecha_alta']


class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = ['raza_id', 'raza_nombre', 'raza_observaciones', 'fecha_alta']
        read_only_fields = ['raza_id', 'fecha_alta']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['cate_id', 'cate_nombre', 'cate_observaciones', 'fecha_alta']
        read_only_fields = ['cate_id', 'fecha_alta']


class ReproduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reproduccion
        fields = [
            'repr_id', 'repr_fecha_servicio', 'repr_fecha_estimada_parto',
            'repr_fecha_real_parto', 'repr_datos_inseminador',
            'repr_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['repr_id', 'fecha_alta']


class AnimalListSerializer(serializers.ModelSerializer):
    raza_nombre = serializers.CharField(source='raza.raza_nombre', read_only=True)
    categoria_nombre = serializers.CharField(source='categoria.cate_nombre', read_only=True)
    estado_repro = serializers.CharField(source='estado_reproductivo.esta_nombre', read_only=True)
    estado_prod = serializers.CharField(source='estado_productivo.esta_nombre', read_only=True)

    class Meta:
        model = Animal
        fields = [
            'anim_id', 'anim_numero', 'anim_nombre', 'anim_sexo',
            'raza_nombre', 'categoria_nombre',
            'estado_repro', 'estado_prod',
            'anim_fecha_nacimiento',
        ]


class AnimalSerializer(serializers.ModelSerializer):
    raza_nombre = serializers.CharField(source='raza.raza_nombre', read_only=True)
    categoria_nombre = serializers.CharField(source='categoria.cate_nombre', read_only=True)
    estado_reproductivo_nombre = serializers.CharField(
        source='estado_reproductivo.esta_nombre', read_only=True
    )
    estado_productivo_nombre = serializers.CharField(
        source='estado_productivo.esta_nombre', read_only=True
    )

    class Meta:
        model = Animal
        fields = [
            'anim_id', 'madre', 'padre',
            'anim_nombre', 'anim_sexo',
            'raza', 'raza_nombre',
            'categoria', 'categoria_nombre',
            'anim_numero', 'anim_foto',
            'anim_fecha_nacimiento', 'anim_fecha_establecimiento',
            'anim_fecha_tatuaje', 'anim_fecha_fallecimiento',
            'estado_reproductivo', 'estado_reproductivo_nombre',
            'estado_productivo', 'estado_productivo_nombre',
            'reproduccion_actual',
            'anim_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['anim_id', 'fecha_alta']

    def validate(self, attrs):
        madre = attrs.get('madre')
        padre = attrs.get('padre')

        if madre and madre.anim_sexo != 'H':
            raise serializers.ValidationError({'madre': 'La madre debe ser Hembra.'})

        if padre and padre.anim_sexo != 'M':
            raise serializers.ValidationError({'padre': 'El padre debe ser Macho.'})

        if madre and padre and madre.anim_id == padre.anim_id:
            raise serializers.ValidationError('Madre y padre no pueden ser el mismo animal.')

        estado_repro = attrs.get('estado_reproductivo')
        if estado_repro and estado_repro.esta_uso != 'VR':
            raise serializers.ValidationError({
                'estado_reproductivo': 'El estado debe ser de uso VR (Vaca-Reproductivo).'
            })

        estado_prod = attrs.get('estado_productivo')
        if estado_prod and estado_prod.esta_uso != 'VP':
            raise serializers.ValidationError({
                'estado_productivo': 'El estado debe ser de uso VP (Vaca-Productivo).'
            })

        f_nac = attrs.get('anim_fecha_nacimiento')
        f_fall = attrs.get('anim_fecha_fallecimiento')
        if f_nac and f_fall and f_fall < f_nac:
            raise serializers.ValidationError({
                'anim_fecha_fallecimiento': 'No puede ser anterior al nacimiento.'
            })

        return attrs


class PesajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesaje
        fields = [
            'pesa_id', 'animal', 'pesa_fecha', 'pesa_valor',
            'unidad', 'pesa_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['pesa_id', 'fecha_alta']


class ProduccionDiariaAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduccionDiariaAnimal
        fields = [
            'pdia_id', 'animal', 'pdia_fecha',
            'pdia_cantidad_producida', 'pdia_cantidad_consumida',
            'unidad', 'pdia_porcentaje_grasa', 'pdia_porcentaje_proteinas',
            'pdia_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['pdia_id', 'fecha_alta']


class ProduccionDiariaTamboSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduccionDiariaTambo
        fields = [
            'pdit_id', 'tambo', 'pdit_fecha',
            'pdit_cantidad_producida', 'pdit_cantidad_consumida',
            'pdit_cantidad_animales_productores',
            'unidad', 'pdit_porcentaje_grasa', 'pdit_porcentaje_proteinas',
            'pdit_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['pdit_id', 'fecha_alta']


class HistorialEstadoAnimalSerializer(serializers.ModelSerializer):
    estado_nombre = serializers.CharField(source='estado.esta_nombre', read_only=True)

    class Meta:
        model = HistorialEstadoAnimal
        fields = [
            'hiea_id', 'animal', 'estado', 'estado_nombre',
            'hiea_fecha', 'hiea_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['hiea_id', 'fecha_alta']


class CampoAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampoAnimal
        fields = [
            'caan_id', 'campo', 'animal',
            'caan_fecha', 'caan_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['caan_id', 'fecha_alta']