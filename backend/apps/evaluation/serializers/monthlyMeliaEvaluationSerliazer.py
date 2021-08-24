from rest_framework import serializers
from ..models import MonthlyMeliaEvaluation


class MonthlyMeliaEvaluationSerliazer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyMeliaEvaluation
        fields = [
            'id',
            'payTime',
            'evaluateWorker',
            'evaluateWorkerCharge',
            'evaluatorWorker',
            'evaluatorWorkerCharge',
            'evaluationDate',
            'asist_punt',
            'dom_cum_tars',
            'trab_equipo',
            'cal_aten_cliente',
            'cui_area_rec_medios',
            'cump_normas',
            'cap_camb_ini_int',
            'observations',
            'totalCalificacion'
        ]
