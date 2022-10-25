from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.

class Persona(models.Model):

    nombre =models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    fecha_de_nacimiento = models.DateField()

class Animal (models.Model):
    raza = models.CharField(max_length = 10)
    alimentacion = models.CharField(max_length = 10)
    fecha_de_nacimiento = models.DateField()
