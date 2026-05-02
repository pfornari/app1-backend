from django.db import models
from core.models import TimestampedSoftDeleteModel


class Pais(TimestampedSoftDeleteModel):
    pais_id = models.IntegerField(primary_key=True)
    pais_nombre = models.CharField(max_length=100)
    pais_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'pais'
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ['pais_nombre']

    def __str__(self):
        return self.pais_nombre


class Provincia(TimestampedSoftDeleteModel):
    prvi_id = models.IntegerField(primary_key=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, related_name='provincias')
    prvi_nombre = models.CharField(max_length=100)
    prvi_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'provincia'
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        ordering = ['prvi_nombre']

    def __str__(self):
        return self.prvi_nombre


class Localidad(TimestampedSoftDeleteModel):
    loca_id = models.IntegerField(primary_key=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, related_name='localidades')
    loca_nombre = models.CharField(max_length=100)
    loca_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'localidad'
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        ordering = ['loca_nombre']

    def __str__(self):
        return self.loca_nombre


class Estado(models.Model):
    """
    Catálogo de estados de animales.
    No hereda de TimestampedSoftDeleteModel porque es un catálogo
    fijo sin fechas de alta/baja.
    USO: VR = Vaca Reproductivo / VP = Vaca Productivo
    """
    USO_CHOICES = (
        ('VR', 'Vaca - Reproductivo'),
        ('VP', 'Vaca - Productivo'),
    )

    esta_id = models.IntegerField(primary_key=True)
    esta_identificador = models.CharField(max_length=1)
    esta_nombre = models.CharField(max_length=100)
    esta_color = models.CharField(max_length=7, null=True, blank=True)
    esta_uso = models.CharField(max_length=2, choices=USO_CHOICES, null=True, blank=True)

    class Meta:
        db_table = 'estado'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.esta_nombre


class TipoUnidad(TimestampedSoftDeleteModel):
    tiun_id = models.IntegerField(primary_key=True)
    tiun_nombre = models.CharField(max_length=100)
    tiun_observaciones = models.CharField(max_length=500, null=True, blank=True)
    tiun_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'tipo_unidad'
        verbose_name = 'Tipo de Unidad'
        verbose_name_plural = 'Tipos de Unidad'
        ordering = ['tiun_nombre']

    def __str__(self):
        return self.tiun_nombre


class Unidad(TimestampedSoftDeleteModel):
    unid_id = models.IntegerField(primary_key=True)
    tipo_unidad = models.ForeignKey(TipoUnidad, on_delete=models.PROTECT, related_name='unidades')
    unid_nombre = models.CharField(max_length=100)
    unid_observaciones = models.CharField(max_length=500, null=True, blank=True)
    unid_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'unidad'
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
        ordering = ['unid_nombre']

    def __str__(self):
        return self.unid_nombre


class ConversionUnidad(TimestampedSoftDeleteModel):
    coun_id = models.IntegerField(primary_key=True)
    unidad_origen = models.ForeignKey(
        Unidad, on_delete=models.PROTECT, related_name='conversiones_origen'
    )
    unidad_destino = models.ForeignKey(
        Unidad, on_delete=models.PROTECT, related_name='conversiones_destino'
    )
    coun_proporcion = models.FloatField(null=True, blank=True)
    coun_observaciones = models.CharField(max_length=500, null=True, blank=True)
    coun_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'conversion_unidad'
        verbose_name = 'Conversión de Unidad'
        verbose_name_plural = 'Conversiones de Unidad'

    def __str__(self):
        return f'{self.unidad_origen} → {self.unidad_destino}'