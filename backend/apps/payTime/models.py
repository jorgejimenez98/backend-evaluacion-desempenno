from django.db import models


class PayTime(models.Model):
    id = models.IntegerField(primary_key=True)
    month = models.CharField(max_length=50)
    initialDate = models.DateTimeField()
    endDate = models.DateTimeField()
    monthOrder = models.IntegerField()  # mes numero
    year = models.IntegerField(blank=True, null=True)  # Anno
    isEliminated = models.BooleanField(default=False)

    def __str__(self):
        return f'Periodo de Pago {self.month} {self.year}'
