from django import forms
from django.db import models


# Create your models here.
class Reserva(models.Model):
  #  ESTADOS = [('reservado', 'RESERVADO'),('completada','COMPLETADA'),('anulada','ANULADA'),('no asisten','NO ASISTEN')]

    nombre = models.CharField(max_length=80)
    telefono = models.IntegerField()
    fecha_reserva = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.IntegerField()
    correo = models.CharField(max_length=20)
    estado = models.CharField(max_length=16)
   