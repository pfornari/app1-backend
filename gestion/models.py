from django.db import models
from core.models import TimestampedSoftDeleteModel


class Establecimiento(TimestampedSoftDeleteModel):
    estb_id = models.AutoField(primary_key=True)
    estb_nombre = models.CharField(max_length=100)
    estb_imagen = models.BooleanField(default=False)
    cuit = models.CharField(max_length=13, null=True, blank=True)
    estb_direccion = models.CharField(max_length=100, null=True, blank=True)
    estb_codigo_postal = models.CharField(max_length=10, null=True, blank=True)
    localidad = models.ForeignKey(
        'catalogos.Localidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='establecimientos'
    )
    estb_telefono = models.CharField(max_length=50, null=True, blank=True)
    estb_fax = models.CharField(max_length=50, null=True, blank=True)
    estb_email = models.EmailField(max_length=100, null=True, blank=True)
    estb_contacto_nya = models.CharField(max_length=100, null=True, blank=True)
    estb_contacto_telefono = models.CharField(max_length=50, null=True, blank=True)
    estb_contacto_celular = models.CharField(max_length=50, null=True, blank=True)
    estb_contacto_email = models.EmailField(max_length=100, null=True, blank=True)
    estb_observaciones = models.CharField(max_length=500, null=True, blank=True)
    estb_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'establecimiento'
        verbose_name = 'Establecimiento'
        verbose_name_plural = 'Establecimientos'
        ordering = ['estb_nombre']

    def __str__(self):
        return self.estb_nombre


class Tambo(TimestampedSoftDeleteModel):
    tamb_id = models.AutoField(primary_key=True)
    establecimiento = models.ForeignKey(
        Establecimiento, on_delete=models.PROTECT, related_name='tambos'
    )
    tamb_nombre = models.CharField(max_length=100)
    tamb_fecha_establecimiento = models.DateField(null=True, blank=True)
    tamb_direccion = models.CharField(max_length=100, null=True, blank=True)
    tamb_codigo_postal = models.CharField(max_length=10, null=True, blank=True)
    localidad = models.ForeignKey(
        'catalogos.Localidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='tambos'
    )
    tamb_observaciones = models.CharField(max_length=500, null=True, blank=True)
    tamb_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'tambo'
        verbose_name = 'Tambo'
        verbose_name_plural = 'Tambos'
        ordering = ['tamb_nombre']

    def __str__(self):
        return self.tamb_nombre


class Campo(TimestampedSoftDeleteModel):
    camp_id = models.AutoField(primary_key=True)
    establecimiento = models.ForeignKey(
        Establecimiento, on_delete=models.PROTECT,
        null=True, blank=True, related_name='campos'
    )
    camp_nombre = models.CharField(max_length=100, null=True, blank=True)
    camp_area = models.SmallIntegerField(null=True, blank=True)
    camp_direccion = models.CharField(max_length=100, null=True, blank=True)
    camp_codigo_postal = models.CharField(max_length=10, null=True, blank=True)
    localidad = models.ForeignKey(
        'catalogos.Localidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='campos'
    )
    camp_telefono = models.CharField(max_length=50, null=True, blank=True)
    camp_email = models.EmailField(max_length=100, null=True, blank=True)
    camp_latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    camp_longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    camp_observaciones = models.CharField(max_length=500, null=True, blank=True)
    camp_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'campo'
        verbose_name = 'Campo'
        verbose_name_plural = 'Campos'
        ordering = ['camp_nombre']

    def __str__(self):
        return self.camp_nombre or f'Campo {self.camp_id}'


class CampoTambo(TimestampedSoftDeleteModel):
    cata_id = models.AutoField(primary_key=True)
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT, related_name='campo_tambos')
    tambo = models.ForeignKey(Tambo, on_delete=models.PROTECT, related_name='campo_tambos')
    cata_fecha = models.DateField(null=True, blank=True)
    cata_observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'campo_tambo'
        verbose_name = 'Campo-Tambo'
        verbose_name_plural = 'Campos-Tambos'


