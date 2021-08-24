from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    pos_db_name = models.CharField(max_length=128)
    pms_db_name = models.CharField(max_length=128)
    zunPrUnidadOrganizativaId = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return f'{self.name} POS: {self.pos_db_name} PMS: {self.pms_db_name} ID: {self.zunPrUnidadOrganizativaId}'
