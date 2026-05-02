from django.db import models
from core.models import TimestampedSoftDeleteModel


class Cliente(TimestampedSoftDeleteModel):
    clie_id = models.AutoField(primary_key=True)
    clie_nombre = models.CharField(max_length=100)
    clie_imagen = models.BooleanField(default=False)
    cuit = models.CharField(max_length=13, null=True, blank=True)
    clie_direccion = models.CharField(max_length=100, null=True, blank=True)
    clie_codigo_postal = models.CharField(max_length=10, null=True, blank=True)
    localidad = models.ForeignKey(
        'catalogos.Localidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='clientes'
    )
    clie_telefono = models.CharField(max_length=50, null=True, blank=True)
    clie_fax = models.CharField(max_length=50, null=True, blank=True)
    clie_email = models.EmailField(max_length=100, null=True, blank=True)
    clie_contacto_nya = models.CharField(max_length=100, null=True, blank=True)
    clie_contacto_telefono = models.CharField(max_length=50, null=True, blank=True)
    clie_contacto_celular = models.CharField(max_length=50, null=True, blank=True)
    clie_contacto_email = models.EmailField(max_length=100, null=True, blank=True)
    clie_observaciones = models.CharField(max_length=500, null=True, blank=True)
    clie_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['clie_nombre']

    def __str__(self):
        return self.clie_nombre


class Proveedor(TimestampedSoftDeleteModel):
    prov_id = models.AutoField(primary_key=True)
    prov_nombre = models.CharField(max_length=100)
    cuit = models.CharField(max_length=13, null=True, blank=True)
    prov_direccion = models.CharField(max_length=100, null=True, blank=True)
    prov_codigo_postal = models.CharField(max_length=10, null=True, blank=True)
    localidad = models.ForeignKey(
        'catalogos.Localidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='proveedores'
    )
    prov_telefono = models.CharField(max_length=50, null=True, blank=True)
    prov_fax = models.CharField(max_length=50, null=True, blank=True)
    prov_email = models.EmailField(max_length=100, null=True, blank=True)
    prov_contacto_nya = models.CharField(max_length=100, null=True, blank=True)
    prov_contacto_telefono = models.CharField(max_length=50, null=True, blank=True)
    prov_contacto_celular = models.CharField(max_length=50, null=True, blank=True)
    prov_contacto_email = models.EmailField(max_length=100, null=True, blank=True)
    prov_observaciones = models.CharField(max_length=500, null=True, blank=True)
    prov_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['prov_nombre']

    def __str__(self):
        return self.prov_nombre


class CategoriaMovimiento(TimestampedSoftDeleteModel):
    camo_id = models.AutoField(primary_key=True)
    camo_nombre = models.CharField(max_length=100)
    camo_observaciones = models.CharField(max_length=500, null=True, blank=True)
    camo_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'categoria_movimiento'
        verbose_name = 'Categoría de Movimiento'
        verbose_name_plural = 'Categorías de Movimiento'
        ordering = ['camo_nombre']

    def __str__(self):
        return self.camo_nombre


class ConceptoMovimiento(TimestampedSoftDeleteModel):
    como_id = models.AutoField(primary_key=True)
    categoria_movimiento = models.ForeignKey(
        CategoriaMovimiento, on_delete=models.PROTECT,
        null=True, blank=True, related_name='conceptos'
    )
    como_codigo = models.CharField(max_length=5, null=True, blank=True)
    como_nombre = models.CharField(max_length=100, null=True, blank=True)
    como_observaciones = models.CharField(max_length=500, null=True, blank=True)
    como_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'concepto_movimiento'
        verbose_name = 'Concepto de Movimiento'
        verbose_name_plural = 'Conceptos de Movimiento'
        ordering = ['como_nombre']

    def __str__(self):
        return self.como_nombre or f'Concepto {self.como_id}'


class Caja(TimestampedSoftDeleteModel):
    caja_id = models.AutoField(primary_key=True)
    establecimiento = models.ForeignKey(
        'gestion.Establecimiento', on_delete=models.PROTECT, related_name='cajas'
    )
    caja_fecha_inicio = models.DateTimeField()
    caja_fecha_fin = models.DateTimeField(null=True, blank=True)
    caja_observaciones = models.CharField(max_length=500, null=True, blank=True)
    caja_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'caja'
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'
        ordering = ['-caja_fecha_inicio']

    def __str__(self):
        return f'Caja {self.caja_id} — {self.establecimiento}'

    @property
    def esta_abierta(self):
        return self.caja_fecha_fin is None


