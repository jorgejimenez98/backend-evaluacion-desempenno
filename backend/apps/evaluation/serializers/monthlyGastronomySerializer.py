from rest_framework import serializers
from ..models import MonthlyGastronomyEvaluation


class MonthlyGastronomyEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyGastronomyEvaluation
        fields = '__all__'
