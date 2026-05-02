from rest_framework import serializers
from .models import (
    Cliente, Proveedor, CategoriaMovimiento, ConceptoMovimiento,
    Caja, MovimientoCaja, Venta, VentaAnimalDetalle, VentaCosechaDetalle,
    VentaMovimientoCaja, Compra, CompraAnimalDetalle, CompraCultivoDetalle,
    CompraMovimientoCaja
)


class ClienteSerializer(serializers.ModelSerializer):
    localidad_nombre = serializers.CharField(source='localidad.loca_nombre', read_only=True)

    class Meta:
        model = Cliente
        fields = [
            'clie_id', 'clie_nombre', 'clie_imagen', 'cuit',
            'clie_direccion', 'clie_codigo_postal',
            'localidad', 'localidad_nombre',
            'clie_telefono', 'clie_fax', 'clie_email',
            'clie_contacto_nya', 'clie_contacto_telefono',
            'clie_contacto_celular', 'clie_contacto_email',
            'clie_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['clie_id', 'fecha_alta']


class ProveedorSerializer(serializers.ModelSerializer):
    localidad_nombre = serializers.CharField(source='localidad.loca_nombre', read_only=True)

    class Meta:
        model = Proveedor
        fields = [
            'prov_id', 'prov_nombre', 'cuit',
            'prov_direccion', 'prov_codigo_postal',
            'localidad', 'localidad_nombre',
            'prov_telefono', 'prov_fax', 'prov_email',
            'prov_contacto_nya', 'prov_contacto_telefono',
            'prov_contacto_celular', 'prov_contacto_email',
            'prov_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['prov_id', 'fecha_alta']


class CategoriaMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaMovimiento
        fields = ['camo_id', 'camo_nombre', 'camo_observaciones', 'fecha_alta']
        read_only_fields = ['camo_id', 'fecha_alta']


class ConceptoMovimientoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(
        source='categoria_movimiento.camo_nombre', read_only=True
    )

    class Meta:
        model = ConceptoMovimiento
        fields = [
            'como_id', 'categoria_movimiento', 'categoria_nombre',
            'como_codigo', 'como_nombre', 'como_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['como_id', 'fecha_alta']


class CajaSerializer(serializers.ModelSerializer):
    establecimiento_nombre = serializers.CharField(
        source='establecimiento.estb_nombre', read_only=True
    )
    esta_abierta = serializers.BooleanField(read_only=True)

    class Meta:
        model = Caja
        fields = [
            'caja_id', 'establecimiento', 'establecimiento_nombre',
            'caja_fecha_inicio', 'caja_fecha_fin',
            'esta_abierta', 'caja_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['caja_id', 'fecha_alta']


class MovimientoCajaSerializer(serializers.ModelSerializer):
    concepto_nombre = serializers.CharField(source='concepto.como_nombre', read_only=True)

    class Meta:
        model = MovimientoCaja
        fields = [
            'moca_id', 'caja', 'concepto', 'concepto_nombre',
            'moca_fecha', 'moca_tipo', 'moca_cantidad',
            'unidad', 'moca_monto', 'moca_observaciones', 'fecha_alta',
        ]
        read_only_fields = ['moca_id', 'fecha_alta']

    def validate(self, attrs):
        caja = attrs.get('caja')
        if caja and not caja.esta_abierta:
            raise serializers.ValidationError(
                'No se pueden registrar movimientos en una caja cerrada.'
            )
        return attrs


class VentaAnimalDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaAnimalDetalle
        fields = [
            'vade_id', 'animal', 'vade_peso_venta',
            'unidad', 'vade_precio_venta', 'vade_observaciones',
        ]
        read_only_fields = ['vade_id']


class VentaCosechaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentaCosechaDetalle
        fields = [
            'vcde_id', 'cultivo', 'vcde_cantidad',
            'unidad', 'vcde_precio_venta', 'vcde_observaciones',
        ]
        read_only_fields = ['vcde_id']


class VentaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.clie_nombre', read_only=True)
    establecimiento_nombre = serializers.CharField(
        source='establecimiento.estb_nombre', read_only=True
    )
    detalles_animal = VentaAnimalDetalleSerializer(many=True, read_only=True)
    detalles_cosecha = VentaCosechaDetalleSerializer(many=True, read_only=True)

    class Meta:
        model = Venta
        fields = [
            'vent_id', 'establecimiento', 'establecimiento_nombre',
            'cliente', 'cliente_nombre',
            'vent_fecha', 'vent_observaciones',
            'detalles_animal', 'detalles_cosecha', 'fecha_alta',
        ]
        read_only_fields = ['vent_id', 'fecha_alta']


class CompraAnimalDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraAnimalDetalle
        fields = [
            'cade_id', 'animal', 'cade_peso_compra',
            'unidad', 'cade_precio_compra', 'cade_observaciones',
        ]
        read_only_fields = ['cade_id']


class CompraCultivoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraCultivoDetalle
        fields = [
            'ccde_id', 'cultivo', 'ccde_cantidad',
            'unidad', 'ccde_precio_compra', 'ccde_observaciones',
        ]
        read_only_fields = ['ccde_id']


class CompraSerializer(serializers.ModelSerializer):
    proveedor_nombre = serializers.CharField(source='proveedor.prov_nombre', read_only=True)
    establecimiento_nombre = serializers.CharField(
        source='establecimiento.estb_nombre', read_only=True
    )
    detalles_animal = CompraAnimalDetalleSerializer(many=True, read_only=True)
    detalles_cultivo = CompraCultivoDetalleSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = [
            'comp_id', 'establecimiento', 'establecimiento_nombre',
            'proveedor', 'proveedor_nombre',
            'comp_fecha', 'comp_observaciones',
            'detalles_animal', 'detalles_cultivo', 'fecha_alta',
        ]
        read_only_fields = ['comp_id', 'fecha_alta']