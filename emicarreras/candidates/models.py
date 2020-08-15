# Django
from django.db import models

# Models
from carrers.models import Carrer

# Utils
from utils.common import AbstractAuditDatesModel

class Gender(AbstractAuditDatesModel):
    
    name = models.CharField(max_length=10, verbose_name="Género")

    class Meta:
        ordering = ("name",)
    
    def __str__(self):
        return f"{self.name}"


class Candidate(AbstractAuditDatesModel):

    first_name = models.CharField(max_length=100, verbose_name="Nombres")
    last_name = models.CharField(max_length=100, verbose_name="Apellido Paterno")
    matriname = models.CharField(max_length=100, verbose_name="Apellido Materno")
    carrer = models.ForeignKey(Carrer, null=True, blank=True, 
        related_name='user_carrer', on_delete=models.SET_NULL, verbose_name="Arma")
    gender = models.ForeignKey(Gender, null=True, blank=True, 
        related_name='user_gender', on_delete=models.SET_NULL, verbose_name="Genero")

    class Meta:
        ordering = ("last_name", "first_name", )
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}, {self.matriname}"
