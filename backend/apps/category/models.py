from django.db import models


class OccupationalCategory(models.Model):
    id_categ = models.IntegerField(primary_key=True)
    cod_categ = models.CharField(unique=True, max_length=20)
    descripcion = models.CharField(max_length=50)
    activo = models.BooleanField()
