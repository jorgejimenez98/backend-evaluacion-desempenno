from rest_framework import serializers
from .models import PuntoDeVenta


class PuntoVentaMiniSerializer(serializers.ModelSerializer):
    desc_pvta = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PuntoDeVenta
        fields = ['id_pvta', 'desc_pvta']

    def get_desc_pvta(self, obj):
        return obj.desc_pvta.title().rstrip()


class PuntoDeVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoDeVenta
        fields = '__all__'
