from django.db import models
from django.utils import timezone


class SoftDeleteQuerySet(models.QuerySet):
    def alive(self):
        return self.filter(fecha_baja__isnull=True)

    def dead(self):
        return self.filter(fecha_baja__isnull=False)

    def delete(self):
        return self.update(fecha_baja=timezone.now())

    def restore(self):
        return self.update(fecha_baja=None)


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).alive()


class AllObjectsManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db)


class TimestampedSoftDeleteModel(models.Model):
    fecha_alta = models.DateTimeField(default=timezone.now, editable=False)
    fecha_baja = models.DateTimeField(null=True, blank=True, editable=False)

    objects = SoftDeleteManager()
    all_objects = AllObjectsManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.fecha_baja = timezone.now()
        self.save(update_fields=['fecha_baja'])

    def restore(self):
        self.fecha_baja = None
        self.save(update_fields=['fecha_baja'])