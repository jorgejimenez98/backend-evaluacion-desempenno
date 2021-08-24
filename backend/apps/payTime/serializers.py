from rest_framework import serializers
from .models import PayTime


class PayTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayTime
        fields = ['id', 'month', 'monthOrder', 'initialDate', 'endDate', 'year']
