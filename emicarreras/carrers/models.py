from django.db import models

# Utils
from utils.common import AbstractAuditDatesModel


class Carrer(AbstractAuditDatesModel):

    name = models.CharField(max_length=200, verbose_name="Nombre del arma.")
    places_h = models.IntegerField(default=0, verbose_name="Número de lugares disponibles para hombres.")
    places_m = models.IntegerField(default=0, verbose_name="Número de lugares disponibles para mujeres.")

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
