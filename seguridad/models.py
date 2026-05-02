from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

from core.models import TimestampedSoftDeleteModel


class UsuarioManager(BaseUserManager):
    def create_user(self, usua_nombre, password=None, **extra_fields):
        if not usua_nombre:
            raise ValueError('El nombre de usuario es obligatorio.')
        user = self.model(usua_nombre=usua_nombre, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usua_nombre, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(usua_nombre, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin, TimestampedSoftDeleteModel):
    usua_id = models.AutoField(primary_key=True)
    usua_nombre = models.CharField(max_length=50, unique=True)
    usua_persona_contacto = models.CharField(max_length=100, null=True, blank=True)
    usua_email = models.EmailField(max_length=100, null=True, blank=True)
    usua_observaciones = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'usua_nombre'
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.usua_nombre