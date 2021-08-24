from django.db import models
from ..category.models import OccupationalCategory


class Charge(models.Model):
    id_cargos = models.IntegerField(primary_key=True)
    cod_cargo = models.CharField(unique=True, max_length=5)
    descripcion = models.CharField(max_length=150)
    activo = models.BooleanField()
    fk_cat_ocupacion = models.ForeignKey(
        OccupationalCategory, models.PROTECT, related_name='charges')

    def __str__(self):
        return f'Cargo {self.descripcion}'
