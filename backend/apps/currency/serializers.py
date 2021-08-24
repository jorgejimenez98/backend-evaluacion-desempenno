from rest_framework import serializers
from .models import Currency


class CurrencyMiniSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Currency
        fields = ['id', 'name']

    def get_name(self, obj):
        return f'{obj.description.rstrip()}({obj.acronym.rstrip()})'


class CurrencySerializer(serializers.ModelSerializer):
    acronym = serializers.SerializerMethodField(read_only=True)
    description = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Currency
        fields = ['id', 'acronym', 'description', 'active']

    def get_description(self, obj):
        return obj.description.rstrip()

    def get_acronym(self, obj):
        return obj.acronym.rstrip()
