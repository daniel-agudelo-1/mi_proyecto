from django.db import models


class Cliente(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length = 200, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
# Create your models here.