class Cultivo(TimestampedSoftDeleteModel):
    cult_id = models.AutoField(primary_key=True)
    cult_nombre = models.CharField(max_length=100)
    cult_observaciones = models.CharField(max_length=500, null=True, blank=True)
    cult_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'cultivo'
        verbose_name = 'Cultivo'
        verbose_name_plural = 'Cultivos'
        ordering = ['cult_nombre']

    def __str__(self):
        return self.cult_nombre


class Siembra(TimestampedSoftDeleteModel):
    siem_id = models.AutoField(primary_key=True)
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT, related_name='siembras')
    cultivo = models.ForeignKey(Cultivo, on_delete=models.PROTECT, related_name='siembras')
    siem_area = models.SmallIntegerField(null=True, blank=True)
    siem_fecha_siembra = models.DateField()
    siem_fecha_cosecha = models.DateField(null=True, blank=True)
    siem_cantidad_cosechada = models.FloatField(null=True, blank=True)
    unidad = models.ForeignKey(
        'catalogos.Unidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='siembras'
    )
    siem_observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'siembra'
        verbose_name = 'Siembra'
        verbose_name_plural = 'Siembras'
        ordering = ['-siem_fecha_siembra']


class Raza(TimestampedSoftDeleteModel):
    raza_id = models.AutoField(primary_key=True)
    raza_nombre = models.CharField(max_length=50)
    raza_observaciones = models.CharField(max_length=500, null=True, blank=True)
    raza_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'raza'
        ordering = ['raza_nombre']

    def __str__(self):
        return self.raza_nombre


class Categoria(TimestampedSoftDeleteModel):
    cate_id = models.AutoField(primary_key=True)
    cate_nombre = models.CharField(max_length=50)
    cate_observaciones = models.CharField(max_length=500, null=True, blank=True)
    cate_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'categoria'
        verbose_name_plural = 'Categorías'
        ordering = ['cate_nombre']

    def __str__(self):
        return self.cate_nombre


class Reproduccion(TimestampedSoftDeleteModel):
    repr_id = models.AutoField(primary_key=True)
    repr_fecha_servicio = models.DateField(null=True, blank=True)
    repr_fecha_estimada_parto = models.DateField(null=True, blank=True)
    repr_fecha_real_parto = models.DateField(null=True, blank=True)
    repr_datos_inseminador = models.CharField(max_length=100, null=True, blank=True)
    repr_observaciones = models.CharField(max_length=500, null=True, blank=True)
    repr_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'reproduccion'
        verbose_name = 'Reproducción'
        verbose_name_plural = 'Reproducciones'
        ordering = ['-repr_fecha_servicio']


class Animal(TimestampedSoftDeleteModel):
    SEXO_CHOICES = (('H', 'Hembra'), ('M', 'Macho'))

    anim_id = models.AutoField(primary_key=True)
    madre = models.ForeignKey(
        'self', on_delete=models.PROTECT,
        null=True, blank=True, related_name='hijos_madre'
    )
    padre = models.ForeignKey(
        'self', on_delete=models.PROTECT,
        null=True, blank=True, related_name='hijos_padre'
    )
    anim_nombre = models.CharField(max_length=50, null=True, blank=True)
    anim_sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True, blank=True)
    raza = models.ForeignKey(Raza, on_delete=models.PROTECT, null=True, blank=True, related_name='animales')
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, blank=True, related_name='animales')
    anim_numero = models.IntegerField(null=True, blank=True)
    anim_foto = models.BooleanField(default=False)
    anim_fecha_nacimiento = models.DateField(null=True, blank=True)
    anim_fecha_establecimiento = models.DateField(null=True, blank=True)
    anim_fecha_tatuaje = models.DateField(null=True, blank=True)
    anim_fecha_fallecimiento = models.DateField(null=True, blank=True)
    estado_reproductivo = models.ForeignKey(
        'catalogos.Estado', on_delete=models.PROTECT,
        null=True, blank=True, related_name='animales_repro'
    )
    estado_productivo = models.ForeignKey(
        'catalogos.Estado', on_delete=models.PROTECT,
        null=True, blank=True, related_name='animales_prod'
    )
    reproduccion_actual = models.ForeignKey(
        Reproduccion, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='+'
    )
    anim_observaciones = models.CharField(max_length=500, null=True, blank=True)
    anim_descripcion = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'animal'
        ordering = ['anim_numero', 'anim_nombre']

    def __str__(self):
        if self.anim_numero and self.anim_nombre:
            return f'#{self.anim_numero} — {self.anim_nombre}'
        return self.anim_nombre or f'Animal {self.anim_id}'


