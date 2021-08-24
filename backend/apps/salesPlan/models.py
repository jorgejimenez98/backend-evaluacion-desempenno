from django.db import models
from ..hotel.models import Hotel
from ..currency.models import Currency
from ..family.models import Family
from ..sellArea.models import PuntoDeVenta


class AnualSalePlan(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, related_name='anualSalePlans')
    year = models.PositiveIntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.pk} Anual Sale PLan {self.hotel.name} - year: {self.year}'

    class Meta:
        unique_together = (('hotel', 'year', 'currency'),)
        index_together = (('hotel', 'year', 'currency'),)

    def getReport(self):
        lista = [i.getTuple() for i in self.monthlySalePlans.all()]
        lista.sort()
        if len(lista) > 0:
            data = []
            cur_fami = lista[0][0]
            cur_pvta = lista[0][1]
            pvtas = []
            meses = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 0]
            tot_fami = [0] * 13
            tot = [0] * 13

            for pvfa in lista:
                if pvfa[1] != cur_pvta:
                    pvtas.append((cur_pvta, meses[:]))
                    cur_pvta = pvfa[1]
                    meses = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 0]
                if pvfa[0] != cur_fami:
                    data.append((cur_fami, pvtas[:], tot_fami[:]))
                    cur_fami = pvfa[0]
                    pvtas = []
                    tot_fami = [0] * 13
                meses[pvfa[2] - 1] = pvfa[3]
                meses[12] += pvfa[3]
                tot_fami[pvfa[2] - 1] += pvfa[3]
                tot_fami[12] += pvfa[3]
                tot[pvfa[2] - 1] += pvfa[3]
                tot[12] += pvfa[3]

            pvtas.append((cur_pvta, meses[:]))
            data.append((cur_fami, pvtas[:], tot_fami[:]))
            data.append(tot)
            return data
        return []


class MonthlySalePlan(models.Model):
    anualSalePlan = models.ForeignKey(AnualSalePlan, on_delete=models.PROTECT, related_name='monthlySalePlans')
    month = models.CharField(max_length=218)
    family = models.ForeignKey(Family, on_delete=models.PROTECT)
    saleArea = models.ForeignKey(PuntoDeVenta, on_delete=models.PROTECT)
    plan = models.FloatField()

    def __str__(self):
        return f'{self.family.desc_grupo} {self.saleArea.desc_pvta} {self.plan}'

    class Meta:
        unique_together = (('month', 'anualSalePlan', 'family', 'saleArea'),)
        index_together = (('month', 'anualSalePlan', 'family', 'saleArea'),)

    def getTuple(self):
        return tuple((
            self.family.desc_grupo.rstrip().lstrip(),
            self.saleArea.desc_pvta.rstrip().lstrip(),
            self.getMonthNumber(),
            self.plan
        ))

    def getMonthNumber(self):
        return {i[1]: i[0] + 1 for i in enumerate(
            'Enero Febrero Marzo Abril Mayo Junio Julio Agosto Septiembre Octubre Noviembre Diciembre'.split())}[
            self.month]
