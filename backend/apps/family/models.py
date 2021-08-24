from django.db import models


# Almngrup == ZunStockGH
class Family(models.Model):
    id_grupo = models.IntegerField(primary_key=True)
    cod_grupo = models.CharField(max_length=2)
    desc_grupo = models.CharField(max_length=70, blank=True, null=True)
    activo = models.BooleanField()

    def __str__(self):
        return f'Familia {self.id_grupo} - {self.desc_grupo}'
