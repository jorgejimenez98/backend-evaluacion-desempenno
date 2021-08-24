from rest_framework import serializers
from .models import OccupationalCategory
from ..charge.serializers import ChargeSerializer

class OccupationalCategoryMiniSerializer(serializers.ModelSerializer):
    cod_categ = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = OccupationalCategory
        fields = ['id_categ', 'cod_categ', 'descripcion', 'activo']

    def get_cod_categ(self, obj):
        return obj.cod_categ.rstrip()


class OccupationalCategorySerializer(OccupationalCategoryMiniSerializer):
    cargos = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = OccupationalCategory
        fields = ['id_categ', 'cod_categ', 'descripcion', 'activo', 'cargos']

    def get_cargos(self, obj):
        return ChargeSerializer(obj.charges.all(), many=True).data
