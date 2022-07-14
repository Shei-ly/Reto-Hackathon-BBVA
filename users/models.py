from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nombreCompleto = models.CharField(max_length=150, default=True)
    area = models.CharField(max_length=50, default=True)
    ubicacion = models.CharField(max_length=50, default=True)
    segmento = models.SmallIntegerField(default=True)
    perfil = models.CharField(max_length=50, default=True)
    
    def get_full_name(self):
        return f'{self.first_name}{self.last_name}'

