from django.db import models
from apps.hotel.models import Hotel


# Restpvta === ZunPosGH, ColonPos
class PuntoDeVenta(models.Model):
    id_pvta = models.IntegerField(primary_key=True)
    cod_pvta = models.CharField(max_length=5)
    desc_pvta = models.CharField(max_length=25, blank=True, null=True)
    activo = models.BooleanField()
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, default=None, related_name='puntos_ventas')

    def __str__(self):
        return f'Punto De venta: {self.cod_pvta} - {self.desc_pvta} {self.activo}'

    class Meta:
        unique_together = (('cod_pvta', 'hotel'),)
        index_together = (('cod_pvta', 'hotel'),)
