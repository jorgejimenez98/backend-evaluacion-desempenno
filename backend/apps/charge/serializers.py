from rest_framework import serializers
from .models import Charge


class ChargeSerializer(serializers.ModelSerializer):
    ocupacion = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Charge
        fields = ['id_cargos', 'cod_cargo',
                  'descripcion', 'activo', 'ocupacion']

    def get_ocupacion(self, obj):
        return obj.fk_cat_ocupacion.descripcion