class CampoAnimal(TimestampedSoftDeleteModel):
    caan_id = models.AutoField(primary_key=True)
    campo = models.ForeignKey(Campo, on_delete=models.PROTECT, related_name='campo_animales')
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, related_name='campo_animales')
    caan_fecha = models.DateField(null=True, blank=True)
    caan_observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'campo_animal'
        verbose_name = 'Campo-Animal'


class HistorialEstadoAnimal(TimestampedSoftDeleteModel):
    hiea_id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, related_name='historial_estados')
    estado = models.ForeignKey('catalogos.Estado', on_delete=models.PROTECT)
    hiea_fecha = models.DateField(null=True, blank=True)
    hiea_observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'historial_estado_animal'
        verbose_name = 'Historial Estado Animal'
        ordering = ['-hiea_fecha']


class Pesaje(TimestampedSoftDeleteModel):
    pesa_id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, related_name='pesajes')
    pesa_fecha = models.DateField()
    pesa_valor = models.FloatField()
    unidad = models.ForeignKey(
        'catalogos.Unidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='pesajes'
    )
    pesa_observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'pesaje'
        verbose_name = 'Pesaje'
        ordering = ['-pesa_fecha']


class ProduccionDiariaAnimal(TimestampedSoftDeleteModel):
    pdia_id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.PROTECT, related_name='producciones_diarias')
    pdia_fecha = models.DateField()
    pdia_cantidad_producida = models.FloatField(null=True, blank=True)
    pdia_cantidad_consumida = models.FloatField(null=True, blank=True)
    unidad = models.ForeignKey(
        'catalogos.Unidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='producciones_animal'
    )
    pdia_porcentaje_grasa = models.FloatField(null=True, blank=True)
    pdia_porcentaje_proteinas = models.FloatField(null=True, blank=True)
    pdia_observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'produccion_diaria_animal'
        verbose_name = 'Producción Diaria Animal'
        ordering = ['-pdia_fecha']


class ProduccionDiariaTambo(TimestampedSoftDeleteModel):
    pdit_id = models.AutoField(primary_key=True)
    tambo = models.ForeignKey(Tambo, on_delete=models.PROTECT, related_name='producciones_diarias')
    pdit_fecha = models.DateField()
    pdit_cantidad_producida = models.FloatField(null=True, blank=True)
    pdit_cantidad_consumida = models.FloatField(null=True, blank=True)
    pdit_cantidad_animales_productores = models.IntegerField(null=True, blank=True)
    unidad = models.ForeignKey(
        'catalogos.Unidad', on_delete=models.PROTECT,
        null=True, blank=True, related_name='producciones_tambo'
    )
    pdit_porcentaje_grasa = models.FloatField(null=True, blank=True)
    pdit_porcentaje_proteinas = models.FloatField(null=True, blank=True)
    pdit_observaciones = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        db_table = 'produccion_diaria_tambo'
        verbose_name = 'Producción Diaria Tambo'
        ordering = ['-pdit_fecha']