class MovimientoCaja(TimestampedSoftDeleteModel):
    TIPO_CHOICES = (('D', 'Debe'), ('H', 'Haber'))

    moca_id = models.AutoField(primary_key=True)
    caja = models.ForeignKey(Caja, on_delete=models.PROTECT, related_name='movimientos')
    concepto = models.ForeignKey(ConceptoMovimiento, on_delete=models.PROTECT, related_name='movimientos')
    moca_fecha = models.DateTimeField()
    moca_tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, null=True, blank=True)
    moca_cantidad = models.FloatField(null=True, blank=True)
    unidad = models.ForeignKey(
        'catalogos.Unidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='movimientos_caja'
    )
    moca_monto = models.FloatField(null=True, blank=True)
    moca_observaciones = models.CharField(max_length=500, null=True, blank=True)
    moca_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'movimiento_caja'
        verbose_name = 'Movimiento de Caja'
        verbose_name_plural = 'Movimientos de Caja'
        ordering = ['-moca_fecha']


class Venta(TimestampedSoftDeleteModel):
    vent_id = models.AutoField(primary_key=True)
    establecimiento = models.ForeignKey(
        'gestion.Establecimiento', on_delete=models.PROTECT, related_name='ventas'
    )
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT,
        null=True, blank=True, related_name='ventas'
    )
    vent_fecha = models.DateTimeField()
    vent_observaciones = models.CharField(max_length=500, null=True, blank=True)
    vent_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'venta'
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['-vent_fecha']

    def __str__(self):
        return f'Venta {self.vent_id} — {self.vent_fecha.date()}'


class VentaAnimalDetalle(TimestampedSoftDeleteModel):
    vade_id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles_animal')
    animal = models.ForeignKey('gestion.Animal', on_delete=models.PROTECT, related_name='ventas_detalle')
    vade_peso_venta = models.FloatField(null=True, blank=True)
    unidad = models.ForeignKey(
        'catalogos.Unidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='ventas_animal'
    )
    vade_precio_venta = models.FloatField(null=True, blank=True)
    vade_observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'venta_animal_detalle'
        verbose_name = 'Detalle Venta Animal'


class VentaCosechaDetalle(TimestampedSoftDeleteModel):
    vcde_id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles_cosecha')
    cultivo = models.ForeignKey('gestion.Cultivo', on_delete=models.PROTECT, null=True, blank=True)
    vcde_cantidad = models.FloatField(null=True, blank=True)
    unidad = models.ForeignKey(
        'catalogos.Unidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='ventas_cosecha'
    )
    vcde_precio_venta = models.FloatField(null=True, blank=True)
    vcde_observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'venta_cosecha_detalle'
        verbose_name = 'Detalle Venta Cosecha'


class VentaMovimientoCaja(TimestampedSoftDeleteModel):
    vemc_id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='movimientos_caja')
    movimiento_caja = models.ForeignKey(MovimientoCaja, on_delete=models.PROTECT)
    vemc_observaciones = models.CharField(max_length=500, null=True, blank=True)
    vemc_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'venta_movimiento_caja'
        verbose_name = 'Venta-Movimiento Caja'


class Compra(TimestampedSoftDeleteModel):
    comp_id = models.AutoField(primary_key=True)
    establecimiento = models.ForeignKey(
        'gestion.Establecimiento', on_delete=models.PROTECT, related_name='compras'
    )
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.PROTECT,
        null=True, blank=True, related_name='compras'
    )
    comp_fecha = models.DateTimeField()
    comp_observaciones = models.CharField(max_length=500, null=True, blank=True)
    comp_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'compra'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['-comp_fecha']

    def __str__(self):
        return f'Compra {self.comp_id} — {self.comp_fecha.date()}'


class CompraAnimalDetalle(TimestampedSoftDeleteModel):
    cade_id = models.AutoField(primary_key=True)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='detalles_animal')
    animal = models.ForeignKey('gestion.Animal', on_delete=models.PROTECT, related_name='compras_detalle')
    cade_peso_compra = models.FloatField(null=True, blank=True)
    unidad = models.ForeignKey(
        'catalogos.Unidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='compras_animal'
    )
    cade_precio_compra = models.FloatField(null=True, blank=True)
    cade_observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'compra_animal_detalle'
        verbose_name = 'Detalle Compra Animal'


class CompraCultivoDetalle(TimestampedSoftDeleteModel):
    ccde_id = models.AutoField(primary_key=True)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='detalles_cultivo')
    cultivo = models.ForeignKey('gestion.Cultivo', on_delete=models.PROTECT, null=True, blank=True)
    ccde_cantidad = models.FloatField(null=True, blank=True)
    unidad = models.ForeignKey(
        'catalogos.Unidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='compras_cultivo'
    )
    ccde_precio_compra = models.FloatField(null=True, blank=True)
    ccde_observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'compra_cultivo_detalle'
        verbose_name = 'Detalle Compra Cultivo'


class CompraMovimientoCaja(TimestampedSoftDeleteModel):
    comc_id = models.AutoField(primary_key=True)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='movimientos_caja')
    movimiento_caja = models.ForeignKey(MovimientoCaja, on_delete=models.PROTECT)
    comc_observaciones = models.CharField(max_length=500, null=True, blank=True)
    comc_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'compra_movimiento_caja'
        verbose_name = 'Compra-Movimiento Caja'