from unittest.util import _MAX_LENGTH
from django.db import models

class Animal (models.Model):
    raza = models.CharField(max_length = 10)
    alimentacion = models.CharField(max_length = 10)
    fecha_de_nacimiento = models.DateField()