# Create your models here.

from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    mensaje = models.TextField()
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.email
