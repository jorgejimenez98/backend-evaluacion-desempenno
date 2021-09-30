from django.db import models
from ..payTime.models import PayTime
from ..workers.models import Worker
from ..charge.models import Charge

"""
python manage.py migrate --fake APPNAME zero
This will make your migration to fake. Now you can run the migrate script
python manage.py migrate APPNAME
"""


class MonthlyEvaluation(models.Model):
    payTime = models.ForeignKey(PayTime, on_delete=models.PROTECT, related_name='monthlyEvaluations', null=False)
    evaluateWorker = models.ForeignKey(Worker, on_delete=models.PROTECT, null=False,
                                       related_name='workerMonthlyEvaluations')
    evaluateWorkerCharge = models.ForeignKey(Charge, on_delete=models.PROTECT, null=False,
                                             related_name='evaluateWorkerCharge')
    evaluatorWorker = models.ForeignKey(Worker, on_delete=models.PROTECT, null=False, related_name='evaluatorWorker')
    evaluatorWorkerCharge = models.ForeignKey(Charge, on_delete=models.PROTECT, null=False,
                                              related_name='evaluatorWorkerCharge')
    evaluationDate = models.DateField(auto_now_add=True)


class MonthlyMeliaEvaluation(MonthlyEvaluation):
    asist_punt = models.PositiveSmallIntegerField()
    dom_cum_tars = models.PositiveSmallIntegerField()
    trab_equipo = models.PositiveSmallIntegerField()
    cal_aten_cliente = models.PositiveSmallIntegerField()
    cui_area_rec_medios = models.PositiveSmallIntegerField()
    cump_normas = models.PositiveSmallIntegerField()
    cap_camb_ini_int = models.PositiveSmallIntegerField()
    observations = models.TextField()

    class Meta:
        app_label = "evaluation"
        managed = True

    def getCalifications(self):
        return [self.asist_punt, self.dom_cum_tars, self.trab_equipo, self.cal_aten_cliente,
                self.cui_area_rec_medios, self.cump_normas, self.cap_camb_ini_int]

    def totalCalificacion(self):
        calificaciones = self.getCalifications()
        totalPoints = sum(calificaciones)
        evaluacion = ''
        if totalPoints <= 14:
            evaluacion = 'M'
        if 14 < totalPoints <= 20:
            evaluacion = 'M'
        elif 20 < totalPoints <= 27:
            evaluacion = 'R'
        elif 27 < totalPoints <= 31:
            evaluacion = 'B'
            if 2 in calificaciones:
                evaluacion = 'R'
        elif 31 < totalPoints <= 35:
            evaluacion = 'MB'
            if 3 in calificaciones or 2 in calificaciones:
                evaluacion = 'B'
        return f'{totalPoints} - {evaluacion}'

    def totalPoints(self):
        return sum(self.getCalifications())

    def getDisscount(self):
        values = {14: 50, 15: 53, 16: 57, 17: 61, 18: 65, 19: 69, 20: 73, 21: 75, 22: 79, 23: 83, 24: 87, 25: 91,
                  26: 95, 27: 99}
        totalPoints = self.totalPoints()
        if totalPoints in values:
            return 100 - values[totalPoints]
        return 0


class MonthlyGastronomyEvaluation(MonthlyEvaluation):
    ind1_CDRI = models.PositiveSmallIntegerField()
    ind2_AMD = models.PositiveSmallIntegerField()
    ind3_PAPPI = models.PositiveSmallIntegerField()
    ind4_CEDP = models.PositiveSmallIntegerField()
    ind5_ROCR = models.PositiveSmallIntegerField()
    ind6_PCRBBRC = models.PositiveSmallIntegerField()
    ind7_CNPE = models.PositiveSmallIntegerField()
    ind8_CCPC = models.PositiveSmallIntegerField()
    ind9_NSC = models.PositiveSmallIntegerField()
    ind10_CPI = models.PositiveSmallIntegerField()
    ind11_INI = models.PositiveSmallIntegerField()
    ind12_RAP = models.PositiveSmallIntegerField()
    ind13_GV = models.PositiveSmallIntegerField()
    ind14_DF = models.PositiveSmallIntegerField()
    ind15_CTP = models.PositiveSmallIntegerField()
    ind16_AC = models.PositiveSmallIntegerField()
    ind17_DIS = models.PositiveSmallIntegerField()
    ind18_CDPA = models.PositiveSmallIntegerField()
    ind19_CTA = models.PositiveSmallIntegerField()
    ind20_HOPT = models.PositiveSmallIntegerField()
    ind21_CNSS = models.PositiveSmallIntegerField()
    ind22_UIE = models.PositiveSmallIntegerField()
    ind23_LCH = models.PositiveSmallIntegerField()
    ind24_APAT = models.PositiveSmallIntegerField()
    ind25_UCU = models.PositiveSmallIntegerField()

    class Meta:
        app_label = "evaluation"
        managed = True


class AnualEvaluation(models.Model):
    year = models.PositiveIntegerField()
    evaluateWorker = models.ForeignKey(Worker, on_delete=models.PROTECT, related_name='anualEvaluations')
    evaluateCharge = models.ForeignKey(Charge, on_delete=models.PROTECT)
    evaluationDate = models.DateField(auto_now_add=True)
    ind1_resume = models.TextField()
    ind2_cumpl = models.TextField()
    ind3_comport = models.TextField()
    ind4_uso_cuid = models.TextField()
    ind5_recomend = models.TextField()
    finalEvaluation = models.CharField(max_length=78)

    def __str__(self):
        return f'Anual Evaluation: {self.evaluateWorker.nombreCompleto()} - {self.finalEvaluation}'

    class Meta:
        index_together = (('year', 'evaluateWorker'),)
        unique_together = (('year', 'evaluateWorker'),)
