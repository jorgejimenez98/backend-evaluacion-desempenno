from django.db import models


class Currency(models.Model):
    id = models.IntegerField(primary_key=True)  # id_moneda
    acronym = models.CharField(max_length=218)  # cod_mone
    description = models.CharField(max_length=218)  # desc_mone
    active = models.BooleanField()  # activo

    def __str__(self):
        return f'Currency {self.description}'
