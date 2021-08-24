from rest_framework import serializers
from ..models import AnualEvaluation


class AnualEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnualEvaluation
        fields = '__all__'
