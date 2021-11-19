from rest_framework import serializers
from ..models import MonthlyMeliaEvaluation


class MonthlyMeliaEvaluationMiniSerliazer(serializers.ModelSerializer):
    payTimeName = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MonthlyMeliaEvaluation
        fields = [
            'payTimeName',
            'totalCalificacion',
            "totalPoints"
        ]

    def get_payTimeName(self, obj):
        return str(obj.payTime)


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
